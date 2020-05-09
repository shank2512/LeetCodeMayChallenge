class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return 1
        else:
            x0,y0=coordinates[0]
            x1,y1=coordinates[1]
            for i in range(2,len(coordinates)):
                x,y=coordinates[i]
                if (y1-y0)*(x-x0)!=(x1-x0)*(y-y0):
                    return 0
            return 1
                
        