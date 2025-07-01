import time

def insertion_sort(data, drawrectangle, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            drawrectangle(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(delay)
            j -= 1
        data[j + 1] = key
        drawrectangle(data, ['yellow' if x == j + 1 else 'red' for x in range(len(data))])
        time.sleep(delay)
    drawrectangle(data, ['green' for x in range(len(data))])
