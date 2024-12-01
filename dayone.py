from collections import Counter

def read_lists_from_file(file_path):
    """
    Reads a file and splits numbers into two lists: left_list and right_list.
    """
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score between two lists.
    """
    right_counts = Counter(right_list)
    similarity_score = sum(num * right_counts[num] for num in left_list)
    return similarity_score

def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists after sorting.
    """
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

# Main logic
file_path = "dayone.txt"  # Replace with your actual file path

# Load the data once
left_list, right_list = read_lists_from_file(file_path)

# Calculate both metrics
similarity_score = calculate_similarity_score(left_list, right_list)
total_distance = calculate_total_distance(left_list, right_list)

# Print results
print(f"Similarity score: {similarity_score}")
print(f"Total distance: {total_distance}")