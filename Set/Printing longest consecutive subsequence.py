def longest_consecutive_sequence(nums):
    # Convert the list to a set for O(1) lookup time
    num_set = set(nums)
    longest_seq = []
    
    # Iterate through the numbers
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_seq = [current_num]  # Initialize current sequence

            # Count the length of the sequence and store elements
            while current_num + 1 in num_set:
                current_num += 1
                current_seq.append(current_num)

            # Update the longest sequence if the current one is longer
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq

    return longest_seq

# Example usage
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(nums)

# Print the sequence
print("Longest Consecutive Sequence:", result)
