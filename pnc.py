import time
import sys

print(sys.setrecursionlimit(10000))
number = int(input("Number to calculate: "))
iterations = int(input("Number of iterations: "))
delay = int(input("Delay between iterations: "))

def checkPalindromic(number, iterations, currentIteration, delay, startTime):
    reversedNumber = int(str(number)[::-1])
    sum = number + reversedNumber
    print("{} + {} = {}".format(number, reversedNumber, sum))

    sys.stdout.write("\033]0;Iteration {} of {}\007".format(currentIteration, iterations))
    if currentIteration != iterations:
        if sum == int(str(sum)[::-1]):
            print("Number is palindromic after {} iterations".format(currentIteration))
        else:
            print("Not palindromic... trying again")
            if delay != 0:
                time.sleep(delay/1000)

            checkPalindromic(sum, iterations, currentIteration + 1, delay, startTime)
    else:
        print("Not palindromic after {} iterations".format(currentIteration))
        print("Time taken: {} seconds".format(time.time() - startTime))
    return
    
        
startTime = time.time()
checkPalindromic(number, iterations, 0, delay, startTime)