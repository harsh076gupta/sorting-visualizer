from tkinter import *
from tkinter import ttk, messagebox
import random
import winsound
from bubblesort_code import bubble_sort
from insertionsort_code import insertion_sort
from mergesort_code import merge_sort
from quicksort_code import quick_sort
from selectionsort_code import selection_sort
from heapsort_code import heap_sort
from countingsort_code import counting_sort

root = Tk()
root.title('DSA PROJECT - Sorting Algorithm Visualizer')
root.geometry("800x680")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []

# Play sound when sorting is complete
def play_done_sound():
    winsound.Beep(800, 150)  # Frequency: 800Hz, Duration: 150ms

# Update status bar
def update_status(msg, color='black'):
    status_label.config(text=msg, fg=color)
    root.update_idletasks()

# Generate the array
def Generate_array():
    global arr
    try:
        lowest = int(lowest_Entry.get())
        highest = int(highest_Entry.get())
        size = int(arrsize_Entry.get())

        if lowest >= highest:
            messagebox.showerror("Invalid Range", "Lower limit must be less than upper limit.")
            return
        if size <= 0:
            messagebox.showerror("Invalid Size", "Array size must be positive.")
            return

        arr = [random.randint(lowest, highest) for _ in range(size)]
        drawrectangle(arr, ['red' for _ in range(len(arr))])
        update_status("Array Generated!", "blue")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input!\n{str(e)}")

# Draw array as rectangles
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 700
    bar_width = max(10, canvas_width / (len(arr) + 1))
    offset = 30
    spacing = 5
    normalized_array = [i / max(arr) for i in arr] if arr else []
    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(arr[i]), font=("Arial", 8))
    root.update_idletasks()

# Sorting Dispatcher
def sorting():
    global arr
    if not arr:
        messagebox.showwarning("No Array", "Please generate an array first.")
        return

    start_button.config(state=DISABLED)
    update_status("Sorting in progress...", "purple")

    speed = sortingspeed.get()
    algo = select_algorithm.get()

    try:
        if algo == "Bubble Sort":
            bubble_sort(arr, drawrectangle, speed)
        elif algo == "Insertion Sort":
            insertion_sort(arr, drawrectangle, speed)
        elif algo == "Merge Sort":
            merge_sort(arr, drawrectangle, speed)
        elif algo == "Quick Sort":
            quick_sort(arr, drawrectangle, speed)
        elif algo == "Selection Sort":
            selection_sort(arr, drawrectangle, speed)
        elif algo == "Heap Sort":
            heap_sort(arr, drawrectangle, speed)
        elif algo == "Count Sort":
            counting_sort(arr, drawrectangle, speed)

        play_done_sound()
        update_status("Sorting Completed!", "green")
    except Exception as e:
        messagebox.showerror("Sorting Error", str(e))
        update_status("Sorting Failed!", "red")

    start_button.config(state=NORMAL)

# GUI LAYOUT
options_frame = Frame(root, bg='green', width=780, height=300)
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=780, height=350, bg='lightgrey')
canvas.grid(row=1, column=0, padx=10, pady=5)

status_label = Label(root, text="Ready", bg='orange', font=('Arial', 12, 'bold'))
status_label.grid(row=2, column=0, pady=5)

# Widgets
Label(options_frame, text="Algorithm: ", font=('Arial', 10, 'bold'), bg='green', fg='white').grid(row=0, column=0, padx=10, pady=5)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, width=18,
                         values=['Bubble Sort', 'Insertion Sort', 'Merge Sort',
                                 'Quick Sort', 'Selection Sort', 'Heap Sort', 'Count Sort'])
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=120, digits=2, resolution=0.2,
                     orient=HORIZONTAL, label="Speed", bg='green', fg='white')
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

start_button = Button(options_frame, text="Start Sorting", command=sorting, bg='red', fg='white',
                      font=('Arial', 10, 'bold'), height=2, width=12)
start_button.grid(row=0, column=3, padx=10, pady=5)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL,
                     label="Lower Limit", bg='green', fg='white')
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL,
                      label="Upper Limit", bg='green', fg='white')
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL,
                      label="Array Size", bg='green', fg='white')
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Generate Array", command=Generate_array, bg='blue', fg='white',
       font=('Arial', 10, 'bold'), height=2, width=12).grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
