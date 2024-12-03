first_numbers = []
second_numbers = []

with open('day1Input.txt', 'r') as file:

    for line in file:
        numbers = line.strip().split()
        first_numbers.append(int(numbers[0]))
        second_numbers.append(int(numbers[1]))
        
freq = {x: second_numbers.count(x) for x in set(second_numbers)}

      
res=0
total=0
for i in range(1000):
    res=first_numbers[i] * freq.get(first_numbers[i], 0)
    total=total+res


print(total)