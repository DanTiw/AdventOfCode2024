first_numbers = []
second_numbers = []

with open('day1Input.txt', 'r') as file:

    for line in file:
        numbers = line.strip().split()
        first_numbers.append(int(numbers[0]))
        second_numbers.append(int(numbers[1]))

first_numbers.sort()
second_numbers.sort()

res=0
total=0
for i in range(1000):
   
    if first_numbers[i]>=second_numbers[i]:
        res=first_numbers[i]-second_numbers[i]
    else:
        res=second_numbers[i]-first_numbers[i]
    total=res+total

print(total)