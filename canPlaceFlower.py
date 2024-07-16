def canPlaceFlowers( flowerbed, n):
    flowerbed = [0]+flowerbed+[0]
    flowersPlaced = 0
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
            flowerbed[i]=1
            flowersPlaced+=1

        if flowersPlaced == n:
            return True
    return False

print(canPlaceFlowers([1,0,0,0,1],0))