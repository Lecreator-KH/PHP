import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def graph():
    dataSet = pd.read_csv('result.csv')
    # print(dataSet)
    # sns.histplot(dataSet, x="Star Count", y="Fork Count",bins=100, discrete=(True, True), log_scale=(2, 3),cbar=True, cbar_kws=dict(shrink=.75))
    sns.histplot(dataSet[(dataSet["Star Count"]<70000)], x="Star Count", y="Fork Count",bins=25, discrete=(False, False), log_scale=(2, 2),cbar=True, cbar_kws=dict(shrink=.75),)
    # prsint(dataSet.head())
    plt.show(block=False)

if __name__ == '__main__':
    graph()
    input("Press Enter to Exit")