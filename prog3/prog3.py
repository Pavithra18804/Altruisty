from collections import deque

def min_of_max_in_subarrays(arr, n, k):
    # List to store maximums of each subarray of size k
    max_in_subarrays = []
    # Deque to store indexes of useful elements in each window of size k
    dq = deque()
    
    for i in range(n):
        # Remove elements that are out of this window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove all elements in the deque that are less than the current element
        # (we only need the maximum elements)
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        # Add current element at the rear of the deque
        dq.append(i)
        
        # Append the maximum of the current window to the result list
        # We start adding to the list after we've processed the first window
        if i >= k - 1:
            max_in_subarrays.append(arr[dq[0]])
    
    # Find and return the minimum of all maximums
    return min(max_in_subarrays)

# Sample Input
k = 2
n = 6
arr = [3, 1, 4, 1, 5, 9]

# Expected Output: 4
print(min_of_max_in_subarrays(arr, n, k))  # Expected output: 4
