import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 15

def generate_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = f"{left} {operator} {right}"
    answer = eval(exp)

    return exp, answer

wrong = 0
print("Press enter to start!")
TOTAL_PROBLEMS = int(input("how many problems do you want to solve? "))
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_question()
    while True:
        guess = input(f"problem #{str(i + 1)}: {exp} = ? ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
time_taken = end_time - start_time
print("\nNice Work!")
print(f"Time taken: {time_taken:.2f} seconds")
print("----------------------")