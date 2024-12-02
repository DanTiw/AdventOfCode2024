def classify_lines(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines: #each line
            numbers = list(map(int, line.split()))
            is_safe = True  
            direction = None  
            for i in range(len(numbers) - 1): #each number
                diff = numbers[i + 1] - numbers[i] #difference can be negative or positive
                if diff == 0: #dont need 0
                    is_safe = False
                    break
                elif abs(diff) > 3: #1,2,3
                  
                    is_safe = False
                    break
                elif direction is None: #first check only for first iteration
                    
                    direction = "increasing" if diff > 0 else "decreasing"
                elif (direction == "increasing" and diff < 0) or (direction == "decreasing" and diff > 0): #nice
                    is_safe = False
                    break
            
            if is_safe:
                safe_count += 1
    print(f"\nTotal Safe: {safe_count}")

classify_lines('day2input.txt')
