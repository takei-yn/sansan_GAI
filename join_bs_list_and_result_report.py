import pandas as pd

path = "./物件一覧_20241212133711.csv"
path2 = "./(2022年度)結果報告データ一覧_250106a.csv"
path3 = "./(2023年度)結果報告データ一覧_250106a.csv"

customer_review = pd.read_csv(path, encoding="CP932",  dtype=str)

bs_list_2022 = pd.read_csv(path2, encoding="CP932", dtype=str)
bs_list_2023 = pd.read_csv(path3, encoding="CP932", dtype=str)

bs_list = pd.concat([bs_list_2022, bs_list_2023], axis=0, ignore_index=True)

# 物件IDをキーにして左結合
join_review = pd.merge(customer_review, bs_list, how="outer", on = "物件ID")

# 欠損値を空文字列で埋める
result = join_review.fillna(" ")

# URLを作成
result["URL"] = ""

result['URL'] = result['URL'].str.cat(result['物件ID'].astype(str))

# join_review.to_csv('join_review_result_report.csv',encoding='utf-8')
result.to_csv('./bs_list_and_result_report/bs_list_and_result_report.csv',encoding='utf-8')

print(result.head())

a = pd.read_csv("./bs_list_and_result_report/bs_list_and_result_report.csv", encoding="utf-8",  dtype=str)

print(a.columns)
print(a.head())