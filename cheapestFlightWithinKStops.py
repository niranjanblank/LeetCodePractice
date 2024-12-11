class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Using both prices and tmpPrices ensures that updates in the current iteration do not interfere with other updates. If we use only prices, a single update during an iteration might affect other updates in the same iteration, leading to incorrect results
        '''
        # initially setting all the prices to earch dst to be inf
        prices = [float("inf")]*n
        # since we start from the source, the price to reach the source is 0.
        prices[src] = 0
        
          # perform the Bellman-Ford-like relaxation process for k+1 iterations.
        # we need at most k stops between src and dst, so we run the loop k+1 times
        # e.g if we need a path from a->c and have a->b->c, this is valid because the number of nodes betweeen
        # a and c is 1
        for i in range(k+1):
            # create a temporary prices array to store updated prices for this iteration.
            # this ensures we only use prices from the previous iteration when updating.
            tmpPrices = prices.copy()
            # going through all the prices
            for s,d,p in flights:
                # skip s, if s is unreachable from previous iteration
                if prices[s] == float('inf'):
                    continue
                # check if the price to reach d can be minimized
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
