from question import Question
category = input("What category do you want to play? (type random for random) ")
if category == "":
    Question()
else:
    Question(category)

