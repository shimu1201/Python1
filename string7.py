"""
0   1   2   3   (Positive Indexing)
J   A   V   A
-4  -3  -2  -1  (Negative Indexing)
"""

# string slicing
s1 = "JAVA"
# fetch last character from the string
print(s1[-1])

# string slicing - fetch first 2 characters from the string 
print(s1[0:2])  #JA

#or
#JA
print(s1[:2])    # by default it will starts from 0

# fetch next 2 character from middle

print(s1[1:3])  #AV

# slicing using og negative indexing
print(s1[-3:-1])    #AV

# JAVA : fetch only AVA
print(s1[-3])   # by default it will ends with -1