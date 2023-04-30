from char_frequency_counter import char_frequency_counter

if __name__ == "__main__":
    input_string = input("Enter String to Count character : \n")
    freq = char_frequency_counter(input_string)

# Print the frequency count for each character
    for char, count in freq.items():
        print(f"{count} {char}'s")