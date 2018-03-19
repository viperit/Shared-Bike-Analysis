# encoding: utf-8

import csv
import function


# 构建2km以内的邻居表
def _create_region_table():
    print("_create_region_table")
    node_region = {}

    def getImax(i):
        if i == 0:
            iMax = 12
        elif i == 1 or i == 2:
            iMax = 11
        elif i == 3:
            iMax = 10
        elif i == 4:
            iMax = 9
        elif i == 5 or i == 6:
            iMax = 8
        elif i == 7:
            iMax = 7
        elif i == 8:
            iMax = 6
        elif i == 9 or i == 10:
            iMax = 5
        elif i == 11:
            iMax = 4
        elif i == 12:
            iMax = 3
        elif i == 13:
            iMax = 2
        elif i == 14 or i == 15:
            iMax = 1
        else:
            iMax = 0
        return iMax

    node_neis = function.getAll_node_nei()
    AllNode = set()  # 全部的点（出现过的点+出现过的点邻居点），大约快20万
    for key, value in node_neis.items():
        for node in value:
            AllNode.add(node)

    for node in AllNode:
        node_region[node] = []

        currentCenter = node
        for i in range(17):  # 右边17个
            nextNode = function.calculate(currentCenter, len(currentCenter), 'right')
            node_region[node].append(nextNode)
            currentCenter = nextNode

        currentCenter = node
        for i in range(17):  # 左边17个
            nextNode = function.calculate(currentCenter, len(currentCenter), 'left')
            node_region[node].append(nextNode)
            currentCenter = nextNode

        for i in range(17):

            currentCenter = node_region[node][i]
            iMax = getImax(i)

            for k in range(iMax):
                nextNode = function.calculate(currentCenter, len(currentCenter), 'top')
                node_region[node].append(nextNode)
                currentCenter = nextNode
            currentCenter = node_region[node][i]
            for k in range(iMax):
                nextNode = function.calculate(currentCenter, len(currentCenter), 'bottom')
                node_region[node].append(nextNode)
                currentCenter = nextNode

        for i in range(17):

            currentCenter = node_region[node][i + 17]
            iMax = getImax(i)

            for k in range(iMax):
                nextNode = function.calculate(currentCenter, len(currentCenter), 'top')
                node_region[node].append(nextNode)
                currentCenter = nextNode
            currentCenter = node_region[node][i + 17]
            for k in range(iMax):
                nextNode = function.calculate(currentCenter, len(currentCenter), 'bottom')
                node_region[node].append(nextNode)
                currentCenter = nextNode
        currentCenter = node
        for i in range(13):
            nextNode = function.calculate(currentCenter, len(currentCenter), 'top')
            node_region[node].append(nextNode)
            currentCenter = nextNode

        currentCenter = node
        for i in range(13):
            nextNode = function.calculate(currentCenter, len(currentCenter), 'bottom')
            node_region[node].append(nextNode)
            currentCenter = nextNode

        node_region[node].append(node)

    with open("./data/temp/region.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region.items():
            writer.writerow([key, value])


# 构建每个点出发到达次数（非geofly）
def _create_loc_frequency_table():
    print("_create_loc_frequency_table")
    node_count_start = {}
    node_count_end = {}
    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]

        if start not in node_count_start:  # 得到每个点出发了几次
            node_count_start[start] = 1
        else:
            node_count_start[start] += 1

        if end not in node_count_end:  # 得到每个点到达了几次
            node_count_end[end] = 1
        else:
            node_count_end[end] += 1

    # 读取node_region
    i = 0
    node_region = {}
    csv_reader = csv.reader(open('./data/temp/region.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_region[row[0]] = eval(row[1])

    # 读取node_neis
    i = 0
    node_neis = {}
    csv_reader = csv.reader(open('./data/temp/neighbour.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_neis[row[0]] = eval(row[1])

    # 得到geofly之前的进、出、总热度
    i = 0
    node_region_start_ratio = {}
    node_region_end_ratio = {}
    node_region_overall_ratio = {}
    for node in node_region:  # 对于所有

        neis = node_region[node]

        total_start = 0
        total_end = 0

        total_node = 0
        total_region = 0

        for nei in neis:
            if nei in node_count_start:
                total_start += node_count_start[nei]  # 区域内总出发
                total_region += node_count_start[nei]  # 区域内总进出
            if nei in node_count_end:
                total_end += node_count_end[nei]  # 区域内总进
                total_region += node_count_end[nei]  # 区域内总进出

        if node in node_count_start:  # 如果该点出发过
            node_region_start_ratio[node] = node_count_start[node] / total_start  # region出发热度
            total_node += node_count_start[node]  # 计算总热度
        else:
            node_region_start_ratio[node] = -1  # 不存在

        if node in node_count_end:  # 如果该点被到达过
            node_region_end_ratio[node] = node_count_end[node] / total_end  # region到达热度
            total_node += node_count_end[node]  # 计算总热
        else:
            node_region_end_ratio[node] = -1  # 不存在

        if total_region == 0 or total_node == 0:
            node_region_overall_ratio[node] = -1
        else:
            node_region_overall_ratio[node] = total_node / total_region

    with open("./data/temp/feature_table/node_region_start_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_start_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_end_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_end_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_overall_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_overall_ratio.items():
            writer.writerow([key, value])


def _create_loc_geofly_frequency_table():
    print("_create_loc_geofly_frequency_table")
    # geofly
    node_count_start_geofly = {}
    node_count_end_geofly = {}
    node_count_start = {}
    node_count_end = {}

    # 读取node_region
    i = 0
    node_region = {}
    csv_reader = csv.reader(open('./data/temp/region.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_region[row[0]] = eval(row[1])

    # 读取node_neis
    i = 0
    node_neis = {}
    csv_reader = csv.reader(open('./data/temp/neighbour.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_neis[row[0]] = eval(row[1])

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        starts = node_neis[row[5]]
        ends = node_neis[row[6]]

        for start in starts:
            if start not in node_count_start_geofly:
                node_count_start_geofly[start] = 1
            else:
                node_count_start_geofly[start] += 1
        for end in ends:
            if end not in node_count_end_geofly:
                node_count_end_geofly[end] = 1
            else:
                node_count_end_geofly[end] += 1

        if row[5] not in node_count_start:
            node_count_start[row[5]] = 1
        else:
            node_count_start[row[5]] += 1

        if row[6] not in node_count_end:
            node_count_end[row[6]] = 1
        else:
            node_count_end[row[6]] += 1

    i = 0
    node_region_start_geofly_ratio = {}
    node_region_end_geofly_ratio = {}

    node_geofly_region_overall_ratio = {}
    for node in node_region:  # 区域内每一个点都进行热门度计算，约20万

        neis = node_region[node]
        total_start = 0
        total_end = 0

        total_node = 0  # 计算该点的进出
        total_region = 0  # 计算区域内的进出

        for nei in neis:
            if nei in node_count_start:
                total_start += node_count_start[nei]  # 只能算没有fly前的次数
                total_region += node_count_start[nei]
            if nei in node_count_end:
                total_end += node_count_end[nei]  # 只能算没有fly前的次数
                total_region += node_count_end[nei]

        if node in node_count_start_geofly:
            node_region_start_geofly_ratio[node] = node_count_start_geofly[node] / total_start
            total_node += node_count_start_geofly[node]
        else:
            node_region_start_geofly_ratio[node] = 0

        if node in node_count_end_geofly:
            node_region_end_geofly_ratio[node] = node_count_end_geofly[node] / total_end
            total_node += node_count_end_geofly[node]
        else:
            node_region_end_geofly_ratio[node] = 0

        if total_region == 0 or total_node == 0:
            node_geofly_region_overall_ratio[node] = -1
        else:
            node_geofly_region_overall_ratio[node] = total_node / total_region

    with open("./data/temp/feature_table/node_region_start_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_start_geofly_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_end_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_end_geofly_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_geofly_region_overall_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_geofly_region_overall_ratio.items():
            writer.writerow([key, value])


def _create_user_use_end_table():
    print("_create_user_use_end_table")

    def get_user_use_end():
        user_use_end = {}

        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            end = row[6]

            if user not in user_use_end:
                user_use_end[user] = {}
                user_use_end[user][end] = 1
            else:
                if end not in user_use_end[user]:
                    user_use_end[user][end] = 1
                else:
                    user_use_end[user][end] += 1
        return user_use_end

    user_use_end = get_user_use_end()
    with open("./data/temp/feature_table/user_use_end.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_use_end.items():
            writer.writerow([key, value])


def _create_user_use_start_table():
    print("_create_user_use_start_table")

    def get_user_use_start():
        user_use_start = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            start = row[5]

            if user not in user_use_start:
                user_use_start[user] = {}
                user_use_start[user][start] = 1
            else:
                if start not in user_use_start[user]:
                    user_use_start[user][start] = 1
                else:
                    user_use_start[user][start] += 1
        return user_use_start

    user_use_start = get_user_use_start()
    with open("./data/temp/feature_table/user_use_start.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_use_start.items():
            writer.writerow([key, value])


# 读取node_region
def _get_node_region():
    i = 0
    node_region = {}
    csv_reader = csv.reader(open('./data/temp/region.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_region[row[0]] = eval(row[1])
    return node_region


# 读取node_neis
def _get_node_neis():
    i = 0
    node_neis = {}
    csv_reader = csv.reader(open('./data/temp/neighbour.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        node_neis[row[0]] = eval(row[1])
    return node_neis


# 读取user_count
def _get_user_count():
    i = 0
    user_count = {}
    csv_reader = csv.reader(open('./data/temp/user_count.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_count[row[0]] = eval(row[1])

    return user_count


# 读取user_use_end
def _get_user_use_end():
    i = 0
    user_use_end = {}
    csv_reader = csv.reader(open('./data/temp/feature_table/user_use_end.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_use_end[row[0]] = eval(row[1])

    return user_use_end


# 读取user_use_end_geofly
def _get_user_use_end_geofly():
    i = 0
    user_use_end_geofly = {}
    csv_reader = csv.reader(open('./data/temp/feature_table/user_use_end_geofly.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_use_end_geofly[row[0]] = eval(row[1])

    return user_use_end_geofly


# 读取user_use_start
def _get_user_use_start():
    i = 0
    user_use_start = {}
    csv_reader = csv.reader(open('./data/temp/feature_table/user_use_start.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_use_start[row[0]] = eval(row[1])

    return user_use_start


# 读取user_use_start_geofly
def _get_user_use_start_geofly():
    i = 0
    user_use_start_geofly = {}
    csv_reader = csv.reader(open('./data/temp/feature_table/user_use_start_geofly.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_use_start_geofly[row[0]] = eval(row[1])

    return user_use_start_geofly


def _create_user_loc_as_end_ratio_table(user_use_end, user_count):
    def get_user_loc_as_end_ratio(user_use_end, user_count):
        user_loc_as_end_ratio = {}
        for user in user_use_end:
            user_loc_as_end_ratio[user] = {}
            for end in user_use_end[user]:
                user_loc_as_end_ratio[user][end] = user_use_end[user][end] / user_count[user]
        return user_loc_as_end_ratio

    user_loc_as_end_ratio = get_user_loc_as_end_ratio(user_use_end, user_count)
    with open("./data/temp/feature_table/user_loc_as_end_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_loc_as_end_ratio.items():
            writer.writerow([key, value])


def _create_user_loc_as_start_ratio(user_use_start, user_count):
    def get_user_loc_as_start_ratio(user_use_start, user_count):
        user_loc_as_start_ratio = {}
        for user in user_use_start:
            user_loc_as_start_ratio[user] = {}
            for start in user_use_start[user]:
                user_loc_as_start_ratio[user][start] = user_use_start[user][start] / user_count[user]
        return user_loc_as_start_ratio

    user_loc_as_start_ratio = get_user_loc_as_start_ratio(user_use_start, user_count)
    with open("./data/temp/feature_table/user_loc_as_start_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_loc_as_start_ratio.items():
            writer.writerow([key, value])


def _create_user_loc_as_end_geofly_ratio_table(user_use_end_geofly, user_count):
    def get_user_loc_as_end_geofly_ratio(user_use_end_geofly, user_count):
        user_loc_as_end_geofly_ratio = {}
        for user in user_use_end_geofly:
            user_loc_as_end_geofly_ratio[user] = {}
            for end in user_use_end_geofly[user]:
                user_loc_as_end_geofly_ratio[user][end] = user_use_end_geofly[user][end] / user_count[user]
        return user_loc_as_end_geofly_ratio

    user_loc_as_end_geofly_ratio = get_user_loc_as_end_geofly_ratio(user_use_end_geofly, user_count)
    with open("./data/temp/feature_table/user_loc_as_end_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_loc_as_end_geofly_ratio.items():
            writer.writerow([key, value])


def _create_user_loc_as_start_geofly_ratio_table(user_use_start_geofly, user_count):
    def get_user_loc_as_start_geofly_ratio(user_use_start_geofly, user_count):
        user_loc_as_start_geofly_ratio = {}
        for user in user_use_start_geofly:
            user_loc_as_start_geofly_ratio[user] = {}
            for start in user_use_start_geofly[user]:
                user_loc_as_start_geofly_ratio[user][start] = user_use_start_geofly[user][start] / user_count[user]
        return user_loc_as_start_geofly_ratio

    user_loc_as_start_geofly_ratio = get_user_loc_as_start_geofly_ratio(user_use_start_geofly, user_count)
    with open("./data/temp/feature_table/user_loc_as_start_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_loc_as_start_geofly_ratio.items():
            writer.writerow([key, value])


def _create_user_use_end_geofly_ratio(node_neis):
    def get_user_use_end_geofly():
        user_use_end_geofly = {}

        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            ends = node_neis[row[6]]

            if user not in user_use_end_geofly:
                user_use_end_geofly[user] = {}
                for end in ends:
                    user_use_end_geofly[user][end] = 1
            else:
                for end in ends:
                    if end not in user_use_end_geofly[user]:
                        user_use_end_geofly[user][end] = 1
                    else:
                        user_use_end_geofly[user][end] += 1
        return user_use_end_geofly

    user_use_end_geofly = get_user_use_end_geofly()
    with open("./data/temp/feature_table/user_use_end_geofly.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_use_end_geofly.items():
            writer.writerow([key, value])


def _create_user_use_start_geofly_table(node_neis):
    def get_user_use_start_geofly(node_neis):
        user_use_start_geofly = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            starts = node_neis[row[5]]

            if user not in user_use_start_geofly:
                user_use_start_geofly[user] = {}
                for start in starts:
                    user_use_start_geofly[user][start] = 1
            else:
                for start in starts:
                    if start not in user_use_start_geofly[user]:
                        user_use_start_geofly[user][start] = 1
                    else:
                        user_use_start_geofly[user][start] += 1
        return user_use_start_geofly

    user_use_start_geofly = get_user_use_start_geofly(node_neis)
    with open("./data/temp/feature_table/user_use_start_geofly.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_use_start_geofly.items():
            writer.writerow([key, value])


def render_feature_table():
    # pass
    _create_region_table()
    _create_loc_frequency_table()
    _create_loc_geofly_frequency_table()
    _create_user_use_end_table()
    _create_user_use_start_table()

    user_count = _get_user_count()
    user_use_start = _get_user_use_start()
    user_use_end = _get_user_use_end()

    _create_user_loc_as_end_ratio_table(user_use_end, user_count)
    _create_user_loc_as_start_ratio(user_use_start, user_count)

    node_neis = _get_node_neis()
    _create_user_use_end_geofly_ratio(node_neis)
    _create_user_use_start_geofly_table(node_neis)

    user_use_start_geofly = _get_user_use_start_geofly()
    user_use_end_geofly = _get_user_use_end_geofly()

    _create_user_loc_as_start_geofly_ratio_table(user_use_start_geofly, user_count)
    _create_user_loc_as_end_geofly_ratio_table(user_use_end_geofly, user_count)
