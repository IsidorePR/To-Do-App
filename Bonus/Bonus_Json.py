import json

with open('Bonus_Json_question.json', 'r') as file:
    content = file.read()

#to convert from string to list
data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1,"-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{index + 1} - {result} Your answer: {question['user_choice']}, "\
               f"Correct answer: {question['correct answer']}"
    print(message)

print("result =" , score, "/", len(data))


