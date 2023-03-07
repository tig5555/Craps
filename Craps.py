import random

number1 = random.randrange(1, 7)
number2 = random.randrange(1, 7)
total_sum = number1 + number2
user_input = input(f"The total_sum of dice is {number1} + {number2} = {total_sum}")



if total_sum in (7, 11):
    print("You win")

elif total_sum in (2, 3, 12):
    print("You lose")

else:
    result = "continue your game please"
    goal = total_sum
    print("Now your goal number is: ", goal)

    while result == "continue your game please":

        number1 = random.randrange(1, 7)
        number2 = random.randrange(1, 7)
        total_sum = number1 + number2
        user_input = input(f"The total_sum of dice is {number1} + {number2} = {total_sum}")

        if total_sum == goal:
            print("You win")
            break

        elif total_sum == 7:
            print("You lose")
            break
