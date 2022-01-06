#Your task is to complete this function
#Function should return complete string
def encode(arr):
    
    # Code here
    
    encoding = []
    n = len(arr)
    i, j = 0, 0
    while not (i >= n or j >= n):
        j = i
        count = 0
        while not (j >= n or arr[j] != arr[i]):
            count, j = count+1, j+1
        encoding.append(arr[i])
        encoding.append(str(count))
        i = j
    return "".join(encoding)

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends