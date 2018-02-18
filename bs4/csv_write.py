# -*- coding: utf-8 -*-
import csv, codecs
with codecs.open("abc.csv", "w", "utf-8 ") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["10", "파이썬책", 30000])
    writer.writerow(["101", "자바책", 21000])
    writer.writerow(["102", "데이터베이스", 15000])
    
    