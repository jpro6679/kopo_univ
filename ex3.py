#ex1.py

def jumsu(x):
    grade = []
    score = []

    s = x.copy()

    for a in x:
        if a > 90:
            grade.append('A')
        elif a > 80:
            grade.append('B')
        elif a > 70:
            grade.append('C')
        elif a > 60:
            grade.append('D')
        else:
            grade.append('F')
    
    x.sort(reverse=True)

    for a in s:
        score.append(x.index(a) + 1)

    return grade, score


a = [100, 65, 45, 45, 75]

g, s = jumsu(a)

print(g)
print(s)


