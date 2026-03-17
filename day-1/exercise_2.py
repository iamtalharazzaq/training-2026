def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


user_based_scores = []
num_scores = int(input("How many scores do you want to enter? "))

for i in range(num_scores):
    score = int(input(f"Enter score {i+1}: "))
    user_based_scores.append(score)


print("\n--- User Based Scores ---")
for s in user_based_scores:
    print(f"Score: {s} -> {grade_classifier(s)}")


scores = [45, 72, 91, 60, 38, 85]
print("\n--- Given Scores ---")
for s in scores:
    print(f"Score: {s} -> {grade_classifier(s)}")
