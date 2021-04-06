import random, time, threading
l1 = [[' ' for _ in range(30)] for __ in range(20)]
shit = 8
y_coordinate = 10
l1[y_coordinate][3] = '-'
score = 0
for j in range(0, shit):
    l1[j][0] = 'H'
for j in range(shit + 5, 20):
    try:
        l1[j][0] = 'H'
    except:
        pass
flag = 1
for i in range(1, 30):
    if flag == 0:
        shit = max(1, shit + random.randint(-2, 2))
        if shit >= 15:
            shit -= 2
        for j in range(0, shit):
            l1[j][i] = 'H'
        for j in range(shit + 5, 20):
            try:
                l1[j][i] = 'H'
            except:
                pass
    flag = (flag + 1) % 3


def birdCoordinates():
    print("Started!")
    global y_coordinate
    while True:
        y_coordinate += 1
        time.sleep(0.3)


def jump():
    global y_coordinate
    while True:
        input()
        y_coordinate -= 1


t1 = threading.Thread(target=birdCoordinates)
t1.start()
t2 = threading.Thread(target=jump)
t2.start()
while True:
    for i in l1:
        print(''.join(i))
    print('')
    for i in range(1, 19):
        if l1[i][3] == '-':
            l1[i][3] = ' '
            break
    for i in l1:
        i.pop(0)
        i.append(' ')
    if l1[y_coordinate][3] == ' ':
        l1[y_coordinate][3] = '-'
    else:
        break
    if flag == 0:
        shit = max(1, shit + random.randint(-2, 2))
        if shit >= 15:
            shit -= 2
        for j in range(0, shit):
            l1[j][-1] = 'H'
        for j in range(shit + 5, 20):
            try:
                l1[j][-1] = 'H'
            except:
                pass
    flag = (flag + 1) % 3
    score += 10
    time.sleep(0.5)
print("GAME OVER!")
print("Score :", score)