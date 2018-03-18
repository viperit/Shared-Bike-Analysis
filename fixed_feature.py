# encoding: utf-8

import csv


# 每个用户骑行次数表：
def _generate_user_count_table():
    print("_generate_user_count_table")
    i = 0
    csv_reader = csv.reader(open('./data/temp/train_hard.csv', encoding='utf-8'))

    user_count = {}

    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user = row[1]

        if user not in user_count:
            user_count[user] = 1
        else:
            user_count[user] += 1

    with open("./data/temp/user_count.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_count.items():
            writer.writerow([key, value])


# 用户在当前小时出发的次数／用户总出发次数: user_cur_hour_used_ratio
def _generate_user_cur_hour_used_ratio_table():
    print("_generate_user_cur_hour_used_ratio_table")
    # 读取用户出发总次数
    i = 0
    csv_reader = csv.reader(open('./data/temp/user_count.csv', encoding='utf-8'))
    user_count = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_count[row[0]] = int(row[1])

    # 得到比例
    i = 0
    csv_reader = csv.reader(open('./data/temp/train_hard.csv', encoding='utf-8'))
    user_cur_hour_used_count = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user = row[1]
        start = row[5]
        end = row[6]
        hour = row[7]
        isholiday = row[8]

        # 计算与isholiday无关，hour划分
        if user not in user_cur_hour_used_count:
            user_cur_hour_used_count[user] = {}
            user_cur_hour_used_count[user][hour] = 1
        else:
            if hour not in user_cur_hour_used_count[user]:
                user_cur_hour_used_count[user][hour] = 1
            else:
                user_cur_hour_used_count[user][hour] += 1

    user_cur_hour_used_ratio = {}
    for user in user_cur_hour_used_count:
        user_cur_hour_used_ratio[user] = {}
        for hour in user_cur_hour_used_count[user]:
            user_cur_hour_used_ratio[user][hour] = user_cur_hour_used_count[user][hour] / user_count[user]

    with open("./data/temp/preprocess/user_cur_hour_used_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_cur_hour_used_ratio.items():
            writer.writerow([key, value])


# 用户在当前时段出发的次数／用户总出发次数: user_cur_period_used_ratio
def _generate_user_cur_period_used_ratio_table():
    pass


# 用户当前订单时间与下次订单时间的差值: user_next_order_time_diff
def _generate_user_next_order_time_diff_table():
    print("_generate_user_next_order_time_diff_table")

    def get_user_order_info():
        i = 0
        user_row = {}
        csv_reader = csv.reader(open('./data/temp/preprocess/train_s_20.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            if row[1] not in user_row:
                user_row[row[1]] = []
                user_row[row[1]].append(row)
            else:
                user_row[row[1]].append(row)
        i = 0
        csv_reader = csv.reader(open('./data/temp/preprocess/test_b_20.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            
            if row[1] not in user_row:
                user_row[row[1]] = []
                user_row[row[1]].append(row)
            else:
                user_row[row[1]].append(row)

        for user in user_row:
            user_row[user].sort(key=lambda k: k[4], reverse=False)
        return user_row
    # # 得到用户订单的排序
    # user_order_info = get_user_order_info()
    #
    # with open("./data/temp/user_order_info.csv", 'w', newline='') as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(['key', 'value'])
    #     for key, value in user_order_info.items():
    #         writer.writerow([key, value])

    # 得到用户订单时间的排序
    user_order_info_time = get_user_order_info()

    with open("./data/temp/preprocess/user_order_info_time.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_order_info_time.items():
            writer.writerow([key, value])

# 用户平均骑行距离／全部平均骑行距离: user_avg_dis_overall_avg_dis_ratio
def _generate_user_avg_dis_overall_avg_dis_ratio_table():
    print("_generate_user_avg_dis_overall_avg_dis_ratio_table")

    def get_user_avg_dis_overall_avg_dis_ratio():

        i = 0
        csv_reader = csv.reader(open('./data/temp/train_hard.csv', encoding='utf-8'))

        total_dis = 0  # 累计行程的曼哈顿距离
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            total_dis += int(row[9])
        avg_dis = total_dis / (i - 1)

        i = 0

        user_dis_info = {}
        csv_reader = csv.reader(open('./data/temp/user_dis_info.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                continue
            user_dis_info[row[0]] = eval(row[1])

        user_avg_dis_overall_avg_dis_ratio = {}
        for user in user_dis_info:
            user_avg_dis_overall_avg_dis_ratio[user] = user_dis_info[user][2] / avg_dis

        return user_avg_dis_overall_avg_dis_ratio

    user_avg_dis_overall_avg_dis_ratio = get_user_avg_dis_overall_avg_dis_ratio()

    with open("./data/temp/preprocess/user_avg_dis_overall_avg_dis_ratio.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in user_avg_dis_overall_avg_dis_ratio.items():
            writer.writerow([key, value])


# 当前小时内全用户的平均骑行距离: overall_avg_dis_cur_hour
def _generate_overall_avg_dis_cur_hour_table():
    print("_generate_overall_avg_dis_cur_hour_table")

    def get_overall_avg_dis_cur_hour():
        i = 0
        all_user_avg_dis_hour = {}
        all_user_count = {}  # 计算每个小时用了几次
        csv_reader = csv.reader(open('./data/temp/train_hard.csv', encoding='utf-8'))

        total_dis = 0  # 累计行程的曼哈顿距离
        for row in csv_reader:
            i += 1
            if i == 1:
                continue

            hour = row[7]

            if hour not in all_user_avg_dis_hour:
                all_user_avg_dis_hour[hour] = 0
                all_user_avg_dis_hour[hour] += int(row[9])
                all_user_count[hour] = 1
            else:
                all_user_avg_dis_hour[hour] += int(row[9])
                all_user_count[hour] += 1

        overall_avg_dis_cur_hour = {}
        for hour in all_user_avg_dis_hour:
            overall_avg_dis_cur_hour[hour] = round(all_user_avg_dis_hour[hour] / all_user_count[hour])
        return overall_avg_dis_cur_hour

    overall_avg_dis_cur_hour = get_overall_avg_dis_cur_hour()
    with open("./data/temp/preprocess/overall_avg_dis_cur_hour.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['key', 'value'])
        for key, value in overall_avg_dis_cur_hour.items():
            writer.writerow([key, value])


# 当前时段内全用户的平均骑行距离: overall_avg_dis_cur_period
def _generate_overall_avg_dis_cur_period_table():
    pass


# 生成所有表格，对外接口
def render_fixed_feature():
    _generate_user_count_table()
    _generate_user_cur_hour_used_ratio_table()
    _generate_user_cur_period_used_ratio_table()
    _generate_user_next_order_time_diff_table()
    _generate_user_avg_dis_overall_avg_dis_ratio_table()
    _generate_overall_avg_dis_cur_hour_table()
    _generate_overall_avg_dis_cur_period_table()

