# encoding: utf-8

"""
全用户+单地点

"""

import csv
import pickle


# ./data/temp/feature_table/start_to_end_end_in_ratio
# ./data/temp/feature_table/start_geofly_to_end_end_in_ratio
# ./data/temp/feature_table/start_to_end_geofly_end_geofly_in_ratio
# ./data/temp/feature_table/start_geofly_to_end_geofly_end_in_ratio
def _create_start_to_end_end_in_ratio_tables():
    def get_start_to_end_end_in_ratio(start_to_end_count_path, end_count_path):
        # 一个是起点到终点次数计算的csv的路径，一个是计算end 到达了几次的csv路径，
        # 在起点飘逸的时候需要给end_count_path也是飘逸的

        node_end_count = {}  # 节点到达次数
        i = 0
        csv_reader = csv.reader(open(end_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            end = row[6]
            if end not in node_end_count:
                node_end_count[end] = 1
            else:
                node_end_count[end] += 1

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
                                                            node_end_count[end]

        return node_start_to_end_count_ratio

    start_to_end_end_in_ratio = get_start_to_end_end_in_ratio('./data/train_hard.csv', \
                                                     './data/train_hard.csv')

    start_geofly_to_end_end_in_ratio = get_start_to_end_end_in_ratio('./data/train_start_geofly.csv', \
                                                            './data/train_hard.csv')

    start_to_end_geofly_end_geofly_in_ratio = get_start_to_end_end_in_ratio('./data/train_end_geofly.csv', \
                                                                   './data/train_end_geofly.csv')

    start_geofly_to_end_geofly_end_in_ratio = get_start_to_end_end_in_ratio('./data/train_end_geofly.csv', \
                                                                   './data/train_end_geofly.csv')

    with open('./data/temp/feature_table/start_to_end_end_in_ratio', 'wb+') as f:
        pickle.dump(start_to_end_end_in_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_geofly_to_end_end_in_ratio', 'wb+') as f:
        pickle.dump(start_geofly_to_end_end_in_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_to_end_geofly_end_geofly_in_ratio', 'wb+') as f:
        pickle.dump(start_to_end_geofly_end_geofly_in_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/start_geofly_to_end_geofly_end_in_ratio', 'wb+') as f:
        pickle.dump(start_geofly_to_end_geofly_end_in_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_7():
    print("render_feature_table_part_7")

    print("-----------------------------")
