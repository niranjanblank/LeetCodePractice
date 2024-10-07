"""
744. Find Smallest Letter Greater Than Target
Solved
Easy
Topics
Companies
Hint
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.



Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
"""


class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if target == letters[mid] and mid + 1 < len(letters) and letters[mid + 1] != letters[mid]:
                return letters[mid + 1]
            elif target < letters[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if right + 1 < len(letters) and letters[right + 1] > target:
            return letters[right + 1]

        return letters[0]


class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(letters) - 1
        mid = 0  # Midpoint variable, initialized to 0 (not necessary but for clarity)

        # Binary search loop: run until left pointer exceeds right pointer
        while left <= right:
            # Calculate the midpoint
            mid = (left + right) // 2

            # If target is less than the letter at mid, search in the left half
            if target < letters[mid]:
                right = mid - 1
            # Otherwise, search in the right half
            else:
                left = mid + 1

        # After binary search is done, left points to the smallest letter greater than target
        # If no such letter exists (i.e., left exceeds bounds), wrap around using % operator
        return letters[left % len(letters)]