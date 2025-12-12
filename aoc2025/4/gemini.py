import sys

def parse_input(filename):
    """
    Reads the input file and returns a set of (row, col) tuples
    representing the locations of paper rolls ('@').
    """
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    rolls = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '@':
                rolls.add((r, c))
    return rolls

def count_neighbors(r, c, current_rolls):
    """
    Counts how many paper rolls exist in the 8 adjacent positions
    around (r, c).
    """
    count = 0
    # Iterate through all 8 distinct adjacent directions
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            
            neighbor = (r + dr, c + dc)
            if neighbor in current_rolls:
                count += 1
    return count

def get_accessible_rolls(current_rolls):
    """
    Identifies all rolls that are currently accessible.
    A roll is accessible if it has fewer than 4 neighbors.
    """
    accessible = set()
    for r, c in current_rolls:
        neighbors = count_neighbors(r, c, current_rolls)
        if neighbors < 4:
            accessible.add((r, c))
    return accessible

def solve():
    if len(sys.argv) < 2:
        print("Usage: python solution.py <input_file>")
        return

    input_file = sys.argv[1]
    
    # --- Part 1 ---
    # Determine accessible rolls in the initial configuration
    initial_rolls = parse_input(input_file)
    accessible_p1 = get_accessible_rolls(initial_rolls)
    
    print(f"Part 1 Output: {len(accessible_p1)}")

    # --- Part 2 ---
    # Simulate the removal process until no more rolls can be removed
    current_rolls = initial_rolls.copy()
    total_removed_count = 0
    
    while True:
        # Find rolls to remove in this step
        to_remove = get_accessible_rolls(current_rolls)
        
        # If no rolls can be removed, we are done
        if not to_remove:
            break
            
        # Update the total count
        count = len(to_remove)
        total_removed_count += count
        
        # Remove the rolls from the grid (update state)
        current_rolls -= to_remove
        
        # (Optional) Debug print to watch progress
        # print(f"Step removed: {count}, Remaining: {len(current_rolls)}")

    print(f"Part 2 Output: {total_removed_count}")

if __name__ == "__main__":
    solve()