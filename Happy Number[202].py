class Solution(object):
    def isHappy(self, n):
        def toDigit(n):
            toStr=list(str(n))
            digits=[]
            for i in range(len(toStr)):
                digits.append(int(toStr[i]))
            return digits
        def squaring(digits):
            sum=0
            for num in digits:
                sum+=num**2
            return sum
        if(n<0):
            return False
        lst=list()
        while n not in lst:
            lst.append(n)
            if(n==1):
                return True
            n=squaring(toDigit(n))
        return False
    
        """
        :type n: int
        :rtype: bool
        """
        
