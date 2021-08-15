import random


def experiment(n, times):
    success = 0
    for i in range(times):
        birthdaySet = set()
        for j in range(n):
            month = random.randrange(1, 12)
            if month == 2:
                day = random.randrange(1, 28)
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                day = random.randrange(1, 31)
            else:
                day = random.randrange(1, 30)
            birthdaySet = birthdaySet | set([str(month) + str(day)])
        if len(birthdaySet) < n:
            success += 1
    print(success/times)


experiment(50, 100000)
