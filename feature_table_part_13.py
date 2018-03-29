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


# 计算起点终点都geofly的占比
def _create_cur_hour_start_geofly_to_end_geofly_ratio_table(cur_hour_start_to_end_count):
    print("_create_cur_hour_start_geofly_to_end_geofly_ratio_table")

    cur_hour_start_geofly_to_end_geofly_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_geofly_to_end_geofly_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_geofly_to_end_geofly_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_geofly_to_end_geofly_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / 1048575

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


def _create_cur_hour_start_geofly_to_end_geofly_overall_ratio_table(cur_hour_start_to_end_count, start_to_end_count):
    print("_create_cur_hour_start_geofly_to_end_geofly_overall_ratio_table")

    cur_hour_start_geofly_to_end_geofly_overall_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_geofly_to_end_geofly_overall_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_geofly_to_end_geofly_overall_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_geofly_to_end_geofly_overall_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_to_end_count[start][end]

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_overall_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_overall_ratio, f, pickle.HIGHEST_PROTOCOL)


def _create_cur_hour_start_geofly_to_end_geofly_start_or_end_ratio_tables(cur_hour_start_to_end_count, start_to_end_count):
    print("_create_cur_hour_start_geofly_to_end_geofly_start_or_end_ratio_tables")
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

    cur_hour_start_geofly_to_end_geofly_start_geofly_ratio = {}
    cur_hour_start_geofly_to_end_geofly_end_geofly_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_geofly_to_end_geofly_start_geofly_ratio[start] = {}
        cur_hour_start_geofly_to_end_geofly_end_geofly_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_geofly_to_end_geofly_start_geofly_ratio[start][end] = {}
            cur_hour_start_geofly_to_end_geofly_end_geofly_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_geofly_to_end_geofly_start_geofly_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / start_count[start]

                cur_hour_start_geofly_to_end_geofly_end_geofly_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / end_count[end]

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_start_geofly_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_start_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_end_geofly_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_end_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


def _create_cur_hour_start_geofly_to_end_geofly_cur_hour_start_ratio_tables(cur_hour_start_to_end_count,
                                                                            cur_hour_start_count):
    print("_create_cur_hour_start_geofly_to_end_geofly_cur_hour_start_ratio_tables")

    cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / cur_hour_start_count[start][hour]

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


def _create_cur_hour_start_geofly_to_end_geofly_cur_hour_end_ratio_tables(cur_hour_start_to_end_count,
                                                                          cur_hour_end_count):
    print("_create_cur_hour_start_geofly_to_end_geofly_cur_hour_end_ratio_tables")

    cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio = {}

    for start in cur_hour_start_to_end_count:
        cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio[start] = {}

        for end in cur_hour_start_to_end_count[start]:
            cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio[start][end] = {}

            for hour in cur_hour_start_to_end_count[start][end]:
                cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio[start][end][hour] = \
                    cur_hour_start_to_end_count[start][end][hour] / cur_hour_end_count[end][hour]

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio', 'wb+') as f:
        pickle.dump(cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_13():
    print("render_feature_table_part_13")

    # node_neis = _get_node_neis()

    # _create_start_to_end_count_table()
    # _create_start_geofly_to_end_count_table(node_neis)
    # _create_start_to_end_geofly_count_table(node_neis)
    # _create_start_geofly_to_end_geofly_count_table(node_neis)

    # _create_cur_hour_start_to_end_count_table()
    # _create_cur_hour_start_geofly_to_end_count_table(node_neis)
    # _create_cur_hour_start_to_end_geofly_count_table(node_neis)
    # _create_cur_hour_start_geofly_to_end_geofly_count_table(node_neis)

    start_geofly_to_end_geofly_count = get_pickle('./data/temp/start_geofly_to_end_geofly_count')

    cur_hour_start_geofly_to_end_geofly_count = \
        get_pickle('./data/temp/cur_hour_start_geofly_to_end_geofly_count')

    cur_hour_start_count, cur_hour_end_count = _get_cur_hour_start_or_end_count(cur_hour_start_geofly_to_end_geofly_count)

    # _create_cur_hour_start_geofly_to_end_geofly_ratio_table(cur_hour_start_geofly_to_end_geofly_count)

    # _create_cur_hour_start_geofly_to_end_geofly_overall_ratio_table(cur_hour_start_geofly_to_end_geofly_count, start_geofly_to_end_geofly_count)

    # _create_cur_hour_start_geofly_to_end_geofly_start_or_end_ratio_tables(cur_hour_start_geofly_to_end_geofly_count,
    #                                                                       start_geofly_to_end_geofly_count)

    # _create_cur_hour_start_geofly_to_end_geofly_cur_hour_start_ratio_tables(cur_hour_start_geofly_to_end_geofly_count,
    #                                                                         cur_hour_start_count)

    _create_cur_hour_start_geofly_to_end_geofly_cur_hour_end_ratio_tables(cur_hour_start_geofly_to_end_geofly_count,
                                                                          cur_hour_end_count)

    print("-----------------------------")
