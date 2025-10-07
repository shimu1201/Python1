# reverse string

s1 = "Python"

print(s1[:])    #Python
print(s1[::])   #Python
print(s1[::-1]) #nohtyP

# to check string is palindrome or not
# e.g. WOW MOM

reverse = s1[::-1]

if reverse == s1:
    print("Yes, it's palindrome") 
else:
    print("No, it's not a palindrome") 

s2 = "WOW"

reverse_s2 = s2[::-1]

if reverse_s2 == s2:
    print("Yes, it's palindrome") 
else:
    print("No, it's not a palindrome") 