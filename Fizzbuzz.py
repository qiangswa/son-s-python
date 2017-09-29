    def hundredprint(x):
    while x < 101:
        remainder = x%3
        remainders = x%5
        if remainders == 0 and remainder == 0:
            print'fizzbuzz'
            x = x + 1
        elif remainder == 0:
            print 'fizz'
            x = x+1
        elif remainders == 0:
            print 'buzz'
            x = x+1

        else:
            print x
            x = x+1


hundredprint(1)