def oscillate(start, end):
    for i in range(start, end):
        yield i
        yield -i

for n in oscillate(-3, 5):
    print(n, end=' ')
print()