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


# 计算占比
def _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_count, start_to_end_count, fn1, fn2, fn3):
    print("_create_cur_hour_start_to_end_ratio_table")

    start_count = {}
    end_count = {}
    for start in start_to_end_count:
        if start not in start_count:
            start_count[start] = 1

        else:
            start_count[start] += 1

        for end in start_to_end_count[start]:
            if end not in end_count:
                end_count[end] = 1

            else:
                end_count[end] += 1

    cur_hour_start_to_end_overall_ratio = {}
    cur_hour_start_to_end_start_ratio = {}
    cur_hour_start_to_end_end_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_to_end_overall_ratio[start] = {}
        cur_hour_start_to_end_start_ratio[start] = {}
        cur_hour_start_to_end_end_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_to_end_overall_ratio[start][end] = {}
            cur_hour_start_to_end_start_ratio[start][end] = {}
            cur_hour_start_to_end_end_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_to_end_overall_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_to_end_count[start][end]

                cur_hour_start_to_end_start_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_count[start]

                cur_hour_start_to_end_end_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / end_count[end]

    print(fn1)
    with open('./data/temp/feature_table/' + fn1, 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_overall_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fn2)
    with open('./data/temp/feature_table/' + fn2, 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_start_ratio, f, pickle.HIGHEST_PROTOCOL)

    print(fn3)
    with open('./data/temp/feature_table/' + fn3, 'wb+') as f:
        pickle.dump(cur_hour_start_to_end_end_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_11():
    print("render_feature_table_part_11")

    node_neis = _get_node_neis()

    _create_start_to_end_count_table()
    _create_start_geofly_to_end_count_table(node_neis)
    _create_start_to_end_geofly_count_table(node_neis)
    _create_start_geofly_to_end_geofly_count_table(node_neis)

    _create_cur_hour_start_to_end_count_table()
    _create_cur_hour_start_geofly_to_end_count_table(node_neis)
    _create_cur_hour_start_to_end_geofly_count_table(node_neis)
    _create_cur_hour_start_geofly_to_end_geofly_count_table(node_neis)

    start_to_end_count = get_pickle('./data/temp/start_to_end_count')
    start_geofly_to_end_count = get_pickle('./data/temp/start_geofly_to_end_count')
    start_to_end_geofly_count = get_pickle('./data/temp/start_to_end_geofly_count')
    start_geofly_to_end_geofly_count = get_pickle('./data/temp/start_geofly_to_end_geofly_count')

    cur_hour_start_to_end_count = get_pickle('./data/temp/cur_hour_start_to_end_count')
    cur_hour_start_geofly_to_end_count = get_pickle('./data/temp/cur_hour_start_geofly_to_end_count')
    cur_hour_start_to_end_geofly_count = get_pickle('./data/temp/cur_hour_start_to_end_geofly_count')
    cur_hour_start_geofly_to_end_geofly_count = \
        get_pickle('./data/temp/cur_hour_start_geofly_to_end_geofly_count')

    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_count, start_to_end_count,
                                              'cur_hour_start_to_end_overall_ratio.csv',
                                              'cur_hour_start_to_end_start_ratio.csv',
                                              'cur_hour_start_to_end_end_ratio.csv')

    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_geofly_to_end_count, start_geofly_to_end_count,
                                              'cur_hour_start_geofly_to_end_overall_ratio.csv',
                                              'cur_hour_start_geofly_to_end_start_ratio.csv',
                                              'cur_hour_start_geofly_to_end_end_ratio.csv')

    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_to_end_geofly_count, start_to_end_geofly_count,
                                              'cur_hour_start_to_end_geofly_overall_ratio.csv',
                                              'cur_hour_start_to_end_geofly_start_ratio.csv',
                                              'cur_hour_start_to_end_geofly_end_ratio.csv')

    _create_cur_hour_start_to_end_ratio_table(cur_hour_start_geofly_to_end_geofly_count,
                                              start_geofly_to_end_geofly_count,
                                              'cur_hour_start_geofly_to_end_geofly_overall_ratio.csv',
                                              'cur_hour_start_geofly_to_end_geofly_start_ratio.csv',
                                              'cur_hour_start_geofly_to_end_geofly_end_ratio.csv')

    print("-----------------------------")
