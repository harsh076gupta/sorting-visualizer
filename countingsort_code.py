import time

def counting_sort(data, drawrectangle, delay):
    if len(data) == 0:
        return

    max_val = max(data)
    count = [0] * (max_val + 1)

    # Count each element
    for i in range(len(data)):
        count[data[i]] += 1
        drawrectangle(data, ['blue' if x == i else 'red' for x in range(len(data))])
        time.sleep(delay)

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            data[index] = i
            drawrectangle(data, ['green' if x == index else 'red' for x in range(len(data))])
            time.sleep(delay)
            index += 1
            count[i] -= 1

    # Final sorted array
    drawrectangle(data, ['green' for x in range(len(data))])
