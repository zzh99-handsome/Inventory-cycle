import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

def visualize(x,y):

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, y)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))

    ax.axvspan(pd.Timestamp('2006-07-03'), pd.Timestamp('2008-05-30'), facecolor='gray', alpha=0.1)
    ax.axvspan(pd.Timestamp('2009-11-30'), pd.Timestamp('2010-02-26'), facecolor='blue', alpha=0.1)
    ax.axvspan(pd.Timestamp('2013-09-30'), pd.Timestamp('2013-12-31'), facecolor='green', alpha=0.1)
    ax.axvspan(pd.Timestamp('2016-08-01'), pd.Timestamp('2017-03-31'), facecolor='red', alpha=0.1)
    ax.axvspan(pd.Timestamp('2019-12-31'), pd.Timestamp('2021-02-26'), facecolor='yellow', alpha=0.1)
    plt.xticks(rotation=45)

    plt.show()

if __name__=='__main__':
    df=pd.read_excel('./主动补库 南华工业品指数-沪深300.xlsx')
    df['date']=pd.to_datetime(df['date'])
    visualize(df['date'],df['nv'])