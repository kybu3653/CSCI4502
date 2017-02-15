#! usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing
import argparse
from scipy import stats
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-f1", "--file1", help="File1",type=file)
parser.add_argument("-a1", "--attribute1", help="Attribute1")
parser.add_argument("-f2", "--file2", help="File2",type=file)
parser.add_argument("-a2", "--attribute2", help="Attribute2")
parser.add_argument("-n", "--norm_type", help="Normalization Type (z or min-max)")

args = parser.parse_args()

if args.file1 and args.attribute1 and args.norm_type:
    df = pd.read_csv(args.file1)
    assert args.attribute1 in ["open","high","low","close","volume"]

    attr = df[args.attribute1]
    if args.norm_type == "min_max":
        min_max_scaler = preprocessing.MinMaxScaler()
        attr_min_max = min_max_scaler.fit_transform(attr)

        for i in range(len(attr)):
            print attr[i], "\t", attr_min_max[i]
    elif args.norm_type == "z_score":
        #std_scaler = preprocessing.StandardScaler().fit(attr)
        #attr_std = std_scaler.fit_transform(attr)
        #print attr_std.mean(),attr_std.std()

        Z_score = stats.zscore(attr)
        for i in range(len(attr)):
            print attr[i],"\t",Z_score[i]

elif args.file1 and args.file2 and args.attribute1 and args.attribute2:
    df1 = pd.read_csv(args.file1)
    df2 = pd.read_csv(args.file2)
    assert args.attribute1 in ["open","high","low","close","volume"] and args.attribute2 in  ["open","high","low","close","volume"] 

    attr1 = df1[args.attribute1]
    attr2 = df2[args.attribute2]
    matrix = np.corrcoef(attr1,attr2)
    print matrix[0][1]
else:
    df = pd.read_csv('HistoricalQuotes.csv')
    dates = []
    for element in df.date:
        yy,mm,dd = map(int, element.split("/"))
        dates.append(datetime(year=yy,month=mm,day=dd))
    plt.plot(dates,df.low,color="red")
    plt.plot(dates,df.high,color="blue")
    low_patch = matplotlib.patches.Patch(color="red",label="Low")
    high_patch = matplotlib.patches.Patch(color="blue",label="High")
    plt.legend(handles=[high_patch,low_patch],loc = 0)
    plt.title("Temporal change of high and low attributes")
    plt.xlabel("Date")
    plt.ylabel("Dollars")
    plt.show()
    
    #BOX PLOT FOR OPEN AND CLOSED
    #used http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/ as reference
    data = [df.open,df.close]
    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data,patch_artist=True)

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    ax.set_xticklabels(['Open', 'Close'])
    plt.title("Boxplot of Open and Close")
    plt.show()

    #Histogram of volume with 10 equal sized bins
    plt.hist(df.volume,10)
    plt.title("Volume Histogram")
    plt.show()

    #plot that I am interested in
    plt.plot(dates,df.high/df.low,color="red")
    plt.plot(dates,df.close/df.open,color="blue")
    low_patch = matplotlib.patches.Patch(color="red",label="High/Low")
    high_patch = matplotlib.patches.Patch(color="blue",label="Close/Open")
    plt.legend(handles=[high_patch,low_patch],loc = 0)
    plt.axhline(y=1, color='black')
    plt.title("Temporal change of ratios of sales prices")
    plt.xlabel("Date")
    plt.ylabel("Unitless")
    plt.show()


