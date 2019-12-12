import matplotlib.pyplot as plt
import csv
import time

while(True):
    offset = 0
    graph4000 = []
    time00 = []
    graph4001 = []
    time01 = []
    graph4002 = []
    time02 = []
    with open('graph4000.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                graph4000.append(float(row[0]))
                offset = float(row[1])
                time00.append(int(row[2]))
                line_count += 1
            else:
                graph4000.append(float(row[0]))
                time00.append(int(row[2]))
                line_count += 1
    with open('graph4001.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        offset4001 = 0
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                graph4001.append(float(row[0]))
                offset4001 = int(float(row[1]) - float(offset))
                time01.append(offset4001)
                line_count += 1
            else:
                graph4001.append(float(row[0]))
                preTime = int(row[2]) + offset4001
                time01.append(preTime)
                line_count += 1
    with open('graph4002.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        offset4002 = 0
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                graph4002.append(float(row[0]))
                offset4002 = int(float(row[1]) - float(offset))
                time02.append(offset4002)
                line_count += 1
            else:
                graph4002.append(float(row[0]))
                preTime = int(row[2]) + offset4002
                time02.append(preTime)
                line_count += 1


    plt.ion()
    plt.plot(time00, graph4000, color='red')
    plt.plot(time01, graph4001, color='blue')
    plt.plot(time02, graph4002, color='green')
    plt.ylabel('bandwidth:')
    plt.xlabel('time:')
    plt.pause(1)
    time.sleep(1)
    #time.sleep(20)
    #plt.close('all')
