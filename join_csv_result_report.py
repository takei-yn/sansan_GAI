import csv
import re
import pandas as pd

#Todo　完全外部結合ではなく、アンケートメインの結合を行う

path = "./joinedcsv/join_review.csv"
path2 = "./(2022年度)結果報告データ一覧_250106a.csv"
path3 = "./(2023年度)結果報告データ一覧_250106a.csv"

customer_review = pd.read_csv(path, encoding="utf-8",  dtype=str)

bs_list_2022 = pd.read_csv(path2, encoding="CP932", dtype=str)
bs_list_2023 = pd.read_csv(path3, encoding="CP932", dtype=str)

bs_list = pd.concat([bs_list_2022, bs_list_2023], axis=0, ignore_index=True)

# 物件IDをキーにして左結合
join_review = pd.merge(customer_review, bs_list, how="left", on = "物件ID") # アンケート + BS一覧 + BS結果報告

# アンケート + BS一覧 でcsv出力
### 

# BS一覧 + BS結果報告 でcsv出力
### 

# 欠損値を空文字列で埋める
result = join_review.fillna(" ")

# join_review.to_csv('join_review_result_report.csv',encoding='utf-8')
result.to_csv('join_review_result_report.csv',encoding='utf-8')

print(result.head())

a = pd.read_csv("join_review_result_report.csv", encoding="utf-8",  dtype=str)

print(a.columns)
print(a.head())