shopping_list = ['milk','bread','flower']
for item in shopping_list:
    print(item)
text = 'vision academy tutorial'
count = 0
for item in text :
    if item == 'a':
        count += 1
print(count)
for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)
def compute_power(base,power):
    result = 1
    for i in range(power):
        result*=base
    return result
base = int(input('base : '))
power = int(input('power : '))
print(compute_power(base,power))