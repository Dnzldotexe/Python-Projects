def compress(s):
    if not s:
        return []
    
    compressed_str = []
    current_char = s[0]
    counter = 1
    
    for char in s[1:]:
        if char == current_char:
            counter += 1
        else:
            # Add the character and its count
            compressed_str.append(current_char)
            compressed_str.append(counter)
            
            # Reset for new character
            current_char = char
            counter = 1
    
    # Add the last character and its count
    compressed_str.append(current_char)
    compressed_str.append(counter)
    
    return compressed_str

# Test cases
print(compress("aaaabbb1111cccdd"))
print(compress(""))  # Empty string
print(compress("a"))  # Single character
print(compress("abcd"))  # No repeated characters