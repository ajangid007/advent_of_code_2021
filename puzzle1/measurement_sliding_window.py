import os
import sys
import queue

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return [int(x) for x in myfile.read().split()]
    
def measureSlidingWindow(input):
    max = 0
    measurement = 0
    windows = queue.Queue(maxsize=3)
    for i in range(4):
        windows.put(queue.Queue(maxsize=3))
    for value in input:
        count = 3

        while not windows.empty():
            window = windows.get()
            if window.full():
                compare  = sum(window)
                if compare > max and max != 0:
                    measurement += 1
                    max = compare
                window.clear()
                windows.put(window)
            if count > 0:
                window.put(value)
                count -= 1
            else:
                break
    return measurement


if __name__ == '__main__':
    input = readInput("input.txt")
    times =  measureSlidingWindow(input)
    print(times)