import csv
import re
import pandas as pd

path = "./【正式運用版】お客様満足度アンケ.csv"
path2 = "./物件一覧_20241212133711.csv"

customer_review = pd.read_csv(path, encoding="utf-16 LE", sep="\t")

bs_list = pd.read_csv(path2, encoding="CP932")

customer_review['受注NO'] = customer_review['受注NO'].map(lambda x : str(x)[:6])


join_review = pd.merge(customer_review, bs_list)

join_review["URL"] = "https://asahikasei-eng.svy.ooo/surveys/185371/result/panels/"

join_review['URL'] = join_review['URL'].str.cat(join_review['USER No.'].astype(str))

join_review.to_csv('join_review.csv',encoding='utf-8')

