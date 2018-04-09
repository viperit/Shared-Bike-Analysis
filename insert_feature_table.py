# encoding: utf-8

"""
插入特征表
"""
import pickle
import csv


# 不geofly，4个一组（普通），2个一组（当前小时）
# 起点geofly，4个一组（普通），2个一组（当前小时）
# 终点geofly，4个一组（普通），2个一组（当前小时）
# 双geofly，6组

# 不geofly的，读四个表，插8个属性
def insert_part12_1(readPath, outPath):
    print("insert_part12_1")

    with open('./data/temp/feature_table/cur_hour_start_to_end_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_start_ratio', 'rb') as f:
        start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_end_ratio', 'rb') as f:
        end_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_overall_ratio', 'rb') as f:
        overall_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_ratio')
                row.append('cur_hour_start_to_end_start_out_ratio')
                row.append('cur_hour_start_to_end_end_in_ratio')
                row.append('cur_hour_start_to_end_overall_ratio')

                row.append('cur_hour_end_to_start_ratio')
                row.append('cur_hour_end_to_start_end_out_ratio')
                row.append('cur_hour_end_to_start_start_in_ratio')
                row.append('cur_hour_end_to_start_overall_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点到终点
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(end_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(overall_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(end_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(overall_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 不geofly，读2个表，插4个属性，当前小时
def insert_part12_2(readPath, outPath):
    print("insert_part12_2")

    with open('./data/temp/feature_table/cur_hour_start_to_end_cur_hour_start_ratio', 'rb') as f:
        cur_hour_start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_cur_hour_end_ratio', 'rb') as f:
        cur_hour_end_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_cur_hour_start_out_ratio')
                row.append('cur_hour_start_to_end_cur_hour_end_in_ratio')

                row.append('cur_hour_end_to_start_cur_hour_end_out_ratio')
                row.append('cur_hour_end_to_start_cur_hour_start_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点到终点
            row.append(cur_hour_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点
            row.append(cur_hour_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 起点geofly，4个一组（普通）
def insert_part12_3(readPath, outPath):
    print("insert_part12_3")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_start_geofly_ratio', 'rb') as f:
        start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_end_ratio', 'rb') as f:
        end_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_overall_ratio', 'rb') as f:
        overall_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_ratio')
                row.append('cur_hour_start_geofly_to_end_start_geofly_out_ratio')
                row.append('cur_hour_start_geofly_to_end_end_in_ratio')
                row.append('cur_hour_start_geofly_to_end_overall_ratio')

                row.append('cur_hour_end_geofly_to_start_ratio')
                row.append('cur_hour_end_geofly_to_start_end_geofly_out_ratio')
                row.append('cur_hour_end_geofly_to_start_start_in_ratio')
                row.append('cur_hour_end_geofly_to_start_overall_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(end_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(overall_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点geofly
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(end_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(overall_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 起点geofly，2个一组（每小时）
def insert_part12_4(readPath, outPath):
    print("insert_part12_4")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio', 'rb') as f:
        cur_hour_start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_cur_hour_end_ratio', 'rb') as f:
        cur_hour_end_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_cur_hour_start_geofly_out_ratio')
                row.append('cur_hour_end_to_start_geofly_cur_hour_end_out_ratio')

                row.append('cur_hour_end_geofly_to_start_cur_hour_end_geofly_out_ratio')
                row.append('cur_hour_end_geofly_to_start_cur_hour_start_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点
            row.append(cur_hour_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点
            row.append(cur_hour_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 终点geofly，4个一组（普通）
def insert_part12_5(readPath, outPath):
    print("insert_part12_5")

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_start_ratio', 'rb') as f:
        start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_end_geofly_ratio', 'rb') as f:
        end_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_overall_ratio', 'rb') as f:
        overall_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_geofly_ratio')
                row.append('cur_hour_start_to_end_geofly_start_out_ratio')
                row.append('cur_hour_start_to_end_geofly_end_geofly_in_ratio')
                row.append('cur_hour_start_to_end_geofly_overall_ratio')

                row.append('cur_hour_end_to_start_geofly_ratio')
                row.append('cur_hour_end_to_start_geofly_end_out_ratio')
                row.append('cur_hour_end_to_start_geofly_start_geofly_in_ratio')
                row.append('cur_hour_end_to_start_geofly_overall_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点到终点geolfy
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(end_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(overall_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点geofly
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(end_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(overall_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 终点geofly，2个一组（每小时）
def insert_part12_6(readPath, outPath):
    print("insert_part12_6")

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_cur_hour_start_ratio', 'rb') as f:
        cur_hour_start_ratio = pickle.load(f)

    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_cur_hour_end_geofly_ratio', 'rb') as f:
        cur_hour_end_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_geofly_cur_hour_start_out_ratio')
                row.append('cur_hour_start_to_end_geofly_cur_hour_end_geofly_in_ratio')

                row.append('cur_hour_end_to_start_geofly_cur_hour_end_out_ratio')
                row.append('cur_hour_end_to_start_geofly_cur_hour_start_geofly_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点到终点geofly
            row.append(cur_hour_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点geofly
            row.append(cur_hour_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_end_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为所有历史次数
def insert_part12_7(readPath, outPath):
    print("insert_part12_7")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点goefly / 所有历史次数
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点goefly / 所有历史次数
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为起点（终点）出发总次数
def insert_part12_8(readPath, outPath):
    print("insert_part12_8")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_start_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_start_geofly_out_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_end_geofly_out_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点goefly / 起点geofly总出发次数
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点goefly / 终点geofly总出发次数
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为当前小时起点（终点）出发总次数
def insert_part12_9(readPath, outPath):
    print("insert_part12_9")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_out_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_cur_hour_end_geofly_out_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点geofly / 当前小时起点goefly总出发
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点geofly / 当前小时终点geofly总出发
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为终点（起点）到达总次数
def insert_part12_10(readPath, outPath):
    print("insert_part12_10")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_end_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_end_geofly_in_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_start_geofly_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点goefly到终点geofly / 终点geofly总到达
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点geofly / 起点geofly总到达
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为当前小时终点（起点）到达总次数
def insert_part12_11(readPath, outPath):
    print("insert_part12_11")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_in_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_cur_hour_start_geofly_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点geofly / 当前小时终点geofly总到达
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点geofly / 当前小时起点geofly总到达
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 双geofly，分母为起点到终点总次数
def insert_part12_12(readPath, outPath):
    print("insert_part12_12")

    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_overall_ratio', 'rb') as f:
        ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_geofly_to_end_geofly_overall_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_overall_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点geofly到终点geofly / 起点到终点总次数
            row.append(ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点geofly到起点geofly / 终点到起点总次数
            row.append(ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 分母为所有历史次数
def insert_part_12_1_ratio(readPath, outPath):
    print("insert_part_12_1_ratio")

    print("load files")
    # 当前小时从此起点到此终点的次数 / 所有历史次数
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_ratio', 'rb') as f:
        cur_hour_start_to_end_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_geofly_ratio = pickle.load(f)

    print("insert features")
    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_ratio')
                row.append('cur_hour_start_geofly_to_end_ratio')
                row.append('cur_hour_start_to_end_geofly_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_ratio')

                row.append('cur_hour_end_to_start_ratio')
                row.append('cur_hour_end_geofly_to_start_ratio')
                row.append('cur_hour_end_to_start_geofly_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = row[7]

            # 起点到终点/所有历史次数
            row.append(cur_hour_start_to_end_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点/所有历史次数
            row.append(cur_hour_start_to_end_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 分母为出发总次数
def insert_part_12_2_out_ratio(readPath, outPath):
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_start_ratio', 'rb') as f:
        cur_hour_start_to_end_start_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_start_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_start_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_start_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_geofly_start_geofly_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_start_out_ratio')
                row.append('cur_hour_start_geofly_to_end_start_geofly_out_ratio')
                row.append('cur_hour_start_to_end_geofly_start_out_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_start_geofly_out_ratio')

                row.append('cur_hour_end_to_start_end_out_ratio')
                row.append('cur_hour_end_geofly_to_start_end_geofly_out_ratio')
                row.append('cur_hour_end_to_start_geofly_end_out_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_end_geofly_out_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = str(row[7])

            # 起点到终点/所有历史次数
            row.append(cur_hour_start_to_end_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(
                cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_start_geofly_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点/所有历史次数
            row.append(cur_hour_start_to_end_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(
                cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_start_geofly_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 分母为当前小时出发总次数
def insert_part_12_3_cur_hour_out_ratio(readPath, outPath):
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_cur_hour_start_ratio', 'rb') as f:
        cur_hour_start_to_end_cur_hour_start_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_cur_hour_start_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_cur_hour_start_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_cur_hour_start_out_ratio')
                row.append('cur_hour_start_geofly_to_end_cur_hour_start_geofly_out_ratio')
                row.append('cur_hour_start_to_end_geofly_cur_hour_start_out_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_out_ratio')

                row.append('cur_hour_end_to_start_cur_hour_end_out_ratio')
                row.append('cur_hour_end_geofly_to_start_cur_hour_end_geofly_out_ratio')
                row.append('cur_hour_end_to_start_geofly_cur_hour_end_out_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_cur_hour_end_geofly_out_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = str(row[7])

            # 起点到终点/所有历史次数
            row.append(cur_hour_start_to_end_cur_hour_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(
                cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_cur_hour_start_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(
                cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio.get(start, {}).get(end, {}).get(hour,
                                                                                                                0))

            # 终点到起点/所有历史次数
            row.append(cur_hour_start_to_end_cur_hour_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_cur_hour_start_geofly_ratio.get(end, {}).get(start, {}).get(hour,
                                                                                                                0))
            row.append(cur_hour_start_to_end_geofly_cur_hour_start_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_cur_hour_start_geofly_ratio.get(end, {}).get(start, {}).get(
                hour, 0))

            # 写出
            writer.writerow(row)


# 分母为到达总次数
def insert_part_12_4_in_ratio(readPath, outPath):
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_end_ratio', 'rb') as f:
        cur_hour_start_to_end_end_in_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_end_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_end_in_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_end_geofly_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_end_geofly_in_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_end_geofly_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_geofly_end_geofly_in_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_end_in_ratio')
                row.append('cur_hour_start_geofly_to_end_end_in_ratio')
                row.append('cur_hour_start_to_end_geofly_end_geofly_in_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_end_geofly_in_ratio')

                row.append('cur_hour_end_to_start_start_in_ratio')
                row.append('cur_hour_end_geofly_to_start_start_in_ratio')
                row.append('cur_hour_end_to_start_geofly_start_geofly_in_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_start_geofly_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = str(row[7])

            # 起点到终点/终点到达次数
            row.append(cur_hour_start_to_end_end_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_end_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_end_geofly_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_end_geofly_in_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点/起点到达次数
            row.append(cur_hour_start_to_end_end_in_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_end_in_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_end_geofly_in_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_end_geofly_in_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


# 分母为当前小时到达总次数
def insert_part_12_5_cur_hour_in_ratio(readPath, outPath):
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_cur_hour_end_ratio', 'rb') as f:
        cur_hour_start_to_end_cur_hour_end_in_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_cur_hour_end_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_cur_hour_end_in_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_cur_hour_end_geofly_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_cur_hour_end_geofly_in_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_ratio',
              'rb') as f:
        cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_in_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_cur_hour_end_in_ratio')
                row.append('cur_hour_start_geofly_to_end_cur_hour_end_in_ratio')
                row.append('cur_hour_start_to_end_geofly_cur_hour_end_geofly_in_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_in_ratio')

                row.append('cur_hour_end_to_start_cur_hour_start_in_ratio')
                row.append('cur_hour_end_geofly_to_start_cur_hour_start_in_ratio')
                row.append('cur_hour_end_to_start_geofly_cur_hour_start_geofly_in_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_cur_hour_start_geofly_in_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = str(row[7])

            # 起点到终点/所有历史次数
            row.append(cur_hour_start_to_end_cur_hour_end_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_cur_hour_end_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(
                cur_hour_start_to_end_geofly_cur_hour_end_geofly_in_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(
                cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_in_ratio.get(start, {}).get(end, {}).get(hour,
                                                                                                                 0))

            # 终点到起点/所有历史次数
            row.append(cur_hour_start_to_end_cur_hour_end_in_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_cur_hour_end_in_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_cur_hour_end_geofly_in_ratio.get(end, {}).get(start, {}).get(hour,
                                                                                                                 0))
            row.append(cur_hour_start_geofly_to_end_geofly_cur_hour_end_geofly_in_ratio.get(end, {}).get(start,
                                                                                                         {}).get(
                hour, 0))

            # 写出
            writer.writerow(row)


# 分母为起点到终点（终点到起点）总次数
def insert_part_12_6_overall_ratio(readPath, outPath):
    # 不geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_overall_ratio', 'rb') as f:
        cur_hour_start_to_end_overall_ratio = pickle.load(f)

    # 起点geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_overall_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_overall_ratio = pickle.load(f)

    # 终点geofly
    with open('./data/temp/feature_table/cur_hour_start_to_end_geofly_overall_ratio', 'rb') as f:
        cur_hour_start_to_end_geofly_overall_ratio = pickle.load(f)

    # 双geofly
    with open('./data/temp/feature_table/cur_hour_start_geofly_to_end_geofly_overall_ratio', 'rb') as f:
        cur_hour_start_geofly_to_end_geofly_overall_ratio = pickle.load(f)

    with open(outPath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        i = 0
        csv_reader = csv.reader(open(readPath, encoding='utf-8'))
        for row in csv_reader:
            i += 1
            if i == 1:
                row.append('cur_hour_start_to_end_overall_ratio')
                row.append('cur_hour_start_geofly_to_end_overall_ratio')
                row.append('cur_hour_start_to_end_geofly_overall_ratio')
                row.append('cur_hour_start_geofly_to_end_geofly_overall_ratio')

                row.append('cur_hour_end_to_start_overall_ratio')
                row.append('cur_hour_end_geofly_to_start_overall_ratio')
                row.append('cur_hour_end_to_start_geofly_overall_ratio')
                row.append('cur_hour_end_geofly_to_start_geofly_overall_ratio')

                writer.writerow(row)
                continue

            start = row[5]
            end = row[6]
            hour = str(row[7])

            # 起点到终点/起点到终点总次数
            row.append(cur_hour_start_to_end_overall_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_overall_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_overall_ratio.get(start, {}).get(end, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_overall_ratio.get(start, {}).get(end, {}).get(hour, 0))

            # 终点到起点/终点到起点总次数
            row.append(cur_hour_start_to_end_overall_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_overall_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_to_end_geofly_overall_ratio.get(end, {}).get(start, {}).get(hour, 0))
            row.append(cur_hour_start_geofly_to_end_geofly_overall_ratio.get(end, {}).get(start, {}).get(hour, 0))

            # 写出
            writer.writerow(row)


def insert():
    # insert_part_12_1_ratio('./data/train_hard.csv', './data/train_hard_p12_1')
    # insert_part_12_1_ratio('./data/test_hard.csv', './data/test_hard_p12_1')
    #
    # insert_part_12_2_out_ratio('./data/train_hard_p12_1', './data/train_hard_p12_2')
    # insert_part_12_2_out_ratio('./data/test_hard_p12_1', './data/test_hard_p12_2')
    #
    # insert_part_12_3_cur_hour_out_ratio('./data/train_hard_p12_2', './data/train_hard_p12_3')
    # insert_part_12_3_cur_hour_out_ratio('./data/test_hard_p12_2', './data/test_hard_p12_3')
    #
    # insert_part_12_4_in_ratio('./data/train_hard_p12_3', './data/train_hard_p12_4')
    # insert_part_12_4_in_ratio('./data/test_hard_p12_3', './data/test_hard_p12_4')

    insert_part12_1('./data/train_hard.csv', './data/train_hard_p12_1')
    insert_part12_1('./data/test_hard.csv', './data/test_hard_p12_1')

    insert_part12_2('./data/train_hard_p12_1', './data/train_hard_p12_2')
    insert_part12_2('./data/test_hard_p12_1', './data/test_hard_p12_2')

    insert_part12_3('./data/train_hard_p12_2', './data/train_hard_p12_3')
    insert_part12_3('./data/test_hard_p12_2', './data/test_hard_p12_3')

    insert_part12_4('./data/train_hard_p12_3', './data/train_hard_p12_4')
    insert_part12_4('./data/test_hard_p12_3', './data/test_hard_p12_4')

    insert_part12_5('./data/train_hard_p12_4', './data/train_hard_p12_5')
    insert_part12_5('./data/test_hard_p12_4', './data/test_hard_p12_5')

    insert_part12_6('./data/train_hard_p12_5', './data/train_hard_p12_6')
    insert_part12_6('./data/test_hard_p12_5', './data/test_hard_p12_6')

    insert_part12_7('./data/train_hard_p12_6', './data/train_hard_p12_7')
    insert_part12_7('./data/test_hard_p12_6', './data/test_hard_p12_7')

    insert_part12_8('./data/train_hard_p12_7', './data/train_hard_p12_8')
    insert_part12_8('./data/test_hard_p12_7', './data/test_hard_p12_8')

    insert_part12_9('./data/train_hard_p12_8', './data/train_hard_p12_9')
    insert_part12_9('./data/test_hard_p12_8', './data/test_hard_p12_9')

    insert_part12_10('./data/train_hard_p12_9', './data/train_hard_p12_10')
    insert_part12_10('./data/test_hard_p12_9', './data/test_hard_p12_10')

    insert_part12_11('./data/train_hard_p12_10', './data/train_hard_p12_11')
    insert_part12_11('./data/test_hard_p12_10', './data/test_hard_p12_11')

    insert_part12_12('./data/train_hard_p12_11', './data/train_hard_p12.csv')
    insert_part12_12('./data/test_hard_p12_11', './data/test_hard_p12.csv')
