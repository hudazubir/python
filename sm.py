#----------This is a STRING MANIPULATION !!!!-------------

#Input a string from the user
user_input = input("Enter a senctence: ")

#Convert the input to uppercase
uppercase_input = user_input.upper()
print("Uppercase:", uppercase_input)

#Convert the input to lowercase
lowercase_input = user_input.lower()
print("lowercase:", lowercase_input)

#Capitalize the first letter of the input
capitalized_input = user_input.capitalize()
print("capital:", capitalized_input)

#Count the occurrences of a specific word
target_word = "Python"
word_count = user_input.count(target_word)
print (f"The word '{target_word}' appears {word_count} times.")

#Replacement a word with another word
replacement_word = "Programming"
new_input = user_input.replace(target_word, replacement_word)
print("After replacement:", new_input)

#Split the input into a list of words
word_list = user_input.split()
print("Word List:", word_list)

#Join the words in the list to form a sentence
joined_sentence = " ".join(word_list)
print("Joined Sentence:", joined_sentence)