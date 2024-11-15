# Define two lists of numbers
list1 = [10, 20, 30, 40, 50]
list2 = [15, 25, 35, 45, 55]

# Calculate the sum of each list
sum_list1 = sum(list1)
sum_list2 = sum(list2)

# Calculate the average of each list
avg_list1 = sum_list1 / len(list1)
avg_list2 = sum_list2 / len(list2)

# Find the maximum and minimum values in each list
max_list1 = max(list1)
min_list1 = min(list1)
max_list2 = max(list2)
min_list2 = min(list2)

# Print the results
print(f"List 1: {list1}")
print(f"Sum of List 1: {sum_list1}")
print(f"Average of List 1: {avg_list1}")
print(f"Max of List 1: {max_list1}")
print(f"Min of List 1: {min_list1}")

print(f"List 2: {list2}")
print(f"Sum of List 2: {sum_list2}")
print(f"Average of List 2: {avg_list2}")
print(f"Max of List 2: {max_list2}")
print(f"Min of List 2: {min_list2}")

# Find the difference between the sums and averages of the two lists
sum_difference = sum_list2 - sum_list1
avg_difference = avg_list2 - avg_list1

print(f"Difference in sums: {sum_difference}")
print(f"Difference in averages: {avg_difference}")
