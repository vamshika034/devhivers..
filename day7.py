#Basic Word Counter Script
# Word Counter Program

text = input("hello, how are you: ")

words = text.split()   # split sentence into words
word_count = len(words)  # count words

print("Total number of words:", word_count)


#Sum of Two Numbers
a = int(input("12: "))
b = int(input("18: "))

sum = a + b
print("Sum is:", sum)

#Find Largest Number
a = int(input("98: "))
b = int(input("99: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)


 #Factorial of a Number
num = int(input("78: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial is:", fact)    
