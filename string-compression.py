def compress(s):
    if not s:
        return []
    index = 0
    counter = 1
    str_length = len(s)
    compressed_str = []
    current_char = s[index]
    # loop over all the characters in the string
    while index+1 < str_length:
        if current_char != s[index+1]:
            # add character 
            compressed_str.append(current_char)
            # add count
            compressed_str.append(counter) 
            # change the character to the current character
            current_char = s[index+1]
            # reset the counter
            counter = 0

        counter += 1
        index += 1

    compressed_str.append(current_char)
    compressed_str.append(counter) 
    # return compressed string
    return compressed_str

# Test cases
print(compress("aaaabbb1111cccdd"))
print(compress(""))  # Empty string
print(compress("a"))  # Single character
print(compress("abcda"))  # No repeated characters


# def compress(s):
#     if not s:
#         return []
    
#     compressed_str = []
#     current_char = s[0]
#     counter = 1
    
#     for char in s[1:]:
#         if char == current_char:
#             counter += 1
#         else:
#             # Add the character and its count
#             compressed_str.append(current_char)
#             compressed_str.append(counter)
            
#             # Reset for new character
#             current_char = char
#             counter = 1
    
#     # Add the last character and its count
#     compressed_str.append(current_char)
#     compressed_str.append(counter)
    
#     return compressed_str

# # Test cases
# print(compress("aaaabbb1111cccdd"))
# print(compress(""))  # Empty string
# print(compress("a"))  # Single character
# print(compress("abcda"))  # No repeated characters
