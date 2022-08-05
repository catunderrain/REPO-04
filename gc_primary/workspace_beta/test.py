
def VAkhung():
    import matplotlib.pyplot as plt
    import random

    x = [random.randint(-20, 20) for i in range(20)]

    y = [random.randint(-20, 20) for i in range(20)]

    print('Gia tri x: ', end='')
    for i in range(20):
        print(x[i], end=' ')
    print('')
    print('Gia tri y: ', end='')
    for i in range(20):
        print(y[i], end=' ')
    print('\n')

    plt.plot(x, y)
    a = []

    for i in range(20):
        temp = []
        temp.append(x[i])
        temp.append(y[i])
        a.append(temp)

    check = True
    i = 0
    count = 0
    while check == True:
        if a[i][0] > a[i+1][0]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            count += 1
        i += 1
        if i == 19:
            i = 0
            count = 0
        if count == 0 and i == 18:
            check = False

    # print(a)
    x = []
    y = []
    for i in range(20):
        x.append(a[i][0])
        y.append(a[i][1])

    print('Gia tri x sorted: ', end='')
    for i in range(20):
        print(x[i], end=' ')
    print('')
    print('Gia tri y sorted: ', end='')
    for i in range(20):
        print(y[i], end=' ')
    print('\n')

    plt.plot(x, y)
    plt.show()


VAkhung()
