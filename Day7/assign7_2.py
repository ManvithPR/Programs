from collections import Counter

# Accept a sentence
sentence = input("Enter a sentence: ")

# Count frequency of each character
char_freq = Counter(sentence)

print("\nCharacter Frequencies:")
for char, count in char_freq.items():
    print(f"'{char}' : {count}")

# Find first non-repeating character
first_non_repeating = None

for char in sentence:
    if char_freq[char] == 1:
        first_non_repeating = char
        break

if first_non_repeating:
    print("\nFirst Non-Repeating Character:", first_non_repeating)
else:
    print("\nNo Non-Repeating Character Found")

# Accept two words for anagram checking
word1 = input("\nEnter the first word: ")
word2 = input("Enter the second word: ")

# Check Anagram
if sorted(word1.lower()) == sorted(word2.lower()):
    print("The words are Anagrams.")
else:
    print("The words are NOT Anagrams.")

# Display unique characters in the sentence
unique_chars = set(sentence)

print("\nUnique Characters in the Sentence:")
print(unique_chars)