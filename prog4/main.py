from collections import Counter

def find_first_odd_flavor(N, C):
    # Count the occurrences of each flavor using Counter
    flavor_counts = Counter(C)

    # Iterate through the candy list to find the first flavor with odd count
    for flavor in C:
        if flavor_counts[flavor] % 2 == 1:
            return f'{flavor} -> "{flavor}" flavor appears an odd number of times.'

    # If no flavor appears an odd number of times
    return "All are even"

# Read the input values
N = int(input())  # Accepting the integer N
C = [input().strip() for _ in range(N)]  # Accepting the list of flavors

# Get the result and print
result = find_first_odd_flavor(N, C)
print(result)
