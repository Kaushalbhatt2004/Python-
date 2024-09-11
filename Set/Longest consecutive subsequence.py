def longest_consecutive(nums):
    # Convert the list to a set for O(1) lookup time
    num_set = set(nums)
    longest_streak = 0

    # Iterate through the numbers
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4 (sequence: 1, 2, 3, 4)
