# Define two lists of words
list_a = ["apple", "banana", "cherry", "date", "elderberry"]
list_b = ["banana", "cherry", "fig", "grape", "apple"]

# Find common words between the two lists
common_words = set(list_a).intersection(list_b)

# Find unique words in each list
unique_to_a = set(list_a) - set(list_b)
unique_to_b = set(list_b) - set(list_a)

# Calculate word frequency (example insight for more complex cases)
from collections import Counter
combined_list = list_a + list_b
word_frequencies = Counter(combined_list)

# Print the analysis results
print("Common Words:")
print(common_words)
print("\nUnique to List A:")
print(unique_to_a)
print("\nUnique to List B:")
print(unique_to_b)
print("\nWord Frequencies Across Both Lists:")
for word, count in word_frequencies.items():
    print(f"{word}: {count} time(s)")

# Generate a new insight: Which list has more unique words?
if len(unique_to_a) > len(unique_to_b):
    print("\nInsight: List A has more unique words.")
elif len(unique_to_a) < len(unique_to_b):
    print("\nInsight: List B has more unique words.")
else:
    print("\nInsight: Both lists have an equal number of unique words.")

# Advanced insight: Highlight the most common word
most_common_word = word_frequencies.most_common(1)[0]
print(f"\nThe most common word is '{most_common_word[0]}' with {most_common_word[1]} occurrences.")

