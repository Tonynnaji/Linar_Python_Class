#class assignment on decision making

score = int(input("Score: ")) 
if score >= 0 and score <= 39:
    print("Grade: F")
elif score >= 40 and score <= 44:
    print("Grade: E")
elif score >= 45 and score <= 49:
    print("Grade: D")
elif score >= 50 and score <= 59:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: B")
elif score >= 70 and score <= 100:
    print("Grade: A")
    print("Excellent, Well done")
else:
    print("Invalid Score")