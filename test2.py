import random

goalsentence = "methinks it is like a weasel"
keyboard = "abcdefghijklmnopqrstuvwxyz "


def monkeyTheorem(strlen):
    generatesentence = ""
    for i in range(strlen):
        generatesentence = generatesentence + random.choice(keyboard)
    return generatesentence


def scoreCalculate(generate, goal):
    score = 0
    for i in range(len(goal)):
        if generate[i] == goal[i]:
            score += 1
    return score / len(goal)*100


def bestscore():
    newsentence = monkeyTheorem(len(goalsentence))
    newscore = scoreCalculate(newsentence, goalsentence)
    bestscore = 0
    while newscore < 50:
        if newscore > bestscore:
            print(newscore, newsentence)
            bestscore = newscore
        newsentence = monkeyTheorem(len(goalsentence))
        newscore = scoreCalculate(newsentence, goalsentence)


bestscore()
