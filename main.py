import random

while True:
    num_letters = int(input("Enter the number of letters: "))
    num_strings = int(input("Enter the number of strings to generate: "))

    for _ in range(num_strings):
        letters = random.choices('abcdefghijklmnopqrstuvwxyz', k=num_letters)
        sequence = ''.join(letters)
        print(sequence)

    repeat = input("Do you want to generate more letter sequences? (yes/no): ")
    if repeat.lower() != 'y' and repeat.lower() != 'yes':
        break
