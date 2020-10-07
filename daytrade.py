import pandas as pd
import numpy as np

df_today = pd.read_csv('./data/T201007.csv', encoding='cp932')
df_1ago = pd.read_csv('./data/T201006.csv', encoding='cp932')
df_2ago = pd.read_csv('./data/T201005.csv', encoding='cp932')
df_3ago = pd.read_csv('./data/T201002.csv', encoding='cp932')

# [日付、番号、？、銘柄名、始値、高値、安値、終値、出来高、市場]

columns_today = df_today.columns
columns_1ago = df_1ago.columns
columns_2ago = df_2ago.columns
columns_3ago = df_3ago.columns

data_today = df_today[[columns_today[1],columns_today[4],columns_today[7]]].values
data_1ago = df_1ago[[columns_1ago[1],columns_1ago[4],columns_1ago[7]]].values
data_2ago = df_2ago[[columns_2ago[1],columns_2ago[4],columns_2ago[7]]].values
data_3ago = df_3ago[[columns_3ago[1],columns_3ago[4],columns_3ago[7]]].values

def up_candle(column):
    if column[1]<column[2]:
        return True
    else:
        return False

def down_candle(column):
    if column[1]>column[2]:
        return True
    else:
        return False

def check_downtrend(column_previous,column):
    if down_candle(column_previous) & down_candle(column):
        if (column_previous[1] > column[1]) & (column_previous[2] > column[2]):
            return True
        else:
            return False
    else:
        return False

def down_to_up(column_previous,column):
    if down_candle(column_previous) & up_candle(column):

        if (column_previous[2] < column[1]) & (column_previous[1] < column[2]):
            return True
        else:
            return False
    else:
        return False



for column in data_today:
    today_index = column[0]
    column_today = column
    column_1ago = [0,0,0]
    column_2ago = [0,0,0]
    column_3ago = [0,0,0]

    for column in data_1ago:
        if today_index == column[0]:
            column_1ago = column


    for column in data_2ago:
        if today_index == column[0]:
            column_2ago = column


    for column in data_3ago:
        if today_index == column[0]:
            column_3ago = column

    if(check_downtrend(column_3ago,column_2ago)):
        if (check_downtrend(column_2ago, column_1ago)):
            if(down_to_up(column_1ago,column_today)):
                print(int(today_index))






