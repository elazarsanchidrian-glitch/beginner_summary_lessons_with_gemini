word = "pneumonoultramicroscopicsilicovolcanoconiosis"

length = len(word)
print(f"Length of the word: {length}")
# Output: Total letters: 45


letters = list(word)
print(letters)  # Let's just look at the letters individually
# Output: ['p', 'n', 'e', 'u', 'm'.....etc etc...


for letter in letters:
    print(letter)
#prints vertically each letter in the word

for letter in letters:
    print(letter, end=" ")
#prints horizontally each letter in the word with a space in between


for index, letter in enumerate(word, start=1):
    print(f"{index}: {letter}")
#prints the index and letter in the word, starting from 1, print every single letter in a clean, numbered vertical list


word = "pneumonoultramicroscopicsilicovolcanoconiosis"

# Convert the word into a list of characters and sort them alphabetically
sorted_letters = sorted(list(word))

print(sorted_letters)



# Convert to a set to remove duplicates, then sort alphabetically back into a list
unique_letters = sorted(list(set(word)))

print(unique_letters)



#now let's add a second word to the mix
word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
word2 = "hippopotomonstrosesquipedaliophobia"

#put them in a new list together
combined_list = [word1, word2]

print(combined_list)

#third word is going to be appended to the list
word3 = "floccinaucinihilipilification"
combined_list.append(word3)

print(combined_list)

#sort alphabetically
combined_list.sort()
print(combined_list)



#input questionnaire!


# Sort alphabetically?
combined_list.sort()
print("Initialized and sorted word list ready!")
print("-" * 50)

# Questionnaire loop
while True:
    # Get user input and convert to lowercase for case-insensitivity
    user_query = input("\nEnter a letter or series of letters to search (or type 'exit' to quit): ").strip().lower()

    if user_query == 'exit':
        print("Goodbye!")
        break

    if not user_query:
        print("Please enter at least one character.")
        continue

    # Check which words contain the user's input as a substring
    matching_words = [word for word in combined_list if user_query in word]

    # Print the results
    if matching_words:
        print(f"\n✅ Yes! '{user_query}' is found in the combined list.")
        print("Found in the following word(s):")
        for word in matching_words:
            print(f"  • {word}")
    else:
        print(f"\n❌ No, '{user_query}' is not found in any of the words.")