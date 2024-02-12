import random
import time

#fact dictionary
fakts = {
    "Which animal is considered the symbol of Australia?": "Kangaroo",
    "Which language family is predominant in China?": "Sino-Tibetan",
    "Which gas is the most abundant gas in the Earth's atmosphere?": "Nitrogen",
    "What is the capital of Switzerland?": "Bern",
    "Which ocean washes the east coast of Australia?": "Pacific Ocean",
    "Which planet is considered the closest planet to the Sun?": "Mercury",
    "Which animal is the national symbol of Russia?": "Bear",
    "Which country is the largest country by area in the world?": "Russia",
    "Who wrote the novel 'Crime and Punishment'?": "Fyodor Dostoevsky",
    "What substance gives plants their green color?": "Chlorophyll"
}

right = 0
wrong = 0


start_time = time.time()
#user interaction
user_input = input("Shall we take the quiz? (Yes/No)")
if user_input.lower() == "yes" or user_input == "y":
    print("let's go")
else:
    print("so bad")
    exit()

#Check if the user's answer matches the correct answer 
while fakts:
    random_key = random.choice(list(fakts.keys()))
    print(random_key)
    user_answer = input("Enter your answer: ")
    correct_answer = fakts[random_key]

    if user_answer.lower() == correct_answer.lower():
        print("That's right!")
        right += 1
    else:
        print("Wrong.")
        wrong += 1

    del fakts[random_key]

#time counting
end_time = time.time()
execution_time = end_time - start_time

#user information
print("The quiz is over. All questions answered!")
print(f"You answered correctly to {right} and it's not right on {wrong} questions.")
print(f"Time spent {execution_time} seconds")