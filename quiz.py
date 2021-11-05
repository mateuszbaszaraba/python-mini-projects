import json

points = 0

#################################################################################


def show_question(question):
    global points

    print("\n", question["question"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"], "\n")

    answer = input("Your answer: ")

    if answer == question["right_answer"]:
        points += 1
        print("Good job! That's a good answer! Points: ", points)
    else:
        print("Oops, that is not a right answer! Right answer: " + question["right_answer"] + ".")


#################################################################################
#################################################################################


with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print("\nGame over, points: " + str(points) + ".")
