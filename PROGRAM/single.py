# WAPPT EXTRACT ALL THE SINGLE VALUE DATATYPES FROM THE TUPLE DATATYPE
var= lambda n:type(n) in [int,float,bool,complex]
print(list(filter(var,(12,23.5,True,[1,2]))))