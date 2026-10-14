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


