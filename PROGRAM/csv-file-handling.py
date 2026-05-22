# def op():
#     return open('file1.csv','w')
# def cl():
#     fl.close()
#TO WRITE

# import csv
# op()
# csv.writer(fl).writerows((['name', 'age','gender'],['Naveen',25,'M',30000],['Gopi',22,'M',40000],['Yoga',21,'M',45000]))
# cl()

# TO READ

a=open('file1.csv','r')
import csv
ob=csv.reader(a)
print(list(a))
a.close