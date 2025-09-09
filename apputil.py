## Exercise 1
# Solution 1
import numpy as np
# Write a function ways(n) which calculates the number of ways you can make change for a given amount of cents n
    # Using coins of denominations 1 cent and 5 cents
    # Function should return the number of ways to yield n cents using only pennies and nickels
# Define ways
def ways(n):
# Define an array using the coins available
    coins = [1, 5, 10, 25]
    # Create a list to store the number of ways to make change for each amount up to n
    ways_to_make_change = [0] * (n + 1)
    # There is one way to make change for 0 cents: use no coins
    ways_to_make_change[0] = 1
    # Loop through each coin
    for coin in coins:
        # Loop through each amount from coin to n
        for amount in range(coin, n + 1):
            # Update the number of ways to make change for the current amount
            ways_to_make_change[amount] += ways_to_make_change[amount - coin]
    # Return the number of ways to make change for n cents
    return ways_to_make_change[n]
    # Test cases
print(ways(0))  # Output: 1 (combination of no coins)
print(ways(3))  # Output: 1 (combinations of pennies)
print(ways(12)) # Output: 4 (combinations of pennies and nickels)
print(ways(20)) # Output: 9 (combinations of pennies and nickels)
print(ways(100)) # Output: 242 (combinations of pennies and nickels)

# Solution 2
import numpy as np
# Write a function ways(n) which calculates the number of ways you can make change for a given amount of cents n
    # Using coins of denominations 1 cent and 5 cents
    # Function should return the number of ways to yield n cents using only pennies and nickels
# Define ways
def ways(n):
# Define an array using the coins available
    coins = [1, 5, 10, 25]
    # Create a list to store the number of ways to make change for each amount up to n
    ways_to_make_change = [0] * (n + 1)
    # There is one way to make change for 0 cents: use no coins
    ways_to_make_change[0] = 1
    # Loop through each coin
    for coin in coins:
        # Loop through each amount from coin to n
        for amount in range(coin, n + 1):
            # Update the number of ways to make change for the current amount
            ways_to_make_change[amount] += ways_to_make_change[amount - coin]
    # Return the number of ways to make change for n cents
    return ways_to_make_change[n]
    # Example of looping through coins
coins = [1, 5, 10, 25]
    # suppose we want to print the pennies and nickels in coins
for coin in coins:
    # we can "skip" values using continue
    if coin > 5:
        continue
    
    # remember what the `%` symbol does
    if coin % 2 > 0:
        f"{coin}"
    
    # `break` completely stops the looping process
    elif coin > 5:
        break
# Test cases
print(ways(0))  # Output: 1 (combination of no coins)
print(ways(3))  # Output: 1 (combinations of pennies)
print(ways(12)) # Output: 4 (combinations of pennies and nickels)
print(ways(20)) # Output: 9 (combinations of pennies and nickels)
print(ways(100)) # Output: 242 (combinations of pennies and nickels)

## Exercise 2
# Solution 1
import numpy as np
# Part 1
# Write a function using NumPy called lowest_score(names, scores) that returns the name of the student with the lowest score
# create two lists, one with names and one with scores
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
# define lowest_score
def lowest_score(names, scores):
    # Convert scores to a NumPy array for easier manipulation
    scores_array = np.array(scores)
    # Find the index of the lowest score
    lowest_index = np.argmin(scores_array)
    # Return the name corresponding to the lowest score
    return names[lowest_index]
# Test cases
print(lowest_score(names, scores))  # Output: 'Mauve' (62 is the lowest score)

# Part 2
# Write a similar function called sort_names(names, scores) that will list the names of students in descending order of test score 
# create two lists, one with names and one with scores
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
# define sort_names
def sort_names(names, scores):
    # Get the indices that would sort the scores array in descending order
    sorted_indices = np.argsort(scores)[::-1]
    # Use these indices to sort the names array accordingly
    sorted_names = names[sorted_indices]
    return sorted_names
# Test cases
print(sort_names(names, scores))  # Output: ['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve']

# Solution 2
import numpy as np
# Part 1
# Write a function using NumPy called lowest_score(names, scores) that returns the name of the student with the lowest score
# create two lists, one with names and one with scores
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
# define lowest_score
def lowest_score(names, scores):
    # Use argmin to find the index of the lowest score
    index = np.argmin(scores)
    # Return the name corresponding to the lowest score from the names list
    return names[index]
# Test cases
print(lowest_score(names, scores))  # Output: 'Mauve' (62 is the lowest score)

# Part 2
# Write a similar function called sort_names(names, scores) that will list the names of students in descending order of test score 
# create two lists, one with names and one with scores
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
# define sort_names
def sort_names(names, scores):
    # Use argsort to get the indices that would sort the scores in descending order
    index = np.argsort(-scores)
    # Return the names sorted by the corresponding scores
    return names[index]
# Test cases
print(sort_names(names, scores))  # Output: ['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve']