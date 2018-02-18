# -*- coding: utf-8 -*-
import codecs
# utf-8로 저장된 CSV 파일 읽기
filename = "list.csv"
csv = codecs.open(filename, "r", "utf-8").read()
# CSV을 파이썬 리스트로 변환하기
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)
# 결과 출력하기
for c in data:
    print(c[1], c[2])
    
    