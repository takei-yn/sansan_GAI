import pandas as pd

path_customer_review = "./【正式運用版】お客様満足度アンケ.csv"
path_bs_list = "./物件一覧_20241212133711.csv"
path_bs_report_2022 = "./(2022年度)結果報告データ一覧_250106a.csv"
path_bs_report_2023 = "./(2023年度)結果報告データ一覧_250106a.csv"


customer_review = pd.read_csv(path_customer_review, encoding="utf-16 LE", sep="\t")
bs_list = pd.read_csv(path_bs_list, encoding="CP932")
bs_report_2022 = pd.read_csv(path_bs_report_2022, encoding="CP932", dtype=str)
bs_report_2023 = pd.read_csv(path_bs_report_2023, encoding="CP932", dtype=str)
#結果報告書　2022+2023
bs_report = pd.concat([bs_report_2022, bs_report_2023], axis=0, ignore_index=True)

#アンケートの受注NOの形式が「6桁番号_案件名」のため、6桁番号を抽出（BS一覧の受注NOが6桁番号のみ）
customer_review['受注NO'] = customer_review['受注NO'].map(lambda x : str(x)[:6])

#アンケートとBS一覧を内部結合 (受注Noの無いアンケートがあるため内部結合)
customer_review_with_bs_list = pd.merge(customer_review, bs_list, how="inner", on="受注NO")

#BS一覧の物件IDの型がfloat64になっているため、strに変換(結果報告書の物件IDがstr)
customer_review_with_bs_list["物件ID"] = customer_review_with_bs_list["物件ID"].map(lambda x : str(x))

# 物件IDをキーにして左結合
join_all = pd.merge(customer_review_with_bs_list, bs_report, how="left", on = "物件ID") # アンケート + BS一覧 + BS結果報告

# 欠損値を空文字列で埋める
customer_review_with_bs_list = customer_review_with_bs_list.fillna(" ")
join_all = join_all.fillna(" ")

# アンケート + BS一覧 にURLを追加
customer_review_with_bs_list["URL"] = "https://asahikasei-eng.svy.ooo/surveys/185371/result/panels/"
customer_review_with_bs_list['URL'] = customer_review_with_bs_list['URL'].str.cat(customer_review_with_bs_list['USER No.'].astype(str))
# アンケート + BS一覧 の物件名に【アンケート】を付け加えてcsv出力
customer_review_with_bs_list["物件名"] = "【アンケート】" + customer_review_with_bs_list["物件名"]
customer_review_with_bs_list.to_csv('./joinedcsv/join_review.csv',encoding='utf-8')

# BS一覧 + BS結果報告 にURLを追加
join_all["URL"] = ""
join_all['URL'] = join_all['URL'].str.cat(join_all['物件ID'].astype(str))
# BS一覧 + BS結果報告 の物件名に【BS結果報告】を付け加えてcsv出力
join_all["物件名"] = "【BS結果報告】" + join_all["物件名"]
join_all.to_csv('./leftreportcsv/join_review_result_report.csv',encoding='utf-8')

