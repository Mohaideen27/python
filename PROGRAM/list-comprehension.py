# WRITE A PROGRAM TO CREATE A LIST FROM 1 TO N AND GENERATE NEW LIST USING LIST COMPREHENSION THAN CONTAIN 'EVEN' FOR EVEN NUMBER AND 'ODD' FOR ODD NUMBER

# print(['even' if i%2==0 else 'odd' for i in range(1,int(input("Enter 'n' value: "))+1)])

# print(['even' if j%2==0 else 'odd' for j in [i for i in range(1,int(input("Enter 'n' value: "))+1)]])

# POSITIVE AND NEGATIVE
# l=[1,-2,0,3,-1,0]
# print(['zero' if i==0 else 'positive' if i>=0 else 'negative' for i in l])

# STRING REVERSING
# l=['PYTHON','JAVA','PHP']
# print([i[::-1] for i in l])

# NEW LIST THAT CONTAINS ONLY VOWELS
l='education'

print([i for i in l if i in 'AEIOUaeiou'])