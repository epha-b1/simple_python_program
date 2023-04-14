def char_frequency_counter(string):

    # Initialize an empty dictionary to store the frequency count of each character
    frequency = {}

    # Iterate through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count by 1
        if char in frequency:
            frequency[char] += 1
        # If the character is not yet in the dictionary, add it with a count of 1
        else:
            frequency[char] = 1

    # Return the dictionary of frequency counts
    return frequency
if __name__ == "__main__":
    input_string = input("Enter String to Count character : \n")
    freq = char_frequency_counter(input_string)

# Print the frequency count for each character
    for char, count in freq.items():
        print(f"{count} {char}'s")

