# encoding: utf-8

import csv
import function


# 区分训练集和测试集
def read_and_split_train():
    train_s_20 = []
    test_b_20 = []
    i = 0
    csv_reader = csv.reader(open('./data/train.csv', encoding='utf-8'))
    for row in csv_reader:
        i += 1
        if i == 1:
            train_s_20.append(row)
            test_b_20.append(row)
            continue

        if row[4] < "2017-05-20 00:00:00":
            train_s_20.append(row)
        else:
            test_b_20.append(row)

    with open("./data/temp/preprocess/train_s_20.csv", 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in train_s_20:
            writer.writerow(row)
    with open("./data/temp/preprocess/test_b_20.csv", 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in test_b_20:
            writer.writerow(row)


def read_feature_talbe():
    # read user_dis_info
    i = 0
    csv_reader = csv.reader(open('./data/temp/user_dis_info.csv', encoding='utf-8'))
    user_dis_info = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_dis_info[row[0]] = eval(row[1])

    # read user_dis_info
    i = 0
    csv_reader = csv.reader(open('./data/temp/preprocess/user_cur_hour_used_ratio.csv', encoding='utf-8'))
    user_cur_hour_used_ratio = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_cur_hour_used_ratio[row[0]] = eval(row[1])

    # read user_order_info_time
    i = 0
    csv_reader = csv.reader(open('./data/temp/preprocess/user_order_info_time.csv', encoding='utf-8'))
    user_order_info_time = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_order_info_time[row[0]] = eval(row[1])

    # read user_avg_dis_overall_avg_dis_ratio
    i = 0
    csv_reader = csv.reader(open('./data/temp/preprocess/user_avg_dis_overall_avg_dis_ratio.csv', encoding='utf-8'))
    user_avg_dis_overall_avg_dis_ratio = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        user_avg_dis_overall_avg_dis_ratio[row[0]] = eval(row[1])

    # read overall_avg_dis_cur_hour
    i = 0
    csv_reader = csv.reader(open('./data/temp/preprocess/overall_avg_dis_cur_hour.csv', encoding='utf-8'))
    overall_avg_dis_cur_hour = {}
    for row in csv_reader:
        i += 1
        if i == 1:
            continue
        overall_avg_dis_cur_hour[row[0]] = eval(row[1])

    return user_dis_info, user_cur_hour_used_ratio, user_order_info_time, \
           user_avg_dis_overall_avg_dis_ratio, overall_avg_dis_cur_hour


def create_preprocessed_train_and_test():
    user_dis_info, user_cur_hour_used_ratio, user_order_info_time, \
    user_avg_dis_overall_avg_dis_ratio, overall_avg_dis_cur_hour = read_feature_talbe()

    i = 0
    with open("./data/train_hard.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        csv_reader = csv.reader(open('./data/temp/preprocess/train_s_20.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('hour')
                row.append('isHoliday')
                row.append('start_to_end_man_dis')
                row.append('user_max_man_dis')
                row.append('user_min_man_dis')
                row.append('user_mean_man_dis')
                row.append('user_mode_man_dis')

                row.append('user_cur_hour_used_ratio')
                row.append('user_next_order_time_diff')
                row.append('user_avg_dis_overall_avg_dis_ratio')
                row.append('overall_avg_dis_cur_hour')
                writer.writerow(row)
                continue
            user = row[1]
            start = row[5]
            end = row[6]
            time = row[4]

            hour = time[time.find(' ') + 1:time.find(' ') + 3]
            day = time[8:10]

            # 当前小时和节假日信息
            row.append(hour)
            if day == '13' or day == '14' or day == '20' or day == '21':
                row.append(1)
            else:
                row.append(0)
            ###

            # 加入曼哈顿距离
            row.append(function.getManhattan(start, end))
            ###

            # 加入用户骑行信息
            if user in user_dis_info:
                row.append(user_dis_info[user][0])
                row.append(user_dis_info[user][1])
                row.append(user_dis_info[user][2])
                if user_dis_info[user][3] != -1:
                    row.append(user_dis_info[user][3])
                else:
                    row.append('')
            else:
                row.append('')
                row.append('')
                row.append('')
                row.append('')

            # 用户当前小时出发比例
            if user in user_cur_hour_used_ratio:
                if hour in user_cur_hour_used_ratio[user]:
                    row.append(user_cur_hour_used_ratio[user][hour])
                else:  # 如果没有当前小时的记录
                    row.append('')
            else:
                row.append('')
            ###

            # 计算 用户当前订单时间与下次订单时间的差值
            cur_day = int(time[8:10])
            cur_hour = int(hour)
            if user in user_order_info_time:
                index = 0
                for order_info in user_order_info_time[user]:
                    if order_info[4] == time and index < len(user_order_info_time[user]) - 1:
                        nextTime = user_order_info_time[user][index + 1][4]
                        next_day = int(nextTime[8:10])
                        next_hour = int(nextTime[nextTime.find(' ') + 1:nextTime.find(' ') + 3])

                        totalHourDiff = (next_day - cur_day) * 24 + (next_hour - cur_hour)
                        row.append(totalHourDiff)
                        break
                    if index == len(user_order_info_time[user]) - 1:
                        row.append('')
                        break
                    index += 1
            else:
                row.append('')
            ###

            # 当前用户平均骑行距离／全部用户的骑行距离
            if user in user_avg_dis_overall_avg_dis_ratio:
                row.append(user_avg_dis_overall_avg_dis_ratio[user])
            else:
                row.append('')
            ###

            # 当前小时全用户的平均骑行距离
            if hour in overall_avg_dis_cur_hour:
                row.append(overall_avg_dis_cur_hour[hour])
            else:
                row.append('')
            ###
            writer.writerow(row)

    i = 0
    with open("./data/test_hard.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        csv_reader = csv.reader(open('./data/temp/preprocess/test_b_20.csv', encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('hour')
                row.append('isHoliday')
                row.append('start_to_end_man_dis')
                row.append('user_max_man_dis')
                row.append('user_min_man_dis')
                row.append('user_mean_man_dis')
                row.append('user_mode_man_dis')

                row.append('user_cur_hour_used_ratio')
                row.append('user_next_order_time_diff')
                row.append('user_avg_dis_overall_avg_dis_ratio')
                row.append('overall_avg_dis_cur_hour')
                writer.writerow(row)
                continue
            user = row[1]
            start = row[5]
            end = row[6]
            time = row[4]

            hour = time[time.find(' ') + 1:time.find(' ') + 3]
            day = time[8:10]

            # 当前小时和节假日信息
            row.append(hour)
            if day == '13' or day == '14' or day == '20' or day == '21':
                row.append(1)
            else:
                row.append(0)
            ###

            # 加入曼哈顿距离
            row.append(function.getManhattan(start, end))
            ###

            # 加入用户骑行信息
            if user in user_dis_info:
                row.append(user_dis_info[user][0])
                row.append(user_dis_info[user][1])
                row.append(user_dis_info[user][2])
                if user_dis_info[user][3] != -1:
                    row.append(user_dis_info[user][3])
                else:
                    row.append('')
            else:
                row.append('')
                row.append('')
                row.append('')
                row.append('')

            # 用户当前小时出发比例
            if user in user_cur_hour_used_ratio:
                if hour in user_cur_hour_used_ratio[user]:
                    row.append(user_cur_hour_used_ratio[user][hour])
                else:  # 如果没有当前小时的记录
                    row.append('')
            else:
                row.append('')
            ###

            # 计算 用户当前订单时间与下次订单时间的差值
            cur_day = int(time[8:10])
            cur_hour = int(hour)
            if user in user_order_info_time:
                index = 0
                for order_info in user_order_info_time[user]:
                    if order_info[4] == time and index < len(user_order_info_time[user]) - 1:
                        nextTime = user_order_info_time[user][index + 1][4]
                        next_day = int(nextTime[8:10])
                        next_hour = int(nextTime[nextTime.find(' ') + 1:nextTime.find(' ') + 3])

                        totalHourDiff = (next_day - cur_day) * 24 + (next_hour - cur_hour)
                        row.append(totalHourDiff)
                        break
                    if index == len(user_order_info_time[user]) - 1:
                        row.append('')
                        break
                    index += 1
            else:
                row.append('')
            ###

            # 当前用户平均骑行距离／全部用户的骑行距离
            if user in user_avg_dis_overall_avg_dis_ratio:
                row.append(user_avg_dis_overall_avg_dis_ratio[user])
            else:
                row.append('')
            ###

            # 当前小时全用户的平均骑行距离
            if hour in overall_avg_dis_cur_hour:
                row.append(overall_avg_dis_cur_hour[hour])
            else:
                row.append('')
            ###
            writer.writerow(row)
