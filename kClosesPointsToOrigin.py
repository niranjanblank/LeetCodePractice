"""
K Closest Points to Origin
"""

class Solution1:
    """
    Time Cmplexity
    Building the Heap
        Inserting n elements into a list: O(n)
    Extracting k closes points
        Each heapop operartion is O(logn)
        Performing k time would be O(logn)
    Total Complexity: O(n) + O(klogn) = O(n+klogn)
    Better method as it is closer to linear time

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            # calc distance
            distance_to_origin = x**2 + y**2
            heap.append((distance_to_origin,x,y))
        # create a heap out of it
        heapq.heapify(heap)

        # to get k closest values, pop the heap k times and store the result
        result = []
        for i in range(k):
            item = heapq.heappop(heap)
            result.append([item[1],item[2]])
        return result


class Solution2:
    """
    Time complexity
    Sorting the list : O(nlogn)
    Selecting the first k elements O(k)
    Overall Compexity: O(nlogn)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort based on dist
        sorted_points = sorted(points, key=lambda item: item[0]**2+item[1]**2)
        return sorted_points[:k]