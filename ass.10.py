def findDigits(N):
 
    if N == 1:
        return 1
 
    # Changing number to string
    s = str(N)
 
    # Add length of number to total_sum 
    return len(s) + findDigits(N - 1)
 
# Driver Code
 
# Given N
N = 13
 
# Function call 
print(findDigits(N))