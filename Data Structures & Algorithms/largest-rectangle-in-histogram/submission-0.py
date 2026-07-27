class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result=[]

        #Take all unique heights in sorted order 
        unique_heights=sorted(set(heights))

        # check every possible minimum height
        for h in unique_heights:

            width=0

            for num in heights:
                if num>h:
                    width+1

                else:
                    if width>0:
                        result.append(h*width)
                    width=0

            if width>0:
                result.append(h*width)              

        for num in heights:
            result.append(num)          

        return max(result)    