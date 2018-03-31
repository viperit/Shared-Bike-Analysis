# encoding: utf-8

"""
全用户+单地点

"""

import csv
import pickle


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


def get_pickle(path):
    pkl_file = open(path, 'rb')

    return pickle.load(pkl_file)


# 起点到终点次数，未漂移
# ./data/temp/start_to_end_count
def _create_start_to_end_count_table():
    print("_create_start_to_end_count_table")

    start_to_end_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]

        if start not in start_to_end_count:
            start_to_end_count[start] = {}
            start_to_end_count[start][end] = 1

        else:
            if end not in start_to_end_count[start]:
                start_to_end_count[start][end] = 1

            else:
                start_to_end_count[start][end] += 1

    with open('./data/temp/start_to_end_count', 'wb+') as f:
        pickle.dump(start_to_end_count, f, pickle.HIGHEST_PROTOCOL)


# 起点到终点次数，起点漂移
# ./data/temp/start_geofly_to_end_count
def _create_start_geofly_to_end_count_table(node_neis):
    print("_create_start_geofly_to_end_count_table")

    start_geofly_to_end_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        starts = node_neis[row[5]]
        end = row[6]

        for start in starts:
            if start not in start_geofly_to_end_count:
                start_geofly_to_end_count[start] = {}
                start_geofly_to_end_count[start][end] = 1

            else:
                if end not in start_geofly_to_end_count[start]:
                    start_geofly_to_end_count[start][end] = 1

                else:
                    start_geofly_to_end_count[start][end] += 1

    with open('./data/temp/start_geofly_to_end_count', 'wb+') as f:
        pickle.dump(start_geofly_to_end_count, f, pickle.HIGHEST_PROTOCOL)


# 起点到终点次数，终点漂移
# ./data/temp/start_to_end_geofly_count
def _create_start_to_end_geofly_count_table(node_neis):
    print("_create_start_to_end_geofly_count_table")

    start_to_end_geofly_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        ends = node_neis[row[6]]

        if start not in start_to_end_geofly_count:
            start_to_end_geofly_count[start] = {}

            for end in ends:
                start_to_end_geofly_count[start][end] = 1

        else:
            for end in ends:
                if end not in start_to_end_geofly_count[start]:
                    start_to_end_geofly_count[start][end] = 1

                else:
                    start_to_end_geofly_count[start][end] += 1

    with open('./data/temp/start_to_end_geofly_count', 'wb+') as f:
        pickle.dump(start_to_end_geofly_count, f, pickle.HIGHEST_PROTOCOL)


# 起点到终点次数，都漂移
# ./data/temp/start_geofly_to_end_geofly_count
def _create_start_geofly_to_end_geofly_count_table(node_neis):
    print("_create_start_geofly_to_end_geofly_count_table")

    start_geofly_to_end_geofly_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        starts = node_neis[row[5]]
        ends = node_neis[row[6]]

        for start in starts:
            if start not in start_geofly_to_end_geofly_count:
                start_geofly_to_end_geofly_count[start] = {}

                for end in ends:
                    start_geofly_to_end_geofly_count[start][end] = 1

            else:
                for end in ends:
                    if end not in start_geofly_to_end_geofly_count[start]:
                        start_geofly_to_end_geofly_count[start][end] = 1

                    else:
                        start_geofly_to_end_geofly_count[start][end] += 1

    with open('./data/temp/start_geofly_to_end_geofly_count', 'wb+') as f:
        pickle.dump(start_geofly_to_end_geofly_count, f, pickle.HIGHEST_PROTOCOL)


# 每小时起点到终点次数，未漂移
# ./data/temp/cur_hour_start_to_end_count
def _create_cur_hour_start_to_end_count_table():
    print("_create_cur_hour_start_to_end_count_table")

    cur_hour_start_to_end_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        end = row[6]
        hour = row[7]

        if start not in cur_hour_start_to_end_count:
            cur_hour_start_to_end_count[start] = {}
            cur_hour_start_to_end_count[start][end] = {}
            cur_hour_start_to_end_count[start][end][hour] = 1

        else:
            if end not in cur_hour_start_to_end_count[start]:
                cur_hour_start_to_end_count[start][end] = {}
                cur_hour_start_to_end_count[start][end][hour] = 1

            else:
                if hour not in cur_hour_start_to_end_count[start][end]:
                    cur_hour_start_to_end_count[start][end][hour] = 1

                else:
                    cur_hour_start_to_end_count[start][end][hour] += 1

    with open('./data/temp/cur_hour_start_to_end_count', 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_count, f, pickle.HIGHEST_PROTOCOL)


# 每小时起点到终点次数，起点漂移
# ./data/temp/cur_hour_start_geofly_to_end_count
def _create_cur_hour_start_geofly_to_end_count_table(node_neis):
    print("_create_cur_hour_start_geofly_to_end_count_table")

    cur_hour_start_geofly_to_end_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        starts = node_neis[row[5]]
        end = row[6]
        hour = row[7]

        for start in starts:
            if start not in cur_hour_start_geofly_to_end_count:
                cur_hour_start_geofly_to_end_count[start] = {}
                cur_hour_start_geofly_to_end_count[start][end] = {}
                cur_hour_start_geofly_to_end_count[start][end][hour] = 1

            else:
                if end not in cur_hour_start_geofly_to_end_count[start]:
                    cur_hour_start_geofly_to_end_count[start][end] = {}
                    cur_hour_start_geofly_to_end_count[start][end][hour] = 1

                else:
                    if hour not in cur_hour_start_geofly_to_end_count[start][end]:
                        cur_hour_start_geofly_to_end_count[start][end][hour] = 1

                    else:
                        cur_hour_start_geofly_to_end_count[start][end][hour] += 1

    with open('./data/temp/cur_hour_start_geofly_to_end_count', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_count, f, pickle.HIGHEST_PROTOCOL)


# 每小时起点到终点次数，终点漂移
# ./data/temp/cur_hour_start_to_end_geofly_count
def _create_cur_hour_start_to_end_geofly_count_table(node_neis):
    print("_create_cur_hour_start_to_end_geofly_count_table")

    cur_hour_start_to_end_geofly_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        start = row[5]
        ends = node_neis[row[6]]
        hour = row[7]

        if start not in cur_hour_start_to_end_geofly_count:
            cur_hour_start_to_end_geofly_count[start] = {}

            for end in ends:
                cur_hour_start_to_end_geofly_count[start][end] = {}
                cur_hour_start_to_end_geofly_count[start][end][hour] = 1

        else:
            for end in ends:
                if end not in cur_hour_start_to_end_geofly_count[start]:
                    cur_hour_start_to_end_geofly_count[start][end] = {}
                    cur_hour_start_to_end_geofly_count[start][end][hour] = 1

                else:
                    if hour not in cur_hour_start_to_end_geofly_count[start][end]:
                        cur_hour_start_to_end_geofly_count[start][end][hour] = 1

                    else:
                        cur_hour_start_to_end_geofly_count[start][end][hour] += 1

    with open('./data/temp/cur_hour_start_to_end_geofly_count', 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_geofly_count, f, pickle.HIGHEST_PROTOCOL)


# 每小时起点到终点次数，都漂移
# ./data/temp/cur_hour_start_geofly_to_end_geofly_count
def _create_cur_hour_start_geofly_to_end_geofly_count_table(node_neis):
    print("_create_cur_hour_start_geofly_to_end_geofly_count_table")

    cur_hour_start_geofly_to_end_geofly_count = {}

    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))

    for row in csv_reader:
        i += 1
        if i == 1:
            continue

        starts = node_neis[row[5]]
        ends = node_neis[row[6]]
        hour = row[7]

        for start in starts:
            if start not in cur_hour_start_geofly_to_end_geofly_count:
                cur_hour_start_geofly_to_end_geofly_count[start] = {}

                for end in ends:
                    cur_hour_start_geofly_to_end_geofly_count[start][end] = {}
                    cur_hour_start_geofly_to_end_geofly_count[start][end][hour] = 1

            else:
                for end in ends:
                    if end not in cur_hour_start_geofly_to_end_geofly_count[start]:
                        cur_hour_start_geofly_to_end_geofly_count[start][end] = {}
                        cur_hour_start_geofly_to_end_geofly_count[start][end][hour] = 1

                    else:
                        if hour not in cur_hour_start_geofly_to_end_geofly_count[start][end]:
                            cur_hour_start_geofly_to_end_geofly_count[start][end][hour] = 1

                        else:
                            cur_hour_start_geofly_to_end_geofly_count[start][end][hour] += 1

    with open('./data/temp/cur_hour_start_geofly_to_end_geofly_count', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_count, f, pickle.HIGHEST_PROTOCOL)


def _get_cur_hour_start_or_end_count(cur_hour_start_to_end_count):
    print("_get_cur_hour_start_or_end_count")

    cur_hour_start_count = {}
    cur_hour_end_count = {}
    for start in cur_hour_start_to_end_count:
        if start not in cur_hour_start_count:
            cur_hour_start_count[start] = {}

            for end in cur_hour_start_to_end_count[start]:
                if end not in cur_hour_end_count:
                    cur_hour_end_count[end] = {}

                for hour in cur_hour_start_to_end_count[start][end]:
                    if hour not in cur_hour_start_count[start]:
                        cur_hour_start_count[start][hour] = cur_hour_start_to_end_count[start][end][hour]

                    else:
                        cur_hour_start_count[start][hour] += cur_hour_start_to_end_count[start][end][hour]

                    if hour not in cur_hour_end_count[end]:
                        cur_hour_end_count[end][hour] = cur_hour_start_to_end_count[start][end][hour]

                    else:
                        cur_hour_end_count[end][hour] += cur_hour_start_to_end_count[start][end][hour]

        else:
            for end in cur_hour_start_to_end_count:
                for hour in cur_hour_start_to_end_count[start][end]:
                    if hour not in cur_hour_start_count[start]:
                        cur_hour_start_count[start][hour] = cur_hour_start_to_end_count[start][end][hour]

                    else:
                        cur_hour_start_count[start][hour] += cur_hour_start_to_end_count[start][end][hour]

                    if hour not in cur_hour_end_count[end]:
                        cur_hour_end_count[end][hour] = cur_hour_start_to_end_count[start][end][hour]

                    else:
                        cur_hour_end_count[end][hour] += cur_hour_start_to_end_count[start][end][hour]

    return cur_hour_start_count, cur_hour_end_count


def _get_start_or_end_count(start_to_end_count):
    print("_get_start_or_end_count")

    start_count = {}
    end_count = {}
    for start in start_to_end_count:
        if start not in start_count:
            start_count[start] = 0

        for end in start_to_end_count[start]:
            start_count[start] += start_to_end_count[start][end]

            if end not in end_count:
                end_count[end] = start_to_end_count[start][end]

            else:
                end_count[end] += start_to_end_count[start][end]

    return start_count, end_count


# 计算占比
def _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_count, start_to_end_count, cur_hour_start_count,
                                              cur_hour_end_count, fns):
    print("_create_cur_hour_start_to_end_ratio_table")

    start_count = {}
    end_count = {}
    for start in start_to_end_count:
        if start not in start_count:
            start_count[start] = 0

        for end in start_to_end_count[start]:
            start_count[start] += start_to_end_count[start][end]

            if end not in end_count:
                end_count[end] = start_to_end_count[start][end]

            else:
                end_count[end] += start_to_end_count[start][end]

    cur_hour_start_to_end_ratio = {}  # 历史次数
    cur_hour_start_to_end_overall_ratio = {}  # 起点到终点总次数
    cur_hour_start_to_end_start_ratio = {}  # 起点出发总次数
    cur_hour_start_to_end_cur_hour_start_ratio = {}  # 每小时起点出发总次数
    cur_hour_start_to_end_end_ratio = {}  # 终点到达总次数
    cur_hour_start_to_end_cur_hour_end_ratio = {}  # 每小时终点到达总次数

    row_count = 1048575

    for start in cur_hour_start_to_end_count:
        cur_hour_start_to_end_ratio[start] = {}
        cur_hour_start_to_end_overall_ratio[start] = {}
        cur_hour_start_to_end_start_ratio[start] = {}
        cur_hour_start_to_end_cur_hour_start_ratio[start] = {}
        cur_hour_start_to_end_end_ratio[start] = {}
        cur_hour_start_to_end_cur_hour_end_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_to_end_ratio[start][end] = {}
            cur_hour_start_to_end_overall_ratio[start][end] = {}
            cur_hour_start_to_end_start_ratio[start][end] = {}
            cur_hour_start_to_end_cur_hour_start_ratio[start][end] = {}
            cur_hour_start_to_end_end_ratio[start][end] = {}
            cur_hour_start_to_end_cur_hour_end_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_to_end_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / row_count

                cur_hour_start_to_end_overall_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_to_end_count[start][end]

                cur_hour_start_to_end_start_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_count[start]

                cur_hour_start_to_end_cur_hour_start_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / cur_hour_start_count[start][hour]

                cur_hour_start_to_end_end_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / end_count[end]

                cur_hour_start_to_end_cur_hour_end_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / cur_hour_end_count[end][hour]

    print(fns[0])
    with open('./data/temp/feature_table/' + fns[0], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fns[1])
    with open('./data/temp/feature_table/' + fns[1], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_overall_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fns[2])
    with open('./data/temp/feature_table/' + fns[2], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_start_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fns[3])
    with open('./data/temp/feature_table/' + fns[3], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_cur_hour_start_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fns[4])
    with open('./data/temp/feature_table/' + fns[4], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_end_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fns[5])
    with open('./data/temp/feature_table/' + fns[5], 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_cur_hour_end_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_12():
    print("render_feature_table_part_12")

    # node_neis = _get_node_neis()

    # _create_start_to_end_count_table()
    # _create_start_geofly_to_end_count_table(node_neis)
    # _create_start_to_end_geofly_count_table(node_neis)
    # _create_start_geofly_to_end_geofly_count_table(node_neis)

    # _create_cur_hour_start_to_end_count_table()
    # _create_cur_hour_start_geofly_to_end_count_table(node_neis)
    # _create_cur_hour_start_to_end_geofly_count_table(node_neis)
    # _create_cur_hour_start_geofly_to_end_geofly_count_table(node_neis)

    start_to_end_count = get_pickle('./data/temp/start_to_end_count')
    start_geofly_to_end_count = get_pickle('./data/temp/start_geofly_to_end_count')
    start_to_end_geofly_count = get_pickle('./data/temp/start_to_end_geofly_count')
    start_geofly_to_end_geofly_count = get_pickle('./data/temp/start_geofly_to_end_geofly_count')

    cur_hour_start_to_end_count = get_pickle('./data/temp/cur_hour_start_to_end_count')
    cur_hour_start_geofly_to_end_count = get_pickle('./data/temp/cur_hour_start_geofly_to_end_count')
    cur_hour_start_to_end_geofly_count = get_pickle('./data/temp/cur_hour_start_to_end_geofly_count')
    cur_hour_start_geofly_to_end_geofly_count = \
        get_pickle('./data/temp/cur_hour_start_geofly_to_end_geofly_count')

    cur_hour_start_count1, cur_hour_end_count1 = _get_cur_hour_start_or_end_count(cur_hour_start_to_end_count)
    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_count, start_to_end_count,
                                              cur_hour_start_count1, cur_hour_end_count1,
                                              ['cur_hour_start_to_end_ratio',
                                               'cur_hour_start_to_end_overall_ratio',
                                               'cur_hour_start_to_end_start_ratio',
                                               'cur_hour_start_to_end_cur_hour_start_ratio',
                                               'cur_hour_start_to_end_end_ratio',
                                               'cur_hour_start_to_end_cur_hour_end_ratio'])

    cur_hour_start_count2, cur_hour_end_count2 = _get_cur_hour_start_or_end_count(cur_hour_start_geofly_to_end_count)
    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_geofly_to_end_count, start_geofly_to_end_count,
                                              cur_hour_start_count2, cur_hour_end_count2,
                                              ['cur_hour_start_geofly_to_end_ratio',
                                               'cur_hour_start_geofly_to_end_overall_ratio',
                                               'cur_hour_start_geofly_to_end_start_geofly_ratio',
                                               'cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio',
                                               'cur_hour_start_geofly_to_end_end_ratio',
                                               'cur_hour_start_geofly_to_end_cur_hour_end_ratio'])

    cur_hour_start_count3, cur_hour_end_count3 = _get_cur_hour_start_or_end_count(cur_hour_start_to_end_geofly_count)
    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_geofly_count, start_to_end_geofly_count,
                                              cur_hour_start_count3, cur_hour_end_count3,
                                              ['cur_hour_start_to_end_geofly_ratio',
                                               'cur_hour_start_to_end_geofly_overall_ratio',
                                               'cur_hour_start_to_end_geofly_start_ratio',
                                               'cur_hour_start_to_end_geofly_cur_hour_start_ratio',
                                               'cur_hour_start_to_end_geofly_end_geofly_ratio',
                                               'cur_hour_start_to_end_geofly_cur_hour_end_geofly_ratio'])

    # cur_hour_start_count4, cur_hour_end_count4 = _get_cur_hour_start_or_end_count(cur_hour_start_geofly_to_end_geofly_count)
    # _create_cur_hour_start_to_end_ratio_table(cur_hour_start_geofly_to_end_geofly_count,
    #                                           start_geofly_to_end_geofly_count,
    #                                           cur_hour_start_count4, cur_hour_end_count4,
    #                                           ['cur_hour_start_geofly_to_end_geofly_ratio',
    #                                            'cur_hour_start_geofly_to_end_geofly_overall_ratio',
    #                                            'cur_hour_start_geofly_to_end_geofly_start_geofly_ratio',
    #                                            'cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio',
    #                                            'cur_hour_start_geofly_to_end_geofly_end_geofly_ratio',
    #                                            'cur_hour_start__geoflyto_end_geofly_cur_hour_end_geofly_ratio'])

    print("-----------------------------")
