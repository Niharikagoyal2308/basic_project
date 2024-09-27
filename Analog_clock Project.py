#DRAW

import tkinter as tk
import time
import math

window = tk.Tk()
window.title("Analog Clock")
window.geometry('600x600')

time_diff = {'Dehradun': 0, 'New York': -5, 'Sydney': 10,'california':-12.5}

def draw_clock(time_zone):
    canvas.delete("clock")
    canvas.create_oval(50, 50, 450, 450, width=2,tags="clock")
    for i in range(1, 13):
        angle = math.radians(30 * i)
        x1 = 250 + 180 * math.sin(angle)
        y1 = 250 - 180 * math.cos(angle)
        x2 = 250 + 200 * math.sin(angle)
        y2 = 250 - 200 * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, width=4,tags="clock")
    draw_hour_hand(time_zone)
    draw_minute_hand(time_zone)
    draw_second_hand(time_zone)

def draw_hour_hand(time_zone):
    canvas.delete("hour_hand")
    local_hour = (time.localtime().tm_hour + time_diff[time_zone]) % 12
    hour_angle = math.radians((30 * local_hour) + (0.5 * time.localtime().tm_min))
    x = 250 + 80 * math.sin(hour_angle)
    y = 250 - 80 * math.cos(hour_angle)
    canvas.create_line(250, 250, x, y, width=4, fill='BROWN', tags="hour_hand")

def draw_minute_hand(time_zone):
    canvas.delete("minute_hand")
    local_minute = (time.localtime().tm_min + (time_diff[time_zone] * 60)) % 60
    minute_angle = math.radians(6 * local_minute)
    x = 250 + 120 * math.sin(minute_angle)
    y = 250 - 120 * math.cos(minute_angle)
    canvas.create_line(250, 250, x, y, width=2, fill='yellow', tags="minute_hand")

def draw_second_hand(time_zone):
    canvas.delete("second_hand")
    local_second = (time.localtime().tm_sec + (time_diff[time_zone] * 60)) % 60
    second_angle = math.radians(6 * local_second)
    x = 250 + 140 * math.sin(second_angle)
    y = 250 - 140 * math.cos(second_angle)
    canvas.create_line(250, 250, x, y, width=1.5, fill='red', tags="second_hand")

def update_clock():
    selected_time_zone = selected_time_zone_var.get()
    draw_clock(selected_time_zone)
    window.after(1000, update_clock)

canvas = tk.Canvas(window, width=500, height=500, bg="White")
canvas.pack()

selected_time_zone_var = tk.StringVar(value='Dehradun')
selected_time_zone_var.trace("w", lambda *args: update_clock())

time_zone_dropdown = tk.OptionMenu(window, selected_time_zone_var, *time_diff.keys())
time_zone_dropdown.pack()

update_clock()

window.mainloop()

