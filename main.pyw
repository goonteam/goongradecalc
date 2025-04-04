import os
import base64
from tkinter import *
from tkinter.ttk import * # idk if this is proper but it makes it easier

# base64 version of icon, so the script can run on its own
icon_base_64 = """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"""

icon = base64.b64decode(icon_base_64)
temp_folder = "goongc_temp"

print("creating temp folder")
try:
    os.mkdir(temp_folder)
except FileExistsError:
    print("temp already exists")

temp_png = "goongc_temp/app.png"
icon_file = open(temp_png, "wb")
icon_file.write(icon)
icon_file.close()

# setting up window

root = Tk()
root.title("goongradecalc")
root.minsize(200,175)
root.maxsize(400,175)
root.geometry("400x175")

icon_photo = PhotoImage(file=temp_png)

root.iconphoto(False, icon_photo)

os.remove(temp_png)

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

print("dleelrltlting temp")
try:
    os.rmdir(temp_folder)
except FileNotFoundError:
    print("alr exists")