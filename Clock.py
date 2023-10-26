import tkinter as tk
from time import strftime

# Clock function
def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

# Timer functions
def start_timer():
    global timer_paused
    timer_paused = False
    countdown()

def pause_timer():
    global timer_paused
    timer_paused = True

def reset_timer():
    global timer_seconds
    timer_seconds = 0
    timer_label.config(text='00:00')

def set_timer():
    global timer_seconds
    timer_seconds = int(entry.get()) * 60
    mins, secs = divmod(timer_seconds, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    timer_label.config(text=timeformat)

def countdown():
    global timer_seconds, timer_paused
    if not timer_paused and timer_seconds > 0:
        mins, secs = divmod(timer_seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        timer_label.config(text=timeformat)
        timer_seconds -= 1
        timer_label.after(1000, countdown)
    elif timer_seconds == 0:
        timer_label.config(text="Done!")

# Stopwatch functions
def start_stopwatch():
    global stopwatch_paused, stopwatch_running
    if not stopwatch_running:
        stopwatch_running = True
        stopwatch_paused = False
        stopwatch()

def pause_stopwatch():
    global stopwatch_paused, stopwatch_running
    stopwatch_paused = True

def reset_stopwatch():
    global stopwatch_seconds, stopwatch_running
    stopwatch_running = False
    stopwatch_seconds = 0
    stopwatch_label.config(text='00:00')

def stopwatch():
    global stopwatch_seconds, stopwatch_paused
    if not stopwatch_paused:
        mins, secs = divmod(stopwatch_seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        stopwatch_label.config(text=timeformat)
        stopwatch_seconds += 1
        stopwatch_label.after(1000, stopwatch)

# Initialize
root = tk.Tk()
root.title("Clock, Timer, and Stopwatch")
root.configure(bg='black')
root.resizable(0, 0)  # Lock window size

timer_paused = True
timer_seconds = 0

stopwatch_paused = True
stopwatch_seconds = 0
stopwatch_running = False

# UI Elements
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')
time()

timer_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
timer_label.pack(anchor='center')

stopwatch_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
stopwatch_label.pack(anchor='center')

entry = tk.Entry(root, bg='black', fg='white')
entry.pack(side=tk.RIGHT)
entry.insert(0, "Enter minutes")

start_timer_button = tk.Button(root, text="Start Timer", command=start_timer, bg='black', fg='white')
pause_timer_button = tk.Button(root, text="Pause Timer", command=pause_timer, bg='black', fg='white')
reset_timer_button = tk.Button(root, text="Reset Timer", command=reset_timer, bg='black', fg='white')
set_time_button = tk.Button(root, text="Set Timer", command=set_timer, bg='black', fg='white')

start_timer_button.pack(side=tk.LEFT)
pause_timer_button.pack(side=tk.LEFT)
reset_timer_button.pack(side=tk.LEFT)
set_time_button.pack(side=tk.RIGHT)

start_stopwatch_button = tk.Button(root, text="Start Stopwatch", command=start_stopwatch, bg='black', fg='white')
pause_stopwatch_button = tk.Button(root, text="Pause Stopwatch", command=pause_stopwatch, bg='black', fg='white')
reset_stopwatch_button = tk.Button(root, text="Reset Stopwatch", command=reset_stopwatch, bg='black', fg='white')

start_stopwatch_button.pack(side=tk.LEFT)
pause_stopwatch_button.pack(side=tk.LEFT)
reset_stopwatch_button.pack(side=tk.LEFT)

root.mainloop()
