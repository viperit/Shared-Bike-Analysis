#encoding: utf-8 
import csv
import numpy as np
import networkx as nx
import math
from scipy.stats import mode


#区分训练集和测试集
def read_and_split_train():
    train_s_20 = []
    test_b_20 = []
    i=0
    csv_reader = csv.reader(open('./data/train.csv', encoding='utf-8'))
    for row in csv_reader:
        i+=1
        if i == 1:
            train_s_20.append(row)
            test_b_20.append(row)
            continue

        if row[4] < "2017-05-20 00:00:00":
            train_s_20.append(row)
        else:
            test_b_20.append(row)

    with open("./data/temp/preprocess/train_b_20.csv", 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in train_s_20: 
                writer.writerow(row)                 
    with open("./data/temp/preprocess/test_b_20.csv", 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in test_b_20: 
                writer.writerow(row) 



