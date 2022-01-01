# Question: Print Anagrams Together

#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        
        dict = {}
        for word in words:
            sortedWord = "".join(sorted(word))
            if sortedWord not in dict:
                dict[sortedWord] = [word]
            else:
                dict[sortedWord].append(word)
            
        res = []
        for i in dict.values():
            res.append(i)
            
        return res
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
