def is_safe(numbers):
    """Check if a sequence is safe."""
    direction = None 
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff == 0 or abs(diff) > 3:
            return False
        if direction is None: 
            direction = "increasing" if diff > 0 else "decreasing"
        elif (direction == "increasing" and diff < 0) or (direction == "decreasing" and diff > 0):
            return False
    return True


def classify_lines_with_removal(file_path):

    safe_count = 0


    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            numbers = list(map(int, line.split()))

            # Check if the sequence is already safe
            if is_safe(numbers):
                safe_count += 1
                print(f"{line.strip()}: Safe (original)")
                continue

          
            safe_with_removal = False
            for i in range(len(numbers)):
                # Remove the i-th element and test the remaining sequence
                modified_numbers = numbers[:i] + numbers[i + 1:]
                if is_safe(modified_numbers):
                    safe_with_removal = True
                    break

            if safe_with_removal:
                safe_count += 1

    print(f"\nTotal Safe: {safe_count}")
    
classify_lines_with_removal('day2input.txt')
