# encoding: utf-8

"""
时间+单地点

"""

import csv
import pickle


# 起点到终点行程次数/起点总出发次数，原始值与漂移后的值
# ./data/temp/feature_table/start_to_end_start_out_ratio
# ./data/temp/feature_table/start_geofly_to_end_start_geofly_out_ratio
# ./data/temp/feature_table/start_to_end_geofly_start_out_ratio
# ./data/temp/feature_table/start_geofly_to_end_geofly_start_geofly_out_ratio
def _create_start_to_end_start_out_tables():
    def get_start_to_end_start_out_ratio(start_to_end_count_path, start_count_path):
        # 一个是起点到终点次数计算的csv的路径，一个是计算start出发了几次的csv路径，
        # 在起点飘逸的时候需要给start_count_path也是飘逸的

        node_start_count = {}  # 节点出发次数
        i = 0
        csv_reader = csv.reader(open(start_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            start = row[5]
            if start not in node_start_count:
                node_start_count[start] = 1
            else:
                node_start_count[start] += 1

        node_start_to_end_count = {}  # 起点到终点的次数

        i = 0
        csv_reader = csv.reader(open(start_to_end_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            start = row[5]
            end = row[6]

            if start not in node_start_to_end_count:
                node_start_to_end_count[start] = {}
                node_start_to_end_count[start][end] = 1
            else:
                if end not in node_start_to_end_count[start]:
                    node_start_to_end_count[start][end] = 1
                else:
                    node_start_to_end_count[start][end] += 1

        node_start_to_end_count_ratio = {}

        for start in node_start_to_end_count:
            node_start_to_end_count_ratio[start] = {}
            for end in node_start_to_end_count[start]:
                node_start_to_end_count_ratio[start][end] = node_start_to_end_count[start][end] / \
                                                            node_start_count[start]

        return node_start_to_end_count_ratio

    start_to_end_start_out_ratio = get_start_to_end_start_out_ratio('./data/train_hard.csv', \
                                                                    './data/train_hard.csv')
    start_geofly_to_end_start_geofly_out_ratio = \
        get_start_to_end_start_out_ratio('./data/train_start_geofly.csv', \
                                         './data/train_start_geofly.csv')

    start_to_end_geofly_start_out_ratio = \
        get_start_to_end_start_out_ratio('./data/train_end_geofly.csv', \
                                         './data/train_hard.csv')

    start_geofly_to_end_geofly_start_geofly_out_ratio = \
        get_start_to_end_start_out_ratio('./data/train_start_geofly_end_geofly.csv', \
                                         './data/train_start_geofly.csv')

    with open('./data/temp/feature_table/start_to_end_start_out_ratio', 'wb+') as f:
        pickle.dump(start_to_end_start_out_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_geofly_to_end_start_geofly_out_ratio', 'wb+') as f:
        pickle.dump(start_geofly_to_end_start_geofly_out_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_to_end_geofly_start_out_ratio', 'wb+') as f:
        pickle.dump(start_to_end_geofly_start_out_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_geofly_to_end_geofly_start_geofly_out_ratio', 'wb+') as f:
        pickle.dump(start_geofly_to_end_geofly_start_geofly_out_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_6():
    print("render_feature_table_part_6")

    _create_start_to_end_start_out_tables()

    print("-----------------------------")
