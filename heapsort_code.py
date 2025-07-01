import time

def heap_sort(data, drawrectangle, delay):
    n = len(data)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawrectangle, delay)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawrectangle(data, get_color_array(n, i, 0))
        time.sleep(delay)
        heapify(data, i, 0, drawrectangle, delay)

    drawrectangle(data, ['green' for x in range(len(data))])  # Final sorted array

def heapify(data, n, i, drawrectangle, delay):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawrectangle(data, get_color_array(len(data), largest, i))
        time.sleep(delay)
        heapify(data, n, largest, drawrectangle, delay)

def get_color_array(length, swap1, swap2):
    color_array = []
    for i in range(length):
        if i == swap1 or i == swap2:
            color_array.append('yellow')
        else:
            color_array.append('red')
    return color_array