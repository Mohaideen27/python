import csv
a=open("file1.csv","r")
for i in csv.reader(a):
    if len(i)>0:
        print(f'|{i[0]:<10}|{i[1]:>10}|{i[2]:^10}|')
a.close()