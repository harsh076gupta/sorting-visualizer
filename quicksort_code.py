import time

def quick_sort(data, drawrectangle, delay):
    quick_sort_helper(data, 0, len(data) - 1, drawrectangle, delay)

def quick_sort_helper(data, low, high, drawrectangle, delay):
    if low < high:
        pivot_index = partition(data, low, high, drawrectangle, delay)
        quick_sort_helper(data, low, pivot_index - 1, drawrectangle, delay)
        quick_sort_helper(data, pivot_index + 1, high, drawrectangle, delay)

def partition(data, low, high, drawrectangle, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        drawrectangle(data, get_color_array(len(data), low, high, i, j))
        time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    drawrectangle(data, ['green' if x == i+1 else 'red' for x in range(len(data))])
    time.sleep(delay)
    return i + 1

def get_color_array(length, low, high, border, curr):
    color_array = []
    for i in range(length):
        if i >= low and i <= high:
            if i == curr:
                color_array.append('yellow')
            elif i == border:
                color_array.append('green')
            else:
                color_array.append('lightblue')
        else:
            color_array.append('red')
    return color_array
