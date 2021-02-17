def findDigits(N):
 
    if N == 1:
        return 1
 
   
    s = str(N)
 
    # Add length of number to total_sum 
    return len(s) + findDigits(N - 1)
 

N = 13
 

print(findDigits(N))
