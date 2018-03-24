# encoding: utf-8

"""
全用户+单地点

"""

import csv
import pickle

# 该用户该小时去该终点／用户总出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_end_ratio
# 该用户该小时去该终点／用户该小时出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_end_cur_hour_ratio
# 该用户该小时去该终点（geofly）／用户总出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_end_geofly_ratio
# 该用户该小时去该终点（geofly）／用户该小时出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_end_geofly_cur_hour_ratio
def _create_user_cur_hour_loc_as_end_ratio_tables():
    print("_create_user_cur_hour_loc_as_end_ratio_tables")

    def get_to_end_ratio(to_end_count_path, user_count_path='./data/train_hard.csv'):
        # 一个是终点到达次数计算的csv的路径，一个是计算用户使用了几次的path
        # 在终点飘逸的时候，user_count_path用户使用的次数不能是飘逸的

        user_count = {}  # 用户出发次数==用户行程次数
        user_hour_count = {}  # 用户每小时出发次数
        i = 0
        csv_reader = csv.reader(open(user_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            hour = row[7]

            if user not in user_count:
                user_count[user] = 1
            else:
                user_count[user] += 1

            if user not in user_hour_count:
                user_hour_count[user] = {}
                user_hour_count[user][hour] = 1
            else:
                if hour not in user_hour_count[user]:
                    user_hour_count[user][hour] = 1
                else:
                    user_hour_count[user][hour] += 1

        user_cur_hour_loc_as_end = {}  # 该用户该小时去该终点次数

        i = 0
        csv_reader = csv.reader(open(to_end_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            end = row[6]
            hour = row[7]

            if user not in user_cur_hour_loc_as_end:
                user_cur_hour_loc_as_end[user] = {}
                user_cur_hour_loc_as_end[user][hour] = {}
                user_cur_hour_loc_as_end[user][hour][end] = 1
            else:
                if hour not in user_cur_hour_loc_as_end[user]:
                    user_cur_hour_loc_as_end[user][hour] = {}
                    user_cur_hour_loc_as_end[user][hour][end] = 1
                else:
                    if end not in user_cur_hour_loc_as_end[user][hour]:
                        user_cur_hour_loc_as_end[user][hour][end] = 1
                    else:
                        user_cur_hour_loc_as_end[user][hour][end] += 1

        user_cur_hour_loc_as_end_ratio = {}  # 该用户该小时去该终点／用户总出发次数

        user_cur_hour_loc_as_end_cur_hour_ratio = {}  # 该用户该小时去该终点／用户该小时出发次数

        for user in user_cur_hour_loc_as_end:
            user_cur_hour_loc_as_end_ratio[user] = {}
            user_cur_hour_loc_as_end_cur_hour_ratio[user] = {}

            for hour in user_cur_hour_loc_as_end[user]:
                user_cur_hour_loc_as_end_ratio[user][hour] = {}
                user_cur_hour_loc_as_end_cur_hour_ratio[user][hour] = {}

                for end in user_cur_hour_loc_as_end[user][hour]:
                    user_cur_hour_loc_as_end_ratio[user][hour][end] = \
                        user_cur_hour_loc_as_end[user][hour][end] / user_count[user]
                    user_cur_hour_loc_as_end_cur_hour_ratio[user][hour][end] = \
                        user_cur_hour_loc_as_end[user][hour][end] / user_hour_count[user][hour]

        return user_cur_hour_loc_as_end_ratio, user_cur_hour_loc_as_end_cur_hour_ratio

    user_cur_hour_loc_as_end_ratio, user_cur_hour_loc_as_end_cur_hour_ratio = get_to_end_ratio('./data/train_hard.csv')

    user_cur_hour_loc_as_end_geofly_ratio, user_cur_hour_loc_as_end_geofly_cur_hour_ratio \
        = get_to_end_ratio('./data/train_end_geofly.csv')

    with open('./data/temp/feature_table/user_cur_hour_loc_as_end_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_end_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_end_cur_hour_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_end_cur_hour_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_end_geofly_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_end_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_end_geofly_cur_hour_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_end_geofly_cur_hour_ratio, f, pickle.HIGHEST_PROTOCOL)


# 该用户该小时从该终点出发／用户总出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_start_ratio
# 该用户该小时从该终点出发／用户该小时出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_start_cur_hour_ratio
# 该用户该小时从该终点（geofly）出发／用户总出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_start_geofly_ratio
# 该用户该小时从该终点（geofly）出发／用户该小时出发次数
# ./data/temp/feature_table/user_cur_hour_loc_as_start_geofly_cur_hour_ratio
def _create_user_cur_hour_loc_as_start_ratio_tables():
    print("_create_user_cur_hour_loc_as_start_ratio_tables")

    def get_from_start_ratio(from_start_count_path, user_count_path='./data/train_hard.csv'):
        # 一个是起点出发计算的csv的路径，一个是计算用户使用了几次的path
        # 在终点飘逸的时候，user_count_path用户使用的次数不能是飘逸的

        user_count = {}  # 用户出发次数==用户行程次数
        user_hour_count = {}  # 用户每小时出发次数
        i = 0
        csv_reader = csv.reader(open(user_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user = row[1]
            hour = row[7]

            if user not in user_count:
                user_count[user] = 1
            else:
                user_count[user] += 1

            if user not in user_hour_count:
                user_hour_count[user] = {}
                user_hour_count[user][hour] = 1
            else:
                if hour not in user_hour_count[user]:
                    user_hour_count[user][hour] = 1
                else:
                    user_hour_count[user][hour] += 1

        user_cur_hour_loc_as_start = {}  # 该用户该小时从该起点出发次数

        i = 0
        csv_reader = csv.reader(open(from_start_count_path, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            user = row[1]
            start = row[5]
            hour = row[7]

            if user not in user_cur_hour_loc_as_start:
                user_cur_hour_loc_as_start[user] = {}
                user_cur_hour_loc_as_start[user][hour] = {}
                user_cur_hour_loc_as_start[user][hour][start] = 1
            else:
                if hour not in user_cur_hour_loc_as_start[user]:
                    user_cur_hour_loc_as_start[user][hour] = {}
                    user_cur_hour_loc_as_start[user][hour][start] = 1
                else:
                    if start not in user_cur_hour_loc_as_start[user][hour]:
                        user_cur_hour_loc_as_start[user][hour][start] = 1
                    else:
                        user_cur_hour_loc_as_start[user][hour][start] += 1

        user_cur_hour_loc_as_start_ratio = {}  # 该用户该小时去该终点／用户总出发次数

        user_cur_hour_loc_as_start_cur_hour_ratio = {}  # 该用户该小时去该终点／用户该小时出发次数

        for user in user_cur_hour_loc_as_start:
            user_cur_hour_loc_as_start_ratio[user] = {}
            user_cur_hour_loc_as_start_cur_hour_ratio[user] = {}

            for hour in user_cur_hour_loc_as_start[user]:
                user_cur_hour_loc_as_start_ratio[user][hour] = {}
                user_cur_hour_loc_as_start_cur_hour_ratio[user][hour] = {}

                for end in user_cur_hour_loc_as_start[user][hour]:
                    user_cur_hour_loc_as_start_ratio[user][hour][end] = \
                        user_cur_hour_loc_as_start[user][hour][end] / user_count[user]
                    user_cur_hour_loc_as_start_cur_hour_ratio[user][hour][end] = \
                        user_cur_hour_loc_as_start[user][hour][end] / user_hour_count[user][hour]

        return user_cur_hour_loc_as_start_ratio, user_cur_hour_loc_as_start_cur_hour_ratio

    user_cur_hour_loc_as_start_ratio, user_cur_hour_loc_as_start_cur_hour_ratio = \
        get_from_start_ratio('./data/train_hard.csv')

    user_cur_hour_loc_as_start_geofly_ratio, user_cur_hour_loc_as_start_geofly_cur_hour_ratio \
        = get_from_start_ratio('./data/train_start_geofly.csv')

    with open('./data/temp/feature_table/user_cur_hour_loc_as_start_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_start_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_start_cur_hour_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_start_cur_hour_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_start_geofly_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_start_geofly_ratio, f, pickle.HIGHEST_PROTOCOL)

    with open('./data/temp/feature_table/user_cur_hour_loc_as_start_geofly_cur_hour_ratio', 'wb+') as f:
        pickle.dump(user_cur_hour_loc_as_start_geofly_cur_hour_ratio, f, pickle.HIGHEST_PROTOCOL)


def render_feature_table_part_8():
    print("render_feature_table_part_8")

    _create_user_cur_hour_loc_as_start_ratio_tables()
    _create_user_cur_hour_loc_as_end_ratio_tables()

    print("-----------------------------")
