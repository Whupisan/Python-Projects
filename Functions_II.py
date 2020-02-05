# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countDown(num):
    for i in range(num,-1,-1):
        print(i)
countDown(5)
# 
# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def printNretrn(a,b):
    print(a)
    return(b)
printNretrn(2,5)
# 
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_length(array):
    return array[0]+ (len(array))
# 
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
arrNew = []
array = [5,2,3,2,1,4]
def valuesGreater(array):                      
    if (len(array) < 2):                 
        return False  
    else:
        for i in range(len(array)):             #        
            if (array[i]>array[1]):           #  if(5>2) if(2>2) if(3>2) if(2>2) if(1>2) if(4>2)        
                arrNew.append(array[i])        #  , arrNew
    return len(arrNew), arrNew
y = valuesGreater(array)
print(y)
# 
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def repeater(former, latter):
    i=0
    while i < former:
        print (latter)
        i+=1
repeater(6,8)