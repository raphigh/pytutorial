i = 1
while i < 6:
    print(i)
    i += 1
print('the program is finished')
answer = input('player 1 pleasse insert the number : ')
answer = int(answer)
correct = False
count = 0
while count < 10 and correct == False:
    guess = int(input('player 2 please insert number : '))
    if guess == answer:
        print('player 2 you won')
    elif guess > answer:
        print('your guess is greater than answer')
        count += 1
    else:
        print('your answer is less than answer')
        count += 1
if correct == False:
    print('you lose')