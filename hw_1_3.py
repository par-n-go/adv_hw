for i in range(1,100):
    if not (i % 15):
        print('FizzBuzz')
        continue
    elif not (i % 3):
        print ('Fizz')
        continue
    elif not (i % 5):
        print ('Buzz')
        continue
    else:
        print (i)