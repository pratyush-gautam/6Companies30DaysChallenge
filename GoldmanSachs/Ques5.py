#User function Template for python3
class Solution:
    def getNthUglyNo(self,n):
        
        # code here
        
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        i = 1
        while i < n:
            next_val = min(2*ugly[i2], 3*ugly[i3], 5*ugly[i5])
            
            if next_val == 2*ugly[i2]:
                i2 += 1
            elif next_val == 3*ugly[i3]:
                i3 += 1
            else:
                i5 += 1
            if ugly[i-1] != next_val:
                ugly.append(next_val)
                i += 1
        return ugly[i-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends