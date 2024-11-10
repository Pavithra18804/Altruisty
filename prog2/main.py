def countBeesBetweenFlowers(s, startIndex, endIndex):
    # Length of the string
    n = len(s)
    
    # Step 1: Create the bee_count array (prefix sum of bees)
    bee_count = [0] * (n + 1)  # bee_count[i] will store number of bees from index 1 to i
    
    for i in range(1, n + 1):
        bee_count[i] = bee_count[i - 1]
        if s[i - 1] == '*':  # If the character at index i-1 is a bee
            bee_count[i] += 1
    
    # Step 2: Answer the queries
    results = []
    for start, end in zip(startIndex, endIndex):
        # The number of bees between start and end (1-indexed)
        # Adjust to 0-based indexing for accessing bee_count
        results.append(bee_count[end] - bee_count[start - 1])
    
    return results

# Sample Input Handling
s = input().strip()  # the line segment with bees and flowers
n_start = int(input())  # the number of elements in startIndex
startIndex = [int(input()) for _ in range(n_start)]  # read all start indices
n_end = int(input())  # the number of elements in endIndex
endIndex = [int(input()) for _ in range(n_end)]  # read all end indices

# Get the result
result = countBeesBetweenFlowers(s, startIndex, endIndex)

# Output the result
for res in result:
    print(res)
