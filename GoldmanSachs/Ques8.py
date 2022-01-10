# I don't know why TLE is giving for this question in gfg

#User function Template for python3

class Solution:
    def CountWays(self, str):
        # Code here
        mod = 1e9 + 7
        n = len(str)
        if str[0]=='0':
            return 0
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            if str[i-1]>'0':
                dp[i] = dp[i-1]
        
            if str[i-2]=='1' or (str[i-2]=='2' and str[i-1]<'7'):
                dp[i] += dp[i-2]
    
        return int(dp[n]%mod)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.CountWays(str)
        print(ans)

# } Driver Code Ends