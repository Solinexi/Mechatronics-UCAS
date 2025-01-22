'''
This program creates a list using list comprehension, then prints it, removes a value and prints again, then prints the highest and lowest values in the list.
'''
l = [i**2 for i in range(1, 11)] # Creates our list of squares
print(l) # Prints it

l.pop() # Removes the last value of the list
print(l) # Prints it

print(min(l)) # Uses the min function to print the lists lowest value
print(max(l)) # Uses the max function to print the lists highest value
