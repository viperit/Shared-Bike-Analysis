# encoding: utf-8

"""
单用户+双地点
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


# 创建用户从此起点到此终点的次数占用户历史次数的比重表
# ./data/temp/feature_table/user_start_to_end_ratio.csv
def _create_user_start_to_end_ratio_table(user_count):
    print("_create_user_start_to_end_ratio_table")

    def get_user_start_to_end():
        user_start_to_end = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            start = row[5]
            end = row[6]

            if user not in user_start_to_end:  # 如果user not exist
                user_start_to_end[user] = {}
                user_start_to_end[user][start] = {}
                user_start_to_end[user][start][end] = 1

            else:
                if start not in user_start_to_end[user]:  # 如果start没有记录过
                    user_start_to_end[user][start] = {}
                    user_start_to_end[user][start][end] = 1
                else:
                    if end not in user_start_to_end[user][start]:  # 如果end没有记录过
                        user_start_to_end[user][start][end] = 1
                    else:
                        user_start_to_end[user][start][end] += 1

        return user_start_to_end

    def get_user_start_to_end_ratio(user_count):
        user_start_to_end = get_user_start_to_end()
        user_start_to_end_ratio = {}
        for user in user_start_to_end:
            user_start_to_end_ratio[user] = {}

            for start in user_start_to_end[user]:
                user_start_to_end_ratio[user][start] = {}
                for end in user_start_to_end[user][start]:
                    user_start_to_end_ratio[user][start][end] = user_start_to_end[user][start][end] / user_count[user]
        return user_start_to_end_ratio

    user_start_to_end_ratio = get_user_start_to_end_ratio(user_count)

    with open("./data/temp/feature_table/user_start_to_end_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_start_to_end_ratio.items():
            writer.writerow([key, value])


# 创建用户从此起点（扩大9倍）到此终点的次数占用户历史次数的比重表
# ./data/temp/feature_table/user_start_geofly_to_end_ratio.csv
def _create_user_start_geofly_to_end_ratio_table(node_neis, user_count):
    print("_create_user_start_geofly_to_end_ratio_table")

    def get_user_start_geofly_to_end(node_neis):
        user_start_geofly_to_end = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            starts = node_neis[row[5]]
            end = row[6]

            if user not in user_start_geofly_to_end:  # 如果user不存在
                user_start_geofly_to_end[user] = {}

                for start in starts:
                    user_start_geofly_to_end[user][start] = {}
                    user_start_geofly_to_end[user][start][end] = 1

            else:
                for start in starts:
                    if start not in user_start_geofly_to_end[user]:
                        user_start_geofly_to_end[user][start] = {}
                        user_start_geofly_to_end[user][start][end] = 1
                    else:
                        if end not in user_start_geofly_to_end[user][start]:
                            user_start_geofly_to_end[user][start][end] = 1
                        else:
                            user_start_geofly_to_end[user][start][end] += 1

        return user_start_geofly_to_end

    def get_user_start_geofly_to_end_ratio(user_count):

        user_start_geofly_to_end = get_user_start_geofly_to_end(node_neis)

        user_start_geofly_to_end_ratio = {}

        for user in user_start_geofly_to_end:

            user_start_geofly_to_end_ratio[user] = {}

            for start in user_start_geofly_to_end[user]:

                user_start_geofly_to_end_ratio[user][start] = {}

                for end in user_start_geofly_to_end[user][start]:
                    user_start_geofly_to_end_ratio[user][start][end] = user_start_geofly_to_end[user][start][end] / \
                                                                       user_count[user]

        return user_start_geofly_to_end_ratio

    user_start_geofly_to_end_ratio = get_user_start_geofly_to_end_ratio(user_count)

    with open("./data/temp/feature_table/user_start_geofly_to_end_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_start_geofly_to_end_ratio.items():
            writer.writerow([key, value])


# 创建用户从此起点到此终点（扩大9倍）的次数占用户历史次数的比重表
# ./data/temp/feature_table/user_start_to_end_geofly_ratio.csv
def _create_user_start_to_end_geofly_ratio_table(node_neis, user_count):
    print("_create_user_start_to_end_geofly_ratio_table")

    def get_user_start_to_end_geofly(node_neis):
        user_start_to_end_geofly = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            start = row[5]
            ends = node_neis[row[6]]

            if user not in user_start_to_end_geofly:
                user_start_to_end_geofly[user] = {}

                user_start_to_end_geofly[user][start] = {}
                for end in ends:
                    user_start_to_end_geofly[user][start][end] = 1

            else:
                if start not in user_start_to_end_geofly[user]:
                    user_start_to_end_geofly[user][start] = {}
                    for end in ends:
                        user_start_to_end_geofly[user][start][end] = 1

                else:
                    for end in ends:
                        if end not in user_start_to_end_geofly[user][start]:
                            user_start_to_end_geofly[user][start][end] = 1
                        else:
                            user_start_to_end_geofly[user][start][end] += 1

        return user_start_to_end_geofly

    def get_user_start_to_end_geofly_ratio(user_count):

        user_start_to_end_geofly = get_user_start_to_end_geofly(node_neis)

        user_start_to_end_geofly_ratio = {}

        for user in user_start_to_end_geofly:

            user_start_to_end_geofly_ratio[user] = {}

            for start in user_start_to_end_geofly[user]:

                user_start_to_end_geofly_ratio[user][start] = {}

                for end in user_start_to_end_geofly[user][start]:
                    user_start_to_end_geofly_ratio[user][start][end] = user_start_to_end_geofly[user][start][end] / \
                                                                       user_count[user]

        return user_start_to_end_geofly_ratio

    user_start_to_end_geofly_ratio = get_user_start_to_end_geofly_ratio(user_count)

    with open("./data/temp/feature_table/user_start_to_end_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_start_to_end_geofly_ratio.items():
            writer.writerow([key, value])


# 用户从此起点（扩大9倍）到此终点（扩大9倍）的次数占用户历史次数的比重
# ./data/temp/feature_table/user_start_geofly_to_end_geofly_ratio.csv
def _create_user_start_geofly_to_end_geofly_ratio_table(node_neis, user_count):
    print("_create_user_start_geofly_to_end_geofly_ratio_table")

    def get_user_start_geofly_to_end_geofly(node_neis):
        user_start_geofly_to_end_geofly = {}
        i = 0
        csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            starts = node_neis[row[5]]
            ends = node_neis[row[6]]

            if user not in user_start_geofly_to_end_geofly:  # user not exist
                user_start_geofly_to_end_geofly[user] = {}

                for start in starts:
                    user_start_geofly_to_end_geofly[user][start] = {}
                    for end in ends:
                        user_start_geofly_to_end_geofly[user][start][end] = 1

            else:
                for start in starts:
                    if start not in user_start_geofly_to_end_geofly[user]:  # 如果该start不在，end肯定都不在
                        user_start_geofly_to_end_geofly[user][start] = {}
                        for end in ends:
                            user_start_geofly_to_end_geofly[user][start][end] = 1

                    else:
                        for end in ends:
                            if end not in user_start_geofly_to_end_geofly[user][start]:
                                user_start_geofly_to_end_geofly[user][start][end] = 1
                            else:
                                user_start_geofly_to_end_geofly[user][start][end] += 1

        return user_start_geofly_to_end_geofly

    def get_user_start_geofly_to_end_geofly_ratio(user_count):

        user_start_geofly_to_end_geofly = get_user_start_geofly_to_end_geofly(node_neis)

        user_start_geofly_to_end_geofly_ratio = {}

        for user in user_start_geofly_to_end_geofly:

            user_start_geofly_to_end_geofly_ratio[user] = {}

            for start in user_start_geofly_to_end_geofly[user]:

                user_start_geofly_to_end_geofly_ratio[user][start] = {}

                for end in user_start_geofly_to_end_geofly[user][start]:
                    user_start_geofly_to_end_geofly_ratio[user][start][end] = \
                        user_start_geofly_to_end_geofly[user][start][end] / user_count[user]

        return user_start_geofly_to_end_geofly_ratio

    user_start_geofly_to_end_geofly_ratio = get_user_start_geofly_to_end_geofly_ratio(user_count)

    with open("./data/temp/feature_table/user_start_geofly_to_end_geofly_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_start_geofly_to_end_geofly_ratio.items():
            writer.writerow([key, value])


def render_feature_table_part_3():
    print("render_feature_table_part_3")
    node_neis = _get_node_neis()
    user_count = _get_user_count()

    _create_user_start_to_end_ratio_table(user_count)
    _create_user_start_geofly_to_end_ratio_table(node_neis, user_count)
    _create_user_start_to_end_geofly_ratio_table(node_neis, user_count)
    _create_user_start_geofly_to_end_geofly_ratio_table(node_neis, user_count)

    print("-----------------------------")
