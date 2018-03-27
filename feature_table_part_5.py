# encoding: utf-8

"""
全用户+单地点

"""

import csv
import pickle


# ./data/temp/feature_table/num_user_to_ratio
# ./data/temp/feature_table/num_user_to_geofly_ratio
def _create_num_user_to_ratio_tables():
    print("_create_num_user_to_ratio_tables")

    def get_node_use_as_end_rate(path):

        i = 0
        user_count = {}
        csv_reader = csv.reader(open('./data/temp/user_count.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user_count[row[0]] = eval(row[1])

        end_node_user_dic = {}  # 记录那些用户使用了终点
        user_end_dic = {}

        i = 0
        csv_reader = csv.reader(open(path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            end = row[6]

            # 看每个终点用了几次
            if user not in user_end_dic:
                user_end_dic[user] = {}
                user_end_dic[user][end] = 1
            else:
                if end not in user_end_dic[user]:
                    user_end_dic[user][end] = 1
                else:
                    user_end_dic[user][end] += 1

            # 记录那些用户在那个终点到达过
            if end not in end_node_user_dic:
                end_node_user_dic[end] = set()
                end_node_user_dic[end].add(user)
            else:
                end_node_user_dic[end].add(user)

        node_use_as_end_rate = {}

        for node in end_node_user_dic:
            total_to = 0
            total_used = 0
            for user in end_node_user_dic[node]:
                total_to += user_end_dic[user][node]
                total_used += user_count[user]
            if total_used != 0:
                node_use_as_end_rate[node] = total_to / total_used
            else:
                node_use_as_end_rate[node] = 0

        return node_use_as_end_rate

    num_user_to_ratio = get_node_use_as_end_rate('./data/train_hard.csv')
    num_user_to_geofly_ratio = get_node_use_as_end_rate('./data/train_end_geofly.csv')

    with open('./data/temp/feature_table/num_user_to_ratio', 'wb+') as f:
        pickle.dump(num_user_to_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/num_user_to_geofly_ratio', 'wb+') as f:
        pickle.dump(num_user_to_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


# ./data/temp/feature_table/num_user_from_ratio
# ./data/temp/feature_table/num_user_from_geofly_ratio
def _create_num_user_from_ratio_tables():
    print("_create_num_user_from_ratio_tables")

    def get_node_use_as_start_rate(path):

        i = 0
        user_count = {}
        csv_reader = csv.reader(open('./data/temp/user_count.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user_count[row[0]] = eval(row[1])

        start_node_user_dic = {}  # 记录那些用户从点出发
        user_start_dic = {}

        i = 0
        csv_reader = csv.reader(open(path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            start = row[5]

            # 看每个起点用了几次
            if user not in user_start_dic:
                user_start_dic[user] = {}
                user_start_dic[user][start] = 1
            else:
                if start not in user_start_dic[user]:
                    user_start_dic[user][start] = 1
                else:
                    user_start_dic[user][start] += 1

            # 记录那些用户在那个终点到达过
            if start not in start_node_user_dic:
                start_node_user_dic[start] = set()
                start_node_user_dic[start].add(user)
            else:
                start_node_user_dic[start].add(user)

        node_use_as_start_rate = {}

        for node in start_node_user_dic:
            total_from = 0
            total_used = 0
            for user in start_node_user_dic[node]:
                total_from += user_start_dic[user][node]
                total_used += user_count[user]
            if total_used != 0:
                node_use_as_start_rate[node] = total_from / total_used
            else:
                node_use_as_start_rate[node] = 0

        return node_use_as_start_rate

    num_user_from_ratio = get_node_use_as_start_rate('./data/train_hard.csv')
    num_user_from_geofly_ratio = get_node_use_as_start_rate('./data/train_start_geofly.csv')

    with open('./data/temp/feature_table/num_user_from_ratio', 'wb+') as f:
        pickle.dump(num_user_from_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/num_user_from_geofly_ratio', 'wb+') as f:
        pickle.dump(num_user_from_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_5():
    print("render_feature_table_part_5")

    _create_num_user_to_ratio_tables()
    _create_num_user_from_ratio_tables()

    print("-----------------------------")
