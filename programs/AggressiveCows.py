def aggressiveCows(stalls, k):
    stalls.sort()  # Sort the stall positions
    low = 1  # Minimum possible distance between cows (at least 1 unit apart)
    high = stalls[-1] - stalls[0]  # Maximum possible distance between the first and last stall
    result = 0  # Variable to store the largest minimum distance found
    
    # Perform binary search on the possible distances
    while low <= high:
        mid = (low + high) // 2  # Middle value for the current search range
        if is_feasible(stalls, k, mid):  # Check if it's possible to place cows with 'mid' distance
            result = mid  # If feasible, update result
            low = mid + 1  # Try to increase the distance
        else:
            high = mid - 1  # Otherwise, try a smaller distance
    
    return result

def is_feasible(stalls, k, min_dist):
    last = stalls[0]  # Place the first cow at the first stall
    count = 1  # We have placed one cow already
    
    for i in range(1, len(stalls)):  # Start from the second stall
        # If the current stall is far enough from the last placed cow
        if stalls[i] - last >= min_dist:
            count += 1  # Place a cow in the current stall
            last = stalls[i]  # Update the position of the last placed cow
            if count == k:  # If we've placed all cows, return True
                return True
    
    return False  # If not all cows could be placed, return False


stalls = [1, 2, 4, 8, 9]
k = 3
print(aggressiveCows(stalls,k))