def calculate_total_distance_from_file(file_path):
    left_list = []
    right_list = []
    
    # Read the file and parse the numbers
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

# Example usage
file_path = "dayone.txt"
result = calculate_total_distance_from_file(file_path)
print(f"Total distance: {result}")