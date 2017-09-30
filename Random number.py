from random import randint
y=range(1, 101)
y.append(randint(1, 100))
def random(x,z):
    f = 0
    while x <= 100:
        f = f + x
        x = x + 1

    d=sum(z)
    answer = d-f
    print answer



random(1,y)