#String Slicing (Extract Parts of a String)
text = "Python programming is fun"
first_word = text.split()[0]
print(first_word)
#Last Word
last_word = text.split()[-1]
print(last_word)
#Middle Section
middle = text[7:18]
print(middle)

#. String Formatting (Insert Variables into Strings)
name = "Vamshika"
age = 20

print(f"My name is {name} and I am {age} years old.")
#Using .format()
name = "Vamshika"
course = "Python"

print("My name is {} and I am learning {}".format(name, course))
#String Methods
text = "python is easy to learn"
#Uppercase
print(text.upper())

#Lowercase
print(text.lower())
#Replace
print(text.replace("easy", "fun"))

#Split
words = text.split()
print(words)

#Join
words = ['Python', 'is', 'very', 'powerful']
sentence = " ".join(words)
print(sentence)

#String Manipulation Example (Sentence)
sentence = "Python is a powerful programming language"


print(sentence.upper())


print(sentence.replace("powerful", "amazing"))


words = sentence.split()
print(words)


new_sentence = "-".join(words)
print(new_sentence)

