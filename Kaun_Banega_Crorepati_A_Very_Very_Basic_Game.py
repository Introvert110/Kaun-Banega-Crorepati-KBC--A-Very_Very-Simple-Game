# print("Press 1 - to start the game: ", )
questions = ["Que1. Who was the first Prime Minister of India?", "Que2. Which one is the larget state in India",
             "Que3. How many states are there in India", "Que4. What is the capital of India?", "Que5. What is the highest mountain in the world?","Que6. What is the national animal of India?" ]
que1_option = ["A- Mahatma Gandhi", "B- Jawaharlal Nehru", "C- Subhash Chandra Bose", "D- Sardar Valabhbhai Patel"]
que2_option = ["A- Rajasthan", "B- Tamil Nadu", "C- Delhi", "D- Assam"]
que3_option = ["A- 27", "B- 28", "C- 20", "D- 15"]
que4_option = ["A- Mumbai", "B- Chennai", "C- Kolkata", "D- New Delhi"]
que5_option = ["A- K2","B- Lhotse", "C- Mount Everest", "D- Annapurna"]
que6_option = ["A- Tiger", "B- Elephant", "C- Lion", "D- Rhinoceros"]

# questions = [
#     {
#         "question": "What is the capital of India?",
#         "correct_answer": "New Delhi",
#         "incorrect_answers": ["Mumbai", "Chennai", "Kolkata"]
#     },
#     {
#         "question": "What is the highest mountain in the world?",
#         "correct_answer": "Mount Everest",
#         "incorrect_answers": ["K2", "Lhotse", "Annapurna"]
#     },
#     {
#         "question": "What is the national animal of India?",
#         "correct_answer": "Tiger",
#         "incorrect_answers": ["Elephant", "Lion", "Rhinoceros"]
#     }
# ]

while True:
    print(questions[0])
    print(que1_option)
    que1 = input(("Enter the option(A, B, C, D): "))
    if que1 == "B":
        print("Correct Answer - You won Rs.1000")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs. 1000")
    
    print(questions[1])
    print(que2_option)
    que2 = input(("Enter the option(A, B, C, D): "))
    if que2 == "A":
        print("Correct Answer - You won Rs.1500")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs. 2500")
    
    print(questions[2])
    print(que3_option)
    que3 = input(("Enter the option(A, B, C, D): "))
    if que3 == "B":
        print("Correct Answer - You won Rs.2000")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs. 4500")
    
    print(questions[3])
    print(que4_option)
    que4 = input(("Enter the option(A, B, C, D): "))
    if que4 == "D":
        print("Correct Answer - You won Rs.2500")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs. 7000")
    
    print(questions[4])
    print(que5_option)
    que5 = input(("Enter the option(A, B, C, D): "))
    if que5 == "C":
        print("Correct Answer - You won Rs.3000")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs. 10000")
    
    print(questions[5])
    print(que6_option)
    que6 = input(("Enter the option(A, B, C, D): "))
    if que6 == "A":
        print("Correct Answer - You won Rs.5000")
    else:
        print("Incorrect Answer - You Lose")
        break
    print("Total Money Won: Rs.15000")