import sys

# Monotonic stack algorithm
def find_largest_subsequence(bank_string, target_length=12):
    """
    Finds the subsequence of length `target_length` that forms the 
    largest possible number using a Monotonic Stack approach.
    """
    n = len(bank_string)
    
    # If the bank has fewer digits than required, it can't contribute.
    if n < target_length:
        return 0
    
    # Calculate how many digits we are allowed to 'delete' to find the max.
    # e.g., if string is 15 chars and we want 12, we can delete 3 chars.
    digits_to_remove = n - target_length
    
    stack = []
    
    for digit in bank_string:
        # While we still have quotas to remove digits, 
        # and the current digit is bigger than the last one we kept,
        # we discard the last one to make room for this bigger one.
        while digits_to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            digits_to_remove -= 1
        
        stack.append(digit)
    
    # If we didn't remove enough (e.g., the digits were already in descending order),
    # we truncate the end to fit the target length.
    result_string = "".join(stack[:target_length])
    
    return int(result_string)

def p2():
    if len(sys.argv) < 2:
        print("Usage: python battery_quest_part2.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    total_output_joltage = 0

    try:
        with open(input_filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                # Calculate max for this bank
                bank_val = find_largest_subsequence(clean_line, 12)
                total_output_joltage += bank_val

        print(f"Total output joltage: {total_output_joltage}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-digit characters.")

if __name__ == "__main__":
    p2()
