import re

with open('day3Input.txt', 'r') as file:
   text = file.read()

   # Pattern to match mul with two numbers, considering do()/don't() states
   pattern = r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))'
   matches = re.findall(pattern, text)
   
   mul_enabled = True
   total = 0
   
   for match in matches:
       if match[0] == 'do()':
           mul_enabled = True
       elif match[0] == 'don\'t()':
           mul_enabled = False
       elif mul_enabled and match[0].startswith('mul('):
           res = int(match[1]) * int(match[2])
           total += res
   
print(total)