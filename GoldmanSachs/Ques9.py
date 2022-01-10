#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        def get_cons_Ds(S, n, ind):
            j, count = ind+1, 0
            while not (j >= n or S[j] != 'D'):
                count, j = count+1, j+1
            return count
        temp = []
        max_reached, last_printed, n = 0, 0, len(S)
        for i, symb in enumerate(S):
            if symb == 'I':
                if i == 0:
                    max_reached = get_cons_Ds(S, n, i) + 2
                    temp.extend([1, max_reached])
                    last_printed = max_reached
                else:
                    max_reached = max_reached+get_cons_Ds(S, n, i) + 1
                    temp.append(max_reached)
                    last_printed = max_reached

            else:
                if i == 0:
                    max_reached = get_cons_Ds(S, n, i) + 2
                    temp.extend([max_reached, max_reached-1])
                    last_printed = max_reached-1
                else:
                    temp.append(last_printed-1)
                    last_printed = last_printed-1

        return "".join([str(item) for item in temp])

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends