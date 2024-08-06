# Example usage
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
value_to_remove = 2
original_dict = {key: value for key, value in original_dict.items()
                if value != value_to_remove}

print(original_dict)

# Output: {'a': 1, 'c': 3}