class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []

        if left < 10 and right > 11:
            res.extend(range(left,10))

            for i in range(11,right + 1):

                if "0" in str(i):
                    pass

                elif all(( i % int(val) == 0 for val in str(i))):
                    res.append(i)

        else:

            for i in range(left,right + 1):

                if "0" in str(i):
                    pass

                elif all(( i % int(val) == 0 for val in str(i))):
                    res.append(i)

        return res
        
