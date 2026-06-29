score = 0

print("=" * 55)
print("   GENERAL KNOWLEDGE QUIZ — TECH, CODE & MEDICAL")
print("   Powered by DecodeLabs")
print("=" * 55)
print()

questions = [
    ("Q1:  What does CPU stand for?",
     ["central processing unit"],
     "Central Processing Unit"),

    ("Q2:  Which data structure uses LIFO order?",
     ["stack"],
     "Stack"),

    ("Q3:  What does HTML stand for?",
     ["hypertext markup language"],
     "HyperText Markup Language"),

    ("Q4:  Which language is known as the 'language of the web' (frontend)?",
     ["javascript", "js"],
     "JavaScript"),

    ("Q5:  What does RAM stand for?",
     ["random access memory"],
     "Random Access Memory"),

    ("Q6:  Which sorting algorithm has best average-case time complexity O(n log n)?",
     ["merge sort", "mergesort", "quick sort", "quicksort", "heap sort", "heapsort"],
     "Merge Sort / Quick Sort / Heap Sort"),

    ("Q7:  What is the output of 2 ** 10 in Python?",
     ["1024"],
     "1024"),

    ("Q8:  What does SQL stand for?",
     ["structured query language"],
     "Structured Query Language"),

    ("Q9:  Which protocol is used to send emails?",
     ["smtp"],
     "SMTP"),

    ("Q10: What does API stand for?",
     ["application programming interface"],
     "Application Programming Interface"),

    ("Q11: In Python, which keyword is used to define a function?",
     ["def"],
     "def"),

    ("Q12: What is the full form of OS in computing?",
     ["operating system"],
     "Operating System"),

    ("Q13: Who created the Python programming language?",
     ["guido van rossum", "guido"],
     "Guido van Rossum"),

    ("Q14: What does DNS stand for?",
     ["domain name system"],
     "Domain Name System"),

    ("Q15: Which data structure uses FIFO order?",
     ["queue"],
     "Queue"),

    ("Q16: What is the base of the binary number system?",
     ["2", "two"],
     "2"),

    ("Q17: What does IDE stand for in programming?",
     ["integrated development environment"],
     "Integrated Development Environment"),

    ("Q18: Which Python library is most commonly used for data analysis?",
     ["pandas"],
     "Pandas"),

    ("Q19: What does HTTP stand for?",
     ["hypertext transfer protocol"],
     "HyperText Transfer Protocol"),

    ("Q20: In Big O notation, what is the time complexity of binary search?",
     ["o(log n)", "log n", "o(logn)", "logn"],
     "O(log n)"),

    ("Q21: What is the powerhouse of the cell?",
     ["mitochondria"],
     "Mitochondria"),

    ("Q22: What does DNA stand for?",
     ["deoxyribonucleic acid"],
     "Deoxyribonucleic Acid"),

    ("Q23: Which organ in the human body produces insulin?",
     ["pancreas"],
     "Pancreas"),

    ("Q24: What is the normal resting heart rate for adults (bpm)?",
     ["60-100", "60 to 100", "60–100"],
     "60–100 bpm"),

    ("Q25: What does MRI stand for?",
     ["magnetic resonance imaging"],
     "Magnetic Resonance Imaging"),

    ("Q26: Which blood type is the universal donor?",
     ["o negative", "o-", "o neg"],
     "O Negative (O-)"),

    ("Q27: What is the largest organ of the human body?",
     ["skin"],
     "Skin"),

    ("Q28: How many bones are in the adult human body?",
     ["206"],
     "206"),

    ("Q29: What does ICU stand for in a hospital?",
     ["intensive care unit"],
     "Intensive Care Unit"),

    ("Q30: Which vitamin is produced by the skin when exposed to sunlight?",
     ["vitamin d", "vitamin d3"],
     "Vitamin D"),

    ("Q31: What is the medical term for high blood pressure?",
     ["hypertension"],
     "Hypertension"),

    ("Q32: Which part of the brain controls balance and coordination?",
     ["cerebellum"],
     "Cerebellum"),

    ("Q33: What does ECG stand for?",
     ["electrocardiogram", "electrocardiograph"],
     "Electrocardiogram"),

    ("Q34: How many chambers does the human heart have?",
     ["4", "four"],
     "4"),

    ("Q35: What is the normal human body temperature in Celsius?",
     ["37", "37.0", "37°c", "37 c"],
     "37°C"),
]

total = len(questions)

for q_text, valid_answers, correct in questions:
    print(q_text)
    user = input("Your answer: ").strip().lower()
    if user in valid_answers:
        print("✓ Correct!\n")
        score += 1
    else:
        print(f"✗ Wrong. Correct answer: {correct}\n")

print("=" * 55)
print(f"   QUIZ COMPLETE!")
print(f"   Your final score: {score}/{total}")

percentage = (score / total) * 100

if percentage == 100:
    print("   Result: PERFECT SCORE — Absolute genius! 🏆")
elif percentage >= 80:
    print("   Result: EXCELLENT — Strong performance! 🎯")
elif percentage >= 60:
    print("   Result: GOOD — Above average!")
elif percentage >= 40:
    print("   Result: AVERAGE — Room to grow.")
else:
    print("   Result: KEEP STUDYING — You'll get there!")

print("=" * 55)