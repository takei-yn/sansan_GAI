import chardet

PATH = '物件一覧_20241212133711.csv'
MODE = 'rb'

with open(PATH, MODE) as f:
    result = chardet.detect(f.read())
    print("encoding: " + result['encoding'])
