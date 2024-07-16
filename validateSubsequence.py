def isValidSubsequence(array, sequence):
   seqIndex = 0
   for value in array:
       if sequence[seqIndex] == value:
           seqIndex += 1
       if seqIndex == len(sequence):
           break
   return seqIndex == len(sequence)
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [4, 5, 1, 22, 25, 6, -1, 8, 10]))