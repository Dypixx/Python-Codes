def quiz_app():
    print("Let’s see how much you know about India. Ready? Let’s go!\n")

    questions = [
        {
            "question": "What is the capital city of India?",
            "options": ["A) New Delhi", "B) Mumbai", "C) Bengaluru", "D) Kolkata"],
            "answer": "A",
        },
        {
            "question": "Which is the largest state in India by area?",
            "options": ["A) Uttar Pradesh", "B) Madhya Pradesh", "C) Rajasthan", "D) Maharashtra"],
            "answer": "C",
        },
        {
            "question": "Who is known as the father of the Nation in India?",
            "options": ["A) Jawaharlal Nehru", "B) Subhas Chandra Bose", "C) Mahatma Gandhi", "D) Sardar Patel"],
            "answer": "C",
        },
        {
            "question": "Which is the longest river in India?",
            "options": ["A) Yamuna", "B) Ganga", "C) Brahmaputra", "D) Godavari"],
            "answer": "B",
        },
        {
            "question": "Which festival is known as the Festival of Lights?",
            "options": ["A) Holi", "B) Diwali", "C) Eid", "D) Christmas"],
            "answer": "B",
        },
        {
            "question": "In which year did India gain independence?",
            "options": ["A) 1942", "B) 1947", "C) 1950", "D) 1960"],
            "answer": "B",
        },
        {
            "question": "Which city is known as the 'Silicon Valley of India'?",
            "options": ["A) New Delhi", "B) Chennai", "C) Bengaluru", "D) Hyderabad"],
            "answer": "C",
        },
        {
            "question": "Who was the first President of India?",
            "options": ["A) Dr. Rajendra Prasad", "B) Dr. S. Radhakrishnan", "C) Jawaharlal Nehru", "D) Dr. A.P.J. Abdul Kalam"],
            "answer": "A",
        },
        {
            "question": "Which is the national flower of India?",
            "options": ["A) Rose", "B) Lotus", "C) Sunflower", "D) Tulip"],
            "answer": "B",
        },
        {
            "question": "Which is the largest city in India by population?",
            "options": ["A) New Delhi", "B) Mumbai", "C) Bengaluru", "D) Kolkata"],
            "answer": "B",
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Awesome! That’s correct!\n")
            score += 1
        else:
            print(f"Oops! The correct answer was {q['answer']}.\n")

    print(f"Well done! Your final score is {score}/{len(questions)}.")
    
    if score == len(questions):
        print("You’re a quiz master! Fantastic job!")
    elif score > len(questions) // 2:
        print("Good job! You know your stuff pretty well!")
    else:
        print("No worries, better luck next time! Keep practicing!")

quiz_app()
