# encoding: utf-8

"""
时间+单地点

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


# 创建每个小时内每个点的进、出、总热度表
# ./data/temp/feature_table/node_region_hour_start_ratio.csv
# ./data/temp/feature_table/node_region_hour_end_ratio.csv
# ./data/temp/feature_table/node_region_hour_overall_ratio.csv
def _create_node_region_hour_ratio_table(node_region):
    print("_create_node_region_hour_ratio_table")

    # 得到每个小时每个点的出发和到达次数
    node_count_hour_start = {}
    node_count_hour_end = {}
    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]
        hour = row[7]

        if hour not in node_count_hour_start:
            node_count_hour_start[hour] = {}
            node_count_hour_start[hour][start] = 1
        else:
            if start not in node_count_hour_start[hour]:
                node_count_hour_start[hour][start] = 1
            else:
                node_count_hour_start[hour][start] += 1

        if hour not in node_count_hour_end:
            node_count_hour_end[hour] = {}
            node_count_hour_end[hour][end] = 1
        else:
            if end not in node_count_hour_end[hour]:
                node_count_hour_end[hour][end] = 1
            else:
                node_count_hour_end[hour][end] += 1

    # 得到geofly之前的进、出、总热度
    def get_hour_ratio(node_region, node_count_start, node_count_end):

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

        return node_region_start_ratio, node_region_end_ratio, node_region_overall_ratio

    node_region_hour_start_ratio = {}
    node_region_hour_end_ratio = {}
    node_region_hour_overall_ratio = {}
    for hour in node_count_hour_start:
        node_region_hour_start_ratio[hour], \
        node_region_hour_end_ratio[hour], \
        node_region_hour_overall_ratio[hour] = get_hour_ratio(node_region, \
                                                              node_count_hour_start[hour], node_count_hour_end[hour])

    with open("./data/temp/feature_table/node_region_hour_start_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_start_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_hour_end_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_end_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_hour_overall_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_overall_ratio.items():
            writer.writerow([key, value])


# 创建每个小时内每个点的进、出、总热度表(geofly后)
# ./data/temp/feature_table/node_region_hour_start_geofly_ratio.csv
# ./data/temp/feature_table/node_region_hour_end_geofly_ratio.csv
# ./data/temp/feature_table/node_region_hour_overall_geofly_ratio.csv
def _create_node_region_hour_geofly_ratio_table(node_region):
    print("_create_node_region_hour_geofly_ratio_table")

    # 得到每个小时每个点的出发和到达次数(用于计算热度比例)
    node_count_hour_start = {}
    node_count_hour_end = {}
    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]
        hour = row[7]

        if hour not in node_count_hour_start:
            node_count_hour_start[hour] = {}
            node_count_hour_start[hour][start] = 1
        else:
            if start not in node_count_hour_start[hour]:
                node_count_hour_start[hour][start] = 1
            else:
                node_count_hour_start[hour][start] += 1

        if hour not in node_count_hour_end:
            node_count_hour_end[hour] = {}
            node_count_hour_end[hour][end] = 1
        else:
            if end not in node_count_hour_end[hour]:
                node_count_hour_end[hour][end] = 1
            else:
                node_count_hour_end[hour][end] += 1

    # 得到geofly每个小时每个点的出发和到达次数
    node_count_hour_start_geofly = {}
    node_count_hour_end_geofly = {}
    i = 0
    csv_reader = csv.reader(open('./data/train_start_geofly.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]
        hour = row[7]

        if hour not in node_count_hour_start_geofly:
            node_count_hour_start_geofly[hour] = {}
            node_count_hour_start_geofly[hour][start] = 1
        else:
            if start not in node_count_hour_start_geofly[hour]:
                node_count_hour_start_geofly[hour][start] = 1
            else:
                node_count_hour_start_geofly[hour][start] += 1

    i = 0
    csv_reader = csv.reader(open('./data/train_end_geofly.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]
        hour = row[7]

        if hour not in node_count_hour_end_geofly:
            node_count_hour_end_geofly[hour] = {}
            node_count_hour_end_geofly[hour][end] = 1
        else:
            if end not in node_count_hour_end_geofly[hour]:
                node_count_hour_end_geofly[hour][end] = 1
            else:
                node_count_hour_end_geofly[hour][end] += 1

    # 得到geofly的进、出、总热度
    def get_hour_ratio_geofly(node_region, node_count_start, node_count_end, node_count_start_geofly,
                              node_count_end_geofly):

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
                    total_start += node_count_start[nei]  # 区域内总出发  只能算没有fly前的次数
                    total_region += node_count_start[nei]  # 区域内总进出
                if nei in node_count_end:
                    total_end += node_count_end[nei]  # 区域内总进   只能算没有fly前的次数
                    total_region += node_count_end[nei]  # 区域内总进出

            if node in node_count_start_geofly:  # 如果该点出发过
                node_region_start_ratio[node] = node_count_start_geofly[node] / total_start  # region出发热度
                total_node += node_count_start_geofly[node]  # 计算总热度
            else:
                node_region_start_ratio[node] = -1  # 不存在

            if node in node_count_end_geofly:  # 如果该点被到达过
                node_region_end_ratio[node] = node_count_end_geofly[node] / total_end  # region到达热度
                total_node += node_count_end_geofly[node]  # 计算总热
            else:
                node_region_end_ratio[node] = -1  # 不存在

            if total_region == 0 or total_node == 0:
                node_region_overall_ratio[node] = -1
            else:
                node_region_overall_ratio[node] = total_node / total_region

        return node_region_start_ratio, node_region_end_ratio, node_region_overall_ratio

    node_region_hour_start_geofly_ratio = {}
    node_region_hour_end_geofly_ratio = {}
    node_region_hour_overall_geofly_ratio = {}
    for hour in node_count_hour_start_geofly:
        node_region_hour_start_geofly_ratio[hour], \
        node_region_hour_end_geofly_ratio[hour], \
        node_region_hour_overall_geofly_ratio[hour] = get_hour_ratio_geofly(node_region, \
                                                                            node_count_hour_start[hour],
                                                                            node_count_hour_end[hour], \
                                                                            node_count_hour_start_geofly[hour], \
                                                                            node_count_hour_end_geofly[hour])

    with open("./data/temp/feature_table/node_region_hour_start_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_start_geofly_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_hour_end_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_end_geofly_ratio.items():
            writer.writerow([key, value])

    with open("./data/temp/feature_table/node_region_hour_overall_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in node_region_hour_overall_geofly_ratio.items():
            writer.writerow([key, value])


def render_feature_table_part_4():
    print("render_feature_table_part_4")

    node_neis = _get_node_neis()

    _create_node_region_hour_ratio_table(node_neis)
    _create_node_region_hour_geofly_ratio_table(node_neis)

    print("-----------------------------")
