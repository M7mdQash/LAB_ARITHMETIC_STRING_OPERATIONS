the_string = "Python is a great programming language"
the_word = "great"

#the printing parts
print("The length of the string is",len(the_string))
print("The index of the word",the_string.find(the_word))
print("The number of times the word appears in the string is",the_string.count(the_word) )
print("The string in uppercase is",the_string.upper())
print("The string in lowercase is",the_string.lower())

print("The string with the word'",the_word,"'replaced with 'awesome' is:",the_string.replace(the_word,"awesome") )
print("the last character in the string is",the_string[-1] )