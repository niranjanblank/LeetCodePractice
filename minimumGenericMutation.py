"""
433. Minimum Genetic Mutation
Solved
Medium
Topics
Companies
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Time Complexity: O(N) , N is the size of the bank
        # Space Complexity: O(N)
        queue = deque()

        # add the start gene to the queue
        queue.append(startGene)

        bank = set(bank)
        
        steps = 0

        # used to mark if the gene is already visited 
        visited = set()

        while queue:

            for _ in range(len(queue)):
                gene = queue.popleft()

                if gene == endGene:
                    return steps
                visited.add(gene)
                # generating all the genes from gene and adding the valid ones to the queue

                # the gene generation has time complexity of O(32) as for each charrarcter in the gene there 
                # are 4 possible replacements leading to 8x4= 32 pootential mutations per gene
                for c in "ACGT":
                    for i in range(len(gene)):
                        temp_gene = gene[:i] + c + gene[i+1:]
                        if temp_gene not in visited  and temp_gene in bank:
                            queue.append(temp_gene)

            steps+=1

        return -1
