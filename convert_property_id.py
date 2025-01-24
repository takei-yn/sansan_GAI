import pandas as pd

# BS結果報告と分かるように、BS結果報告の物件名を変更
bs_list_and_result_report = pd.read_csv("./bs_list_and_result_report/bs_list_and_result_report.csv", encoding="utf-8",  dtype=str)
bs_list_and_result_report["物件名"] = "【BS結果報告】" + bs_list_and_result_report["物件名"]

# 上のBSのみのデータだとデータが多すぎるため、アンケートのデータを結合した後のデータを利用する (SmartTextHub取込時にFilterする)
join_review_result_report = pd.read_csv("./leftreportcsv/join_review_result_report.csv", encoding="utf-8",  dtype=str)
join_review_result_report["物件名"] = "【BS結果報告】" + join_review_result_report["物件名"]
# 欠損値を空文字列で埋める
result = join_review_result_report.fillna(" ")

# URLを作成
result["URL"] = ""

result['URL'] = result['URL'].str.cat(result['物件ID'].astype(str))

result.to_csv('./leftreportcsv/join_review_result_report.csv',encoding='utf-8')

# アンケートと分かるように、アンケートの物件名を変更
bs_list_and_result_report.to_csv('./bs_list_and_result_report/bs_list_and_result_report.csv',encoding='utf-8')
print(bs_list_and_result_report.head())

join_review = pd.read_csv("./joinedcsv/join_review.csv", encoding="utf-8",  dtype=str)
join_review["物件名"] = "【アンケート】" + join_review["物件名"]

join_review.to_csv('./joinedcsv/join_review.csv',encoding='utf-8')
print(join_review.head())