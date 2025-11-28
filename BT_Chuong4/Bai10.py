import time


def drawShape(n, option):
    if(option == 1):
        for i in range(1, n):
            for j in range(1, n*2):
                if(j >= n and j < i + n):
                    print("*", end = ' ')
                else: print(' ', end=' ')
            print()
        for i in range(1, n*2): print("*", end=' ')
        print()
        for i in range(1, n):
            for j in range(1, n*2):
                if(j <= n and j < n - i + 1):
                    print("*", end = ' ')
                else: print(' ', end=' ')
            print()
    elif(option == 2):
        for i in range(1, n):
            for j in range(1, n*2):
                if(j >= n and j == i + n - 1 or j == n):
                    print("*", end = ' ')
                else: print(' ', end=' ')
            print()
        for i in range(1, n*2): print("*", end=' ')
        print()
        for i in range(1, n):
            for j in range(1, n*2):
                if(j <= n and j == n - i or j == 1):
                    print("*", end = ' ')
                else: print(' ', end=' ')
            print()
    time.sleep(5)
n = int(input("Nhap n: "))
drawShape(n, 1)
drawShape(n, 2)