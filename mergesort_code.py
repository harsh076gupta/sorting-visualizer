import time

def merge_sort(data, drawrectangle, delay):
    merge_sort_helper(data, 0, len(data)-1, drawrectangle, delay)

def merge_sort_helper(data, left, right, drawrectangle, delay):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(data, left, mid, drawrectangle, delay)
        merge_sort_helper(data, mid + 1, right, drawrectangle, delay)
        merge(data, left, mid, right, drawrectangle, delay)

def merge(data, left, mid, right, drawrectangle, delay):
    left_part = data[left:mid+1]
    right_part = data[mid+1:right+1]

    i = 0  # index for left_part
    j = 0  # index for right_part
    k = left  # index for main data array

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        drawrectangle(data, get_color_array(len(data), left, right, k))
        time.sleep(delay)
        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        drawrectangle(data, get_color_array(len(data), left, right, k))
        time.sleep(delay)
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        drawrectangle(data, get_color_array(len(data), left, right, k))
        time.sleep(delay)
        j += 1
        k += 1

    # Final sorted segment
    drawrectangle(data, ['green' if left <= x <= right else 'red' for x in range(len(data))])
    time.sleep(delay)

def get_color_array(length, left, right, curr):
    color_array = []
    for i in range(length):
        if i >= left and i <= right:
            if i == curr:
                color_array.append('yellow')
            else:
                color_array.append('lightblue')
        else:
            color_array.append('red')
    return color_array
