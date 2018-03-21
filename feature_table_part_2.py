# encoding: utf-8

"""
单用户+单地点

"""

import csv


# 读取node_neis
# ./data/temp/neighbour.csv
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
# ./data/temp/user_count.csv
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


# 读取user_use_start
# ./data/temp/feature_table/user_use_start.csv
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


# 读取user_use_end
# ./data/temp/feature_table/user_use_end.csv
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


# 读取user_use_start_geofly
# ./data/temp/feature_table/user_use_start_geofly.csv
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


# 读取user_use_end_geofly
# ./data/temp/feature_table/user_use_end_geofly.csv
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


# 创建用户使用的起点的次数表
# ./data/temp/feature_table/user_use_start.csv
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


# 创建用户使用的终点的次数表
# ./data/temp/feature_table/user_use_end.csv
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


# 创建用户使用的终点的次数（geofly）表
# ./data/temp/feature_table/user_use_end_geofly.csv
def _create_user_use_end_geofly_ratio(node_neis):
    def get_user_use_end_geofly(node_neis):
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

    user_use_end_geofly = get_user_use_end_geofly(node_neis)
    with open("./data/temp/feature_table/user_use_end_geofly.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_use_end_geofly.items():
            writer.writerow([key, value])


# 创建用户使用起点的次数（geofly）表
# ./data/temp/feature_table/user_use_start_geofly.csv
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


# 用户去某一点的比例
# 所有点都集中在此表上，不区分起点和终点
# ./data/temp/feature_table/user_loc_as_end_ratio.csv
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


# 用户从某点出发的比例
# 所有点都集中在此表上，不区分起点和终点
# ./data/temp/feature_table/user_loc_as_start_ratio.csv
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


# geofly后，用户去某一点的比例
# 所有点都集中在此表上，不区分起点和终点
# ./data/temp/feature_table/user_loc_as_end_geofly_ratio.csv
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


# geofly后，用户从某点出发的比例
# 所有点都集中在此表上，不区分起点和终点
# ./data/temp/feature_table/user_loc_as_start_geofly_ratio.csv
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


def render_feature_table_part_2():
    print("render_feature_table_part_2")

    # 获取缓存表
    user_count = _get_user_count()
    user_use_start = _get_user_use_start()
    user_use_end = _get_user_use_end()
    node_neis = _get_node_neis()
    user_use_start_geofly = _get_user_use_start_geofly()
    user_use_end_geofly = _get_user_use_end_geofly()

    # 中间结果的辅助表
    _create_user_use_start_table()
    _create_user_use_end_table()

    _create_user_use_start_geofly_table(node_neis)
    _create_user_use_end_geofly_ratio(node_neis)

    # 中间结果
    _create_user_loc_as_end_ratio_table(user_use_end, user_count)
    _create_user_loc_as_start_ratio(user_use_start, user_count)

    _create_user_loc_as_start_geofly_ratio_table(user_use_start_geofly, user_count)
    _create_user_loc_as_end_geofly_ratio_table(user_use_end_geofly, user_count)

    print("-----------------------------")
