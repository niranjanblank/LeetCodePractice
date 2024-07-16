"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

def encode(strs):
    # Initialize an empty string to hold the encoded result.
    encoded_string = ""
    # Loop through each string in the input list of strings.
    for item in strs:
        # For each string, append its length followed by '#' and then the string itself.
        encoded_string += f'{len(item)}#{item}'
    # Return the fully encoded string.
    return encoded_string

def decode(s):
    # Initialize a list to collect the decoded strings.
    decoded_list = []
    # Variable to temporarily store the number of characters (as string) in the next word to decode.
    code = ""
    # Index to track our position in the encoded string.
    i = 0
    # Process the entire encoded string.
    while i < len(s):
        # Check if the current character is not '#'.
        if s[i] != "#":
            # Accumulate the digits in 'code' which represent the length of the next word.
            code += s[i]
            i += 1
        else:
            # Once '#' is found, calculate the start index of the actual word.
            start = i + 1
            # Convert the accumulated digits into an integer to get the word length.
            word_length = int(code)
            # Calculate the end index of the word.
            end = start + word_length
            # Extract the word and add to the list of decoded strings.
            word = s[start:end]
            decoded_list.append(word)
            # Reset the 'code' for the next iteration.
            code = ""
            # Move the index to the end of the current word.
            i = end
    # Return the list of decoded strings.
    return decoded_list


encoded_string = encode(["we","say",":","yes"])
print(encoded_string)
print(decode(encoded_string))