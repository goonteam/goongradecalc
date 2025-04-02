from tkinter import *

# setting up window

root = Tk()
root.title("goongradecalc")
root.minsize(200,165)
root.maxsize(400,165)
root.geometry("400x165")

# adding widgets (later)

label1 = Label(root, text="Welcome to goongradecalc!")
label1.pack()

point_count_label = Label(root,text="How many points did you get?")
point_count_label.pack()

point_count = Entry(root)
point_count.pack()

point_ability_label = Label(root, text="How many points could you get?")
point_ability_label.pack()

point_ability = Entry(root)
point_ability.pack()

def calculate_grade():
    max_points = float(point_ability.get())
    gotten_points = float(point_count.get())
    percent_points_unround = gotten_points / max_points * 100
    percent_points_round = round(percent_points_unround)
    percent_result.config(text="Your percentage is: " + str(percent_points_round) + "%")

percent_result = Label(root, text="Your percentage is: ")

calculate_grade_btn = Button(root, text="Calculate Grade!", command=calculate_grade)
calculate_grade_btn.pack()

percent_result.pack()

root.mainloop()