# -*- coding: utf-8 -*-
import csv, codecs
# CSV 파일 열기
filename = "list.csv"
fp = codecs.open(filename, "r", "utf-8")
# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
    
    