#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        
        #Code here

        subarrays = 0
        i, j = 0, 0
        product = 1
        while j < n:
            product *= a[j]
            while not (i > j or product < k):
                product /= a[i]
                i += 1
            subarrays += j-i+1
            j += 1
        return subarrays
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends