# The following iterative sequence is defined for the set of positive
# integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
# sequence:

#                 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def get_next_collatz_number(n):
    """
    Get the next number in the Collatz sequence.
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    """
    if is_even(n):
        return n // 2
    else:
        return 3 * n + 1

def generate_collatz_path(n):
    """
    Generate the path of numbers in a Collatz sequence until we hit 1
    or a number we've seen before.
    Returns the path as a list.
    """
    path = []
    while n != 1:
        path.append(n)
        n = get_next_collatz_number(n)
    return path

def store_path_lengths_in_memo(path, memo, base_length):
    """
    Store the chain lengths for all numbers in the path using memoization.
    Works backwards through the path to calculate and store lengths.
    """
    current_length = base_length
    for i in range(len(path) - 1, -1, -1):
        current_length += 1
        memo[path[i]] = current_length

def get_collatz_length_from_memo(n, memo):
    """
    Get the Collatz chain length for a number, checking memo first.
    If not in memo, calculate it and store intermediate results.
    """
    if n in memo:
        return memo[n]

    original_n = n
    path = []

    # Follow the sequence until we hit a known value or reach 1
    while n != 1 and n not in memo:
        path.append(n)
        n = get_next_collatz_number(n)

    # Determine the base length from where we stopped
    if n == 1:
        base_length = 1
    else:
        base_length = memo[n]

    # Store lengths for all numbers in the path
    store_path_lengths_in_memo(path, memo, base_length)

    return memo[original_n]

def collatz_length(n, memo=None):
    """
    Calculate the length of the Collatz sequence starting from n.
    Uses memoization to avoid recalculating known sequences.
    """
    if memo is None:
        memo = {}

    # Handle the base case
    if n == 1:
        return 1

    return get_collatz_length_from_memo(n, memo)

# def print_progress(current, max_so_far, length_so_far, interval=100000):
#     """Print progress updates during the search."""
#     if current % interval == 0:
#         print(f"Checked up to {current}, current max: {max_so_far} with length {length_so_far}")

def update_max_if_longer(current_num, current_length, max_num, max_length):
    """
    Update the maximum length and corresponding number if current is longer.
    Returns (new_max_num, new_max_length).
    """
    if current_length > max_length:
        return current_num, current_length
    return max_num, max_length

def find_longest_collatz_chain(limit):
    """
    Find the starting number under 'limit' that produces the longest Collatz chain.
    Returns (number_with_max_length, max_length).
    """
    memo = {}
    max_length = 0
    number_with_max_length = 0

    for i in range(1, limit):
        length = collatz_length(i, memo)
        number_with_max_length, max_length = update_max_if_longer(
            i, length, number_with_max_length, max_length
        )
     #   print_progress(i, number_with_max_length, max_length)

    return number_with_max_length, max_length

# def test_example():
#     """Test with the example from the problem statement."""
#     test_length = collatz_length(13)
#     print(f"Length of Collatz sequence starting at 13: {test_length}")
#     return test_length == 10

# def solve_small_example():
#     """Solve for a smaller range as a test."""
#     print("Finding the longest Collatz chain under 100...")
#     result_number, result_length = find_longest_collatz_chain(100)
#     print(f"The number under 100 with the longest Collatz chain is: {result_number}")
#     print(f"Its chain length is: {result_length}")
#     return result_number, result_length

def solve_full_problem():
    """Solve the full problem for numbers under one million."""
    result_number, result_length = find_longest_collatz_chain(1000000)
    print(f"The number under 1,000,000 with the longest Collatz chain is: {result_number}")
    print(f"Its chain length is: {result_length}")
    return result_number, result_length

def main():
    """Main function to run all tests and solve the problem."""
    # Verify the example works
    # if test_example():
    #     print("✓ Example test passed!")
    # else:
    #     print("✗ Example test failed!")
    #     return

    # # Test with smaller range
    # solve_small_example()




    # Solve the full problem
    start = time.time()
    solve_full_problem()
    elapsed = (time.time() - start)
    print(str(elapsed) + " seconds")


if __name__ == "__main__":
    main()
