"""
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

# def compress(chars):
#     if not chars:
#         return []
#
#     out = []
#     current_letter = chars[0]
#     current_letter_count = 0
#
#     for item in chars:
#         if item == current_letter:
#             current_letter_count += 1
#         else:
#             out.append(current_letter)
#             if current_letter_count > 1:
#                 out.extend(str(current_letter_count))
#             current_letter = item
#             current_letter_count = 1
#
#     # Append the last character and its count
#     out.append(current_letter)
#     if current_letter_count > 1:
#         out.extend(str(current_letter_count))
#
#     return out

# solution 2
def compress(chars):
    if not chars:
        return 0

    read = 0
    write = 0

    while read < len(chars):
        char = chars[read]
        count = 0

        # counting number of occurences
        while read < len(chars) and chars[read] == char:
            read+=1
            count+=1

        chars[write]=char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write +=1
    print(chars)
    return write
print(compress(["a", "a", "b", "b", "c", "c", "c","c","c"]))