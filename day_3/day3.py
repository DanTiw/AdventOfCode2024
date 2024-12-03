import re

# Pattern to match mul with two numbers
pattern = r'mul\((\d+),(\d+)\)'

# Example text
with open('day3Input.txt', 'r') as file:
    text = file.read()
    
# Find all matches in the text
matches = re.findall(pattern, text)
total=0
for match in matches:
    res=int(match[0])*int(match[1])
    total=total+res
    
print(total)

