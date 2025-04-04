from tkinter import *
from tkinter.ttk import * # idk if this is proper but it makes it easier
import os

ICON_FILE_PATH = os.path.join(os.path.abspath(__file__), "..", "newlogo.png")

# setting up window

root = Tk()
root.title("goongradecalc")
root.minsize(200,175)
root.maxsize(400,175)
root.geometry("400x175")

icon_photo = PhotoImage(file=ICON_FILE_PATH)

root.iconphoto(False, icon_photo)

# adding a notebook, for future functionality maybe

notebook = Notebook(root)
notebook.pack(fill=BOTH, expand=True)

# and frames
print("test")
using_points_frame = Frame(notebook)
using_percent_frame = Frame(notebook)

notebook.add(using_points_frame, text="Points to Percentage")
notebook.add(using_percent_frame, text="Percentage to Points")

# everything for the percentage stuff

label1 = Label(using_points_frame, text="Welcome to goongradecalc!")
label1.pack()

label1_on_other_frame = Label(using_percent_frame, text="Welcome to goongradecalc!")
label1_on_other_frame.pack()

point_count_label = Label(using_points_frame,text="How many points did you get?")
point_count_label.pack()

point_count = Entry(using_points_frame)
point_count.pack()

point_ability_label = Label(using_points_frame, text="How many points could you get?")
point_ability_label.pack()

point_ability = Entry(using_points_frame)
point_ability.pack()

def calculate_grade():
    max_points = float(eval(point_ability.get()))
    gotten_points = float(eval(point_count.get()))
    percent_points_unround = gotten_points / max_points * 100
    percent_points_round = round(percent_points_unround)
    percent_result.config(text="Your percentage is: " + str(percent_points_round) + "%")

percent_result = Label(using_points_frame, text="Your percentage is: ")

calculate_grade_btn = Button(using_points_frame, text="Calculate Grade!", command=calculate_grade)
calculate_grade_btn.pack()

percent_result.pack()

# and now percent to points

percent_ask_label = Label(using_percent_frame, text="What percentage did you get?")
percent_ask_label.pack()

percent_entry = Entry(using_percent_frame)
percent_entry.pack()

point_max_ask_label = Label(using_percent_frame, text="What's the maximum amount of points?")
point_max_ask_label.pack()

point_max_entry = Entry(using_percent_frame)
point_max_entry.pack()

def turn_percent_to_points():
    percent_gotten = float(eval(percent_entry.get()))
    maximum_points = float(eval(point_max_entry.get()))
    percent_to_decimal = percent_gotten / 100
    points_you_got = percent_to_decimal * maximum_points

    points_you_got = round(points_you_got, 2)
    maximum_points = round(maximum_points, 2)

    if round(points_you_got) == points_you_got: # turn into integer so it looks better
        points_you_got = round(points_you_got)
    if round(maximum_points) == maximum_points:
        maximum_points = round(maximum_points)

    result_of_percent_label.config(text="You got a: " + str(points_you_got) + "/" + str(maximum_points))

points_calc_button = Button(using_percent_frame, text="Calculate Grade!", command=turn_percent_to_points)
points_calc_button.pack()

result_of_percent_label = Label(using_percent_frame, text="You got a: ")
result_of_percent_label.pack()

root.mainloop()