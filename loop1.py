"""
for var in sequence:
    statement
range([start],stop,[step]):

syntax :

    range(2,6)  # 2 3 4 5

    range(5)    # 0 1 2 3 4

    range(1,7,2)    # start, stop, step
                    # 1 3 5 
"""

#1

for i in range(6): # by default starts from 0 to 5
    print(i)

#2

for i in range(1,6): 
    print(f"({i}) Hello")

#3

for i in range(1,6): 
    print(i,end= " ")