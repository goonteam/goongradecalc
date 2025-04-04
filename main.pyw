import os
import base64
from tkinter import *
from tkinter.ttk import * # idk if this is proper but it makes it easier

# base64 version of icon, so the script can run on its own
icon_base_64 = """iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAAXNSR0IArs4c6QAAAARnQU1BAACx
jwv8YQUAAAAJcEhZcwAADsEAAA7BAbiRa+0AAAn9SURBVHhe7Z09cBNHFMdvhc3YVHShpEwmRUKX
jqRCpgFKJlKMulBBulA5roirpDOdgqUZnApXyFQxHR2kSYs76EgFHuRo897ennxa3Um3X/f5fjOM
bo9BOm7/+97bt18BQRAEQRAEQRAEQRCNgcnPWrJ3bXiHtYItuLwc3vHC8SQIdjZHnUeyXCkqJ4Cc
KlUfzh+dtk63e8967+SdSlAqAZS2cv1wzCfB9g/PO3/IciEULoAcKn3/9MO413vRO5FlZ/Sv9tdW
1lefwFu8KW+ZUKgQChHA3vW9NuOtXbg0rXRvlWrC3sbezYCzLcbY1/KWLicQR/xURByRiwD6N/oX
Vz6t3Ief24TiskovVeX64HF78HOLsYeyqJJrUOlVANOK5+we/NJFeTuJ2ld6EouFwLe7o+4vsuAN
bwJ4vDH8scWDhwsrHiLn7mH3riw1EhFHXDgP7pDfkbfieI8PnApgiW8vRdRbZmRQ+RRqpS1vIV7j
A6cCGLSHb+EbL8liBFW8BmkWYcL5g83D7q+y6AxnAhhsDMBfMezOxWmkb3dBQnxwAg3pruuGZC2A
FLO/3x11bstrwpDQGqy+h8u18I57d9CSn8awSasPH2eVz4NDbPWyRFiAlhNM/7YsImtQYbtoHWTZ
GmMBYBdvuDH8TfH5+6cfx7fI5LsD/T76f1kUgGtQXa0xRi4AM19g9vvwr+NdPDL7HpHu4KMsBhAP
9FzEA0YWQPj8eOWT2feOtKpTy8pawS6Oo8iiMWYuIGb2UYndw84GmX3/qPEAikBeG6MtgLC7dwb1
7/MjIR5YG14fmg5ACbQEgOldaP7xAGRffhI5IZNB0/cOFtgqINQSQIvHfoz8fmEwFuzIS3THNnMR
NF1AzPdTd684Os86r+Fj+u5t8gJmQSBAlV8s0H+fZgNt8gLGAiCKZfxhjMFg1AjXTK0ACaCioAV2
YQVIABVGWoGIaMBICxJAhXERhxkLwEUakigeXQFMFYdpyDAxRBSMrBMWDDaGHP680WmcWgLwPTZN
GMD5obwIP4Lgss4YgfZwcMJUJaTSCySryMIJuBqzrY3mAyRMVRLgQIWPiYvELGI5HQtwMs78lHse
HHQPO7dkaSlGAkBSLAFCs4A9oLOGEsRxRaaLl2IsgIg0awCQWzBAe92kNPeD9hDXE4QDQxpWwFoA
yAJrIB6wiuvm8yBs1RxcZuszrDVNZqbc47wAzoNX4m+A7qiTqW6dCCBioRBmKcw66JjSErJwnQV2
A+VlMQKIEG7BfN38MTzUwZiNd1xZjSpWOryDfzqjzpeymInSCCDCwbr5OJmtRqUqnAd/Qy185WKh
bOkEkEQYNKauhs2LWi5Zq4QAluHYasSp/TpFEACuGxC9saw5mdIJIAlDq9G4ham4UgtMwH1ZPAEr
sC6vU6mEAIhsyJzMdPVQFjdA8wFqhIm1IwE0HBJAwyEB1AiTCTokgBoxs3ILekHycyEkgDoRX7kF
XWB5uRASQE3J2iMgATQcEkDDIQE0HBJAwyEBNBwSQMMhATQcEkDDIQE0HBJAwyEBNBwSQMMhATQc
EkDDIQE0HBJAwyEB1ATTDbtIADXBZD4gQgKoCwbzARESQA3RWSFEAmg4JICGQwJoOCSAhuN9f4CM
+/XQnoKWmGwPg3izALjhITzUG6j82cOlk7kMD7KrnklI+MeLAMRul5PWE7jU3KWLbaFoaBt6PWze
l3MXMK185WDptP165J6CuM1pW96KoD2HMzJoD9/GEkFah3g7twBQ+bOniuP+d/BAackJvI9nEMK/
VCta7HtP1iADhllAxKkAhA+PPUzWzQ9RBN3R9z14+HVFCOJQCooNsqOTBUScCSBsqbPnCuvufBkJ
QTkgGWBbdDJJMrYW0okAsKvX4sHZJtGW5wrjBofCGsD3yFt4Lt5DDBDxt+QtAjAdBYywFgAqUHT1
Yn7fxbnCZ7HB2UFVgNZ5OHUHA24b/49YC0BRoPD7tpUfgd+jHFSFrFFMECIC7hgm793eBcwqcN12
x2sVdAeY2YL+6u/yFoD5AhKBGnDLKy2cBYGIq5afhDgmNRYTND0wVIM/04bnVAA+mcYEs4HhrPtp
ELbBX0RlBIBMRRA7Nh3PypHXjSAaY7EN/iIqJQBEupmDsASub6IEoTVHBn4zYyw2rrdyAkAgItyR
lxgImZxLVEnmMq2IYfAXYT0YZDoObQv87vR0DKDWA0digG3+LEGtQZ80KmkBEFBaXPm1ThDNmX3L
TGscpwLIM00ruoXKwFHd0sRJAR+w7yLTGuHCBcRNcaZzalyi/j64grt1cAViKt38AdFOzH4cawug
pGrV84O9o/5+HVxB0vgKICbVyOtMoIj2NoZ/LbKMToK2ogLBCPXIWrACvSpagZRgT0T6upk+FBG0
7qgxpFpmVzHA1B8VkaOX5+NNn6GqViCpj286vqJkCqd5ExUnApiNyIvJ0auuoGqDRWl9fJNgT5j8
jJlCJ+Y6YWJn7sEgohycCPDt7qhbaiGIYG9+3YRRsJfmQha5ZScWIJajj8g9GESSRgzLPFaArV4E
e476+EkuZFmm0GnAFg8GiwrE0Bqdu7A6gv/Yt1iGBzr6j41vuzqK3pb+jf7FlU8rYKXYJhRnK0tG
+rpmPy1TmOW7XAugFH1ybPWcB69kESlFfkBE5jh3crZ7F7Z6i+SOsi5AkLU35qoXIChLn7zzrPNa
MX34LP283QG2djTz0DDeoHUU3TK18rGlWlS+mBhiMUDk1AIgap8cnqawQAyPomcBPgv7HMt5uYOp
mefsXkKFI84Gr2xWBSHOBYDMReMT/l33efdIlnIlyR2gpcpytr4uGSoecXKsfZLfh+9d1/1eLwJI
6BYew8N9YfufNmXQHoDpZcoCCneWKaUrF+F8qFpUfsL6S5OuoxcBIP3r/Usrk9VX8AuheTJIZ7oE
3QG0zC3GWDwOMN6XIDVte4afik/+TWOr4k0ASOiDW09lEWfyXBEBWkGkr0TWswaixc+P1EXkWfHW
DcurABAIUvCFR9O2Cp+5I0Rw4Ty8TL5o7sCMZVjSd49w4ttVUsx9iAOr6l0ASUEY+Krc08Qq6dZg
hmP48xK6D7gEKzmo8+TafLb6ON4FgKhBGEThD3xE4bpktAZpeGnxSKqL8SC2XASAzA/UFO8OIkSC
iAeb8HzoqtJMfFYyBZZLeg7zeLI0uQkgbG2r7+EyPlBUiDvoX3ty+Rwbf8MCdhUsE7qA5ErgwbuA
8X/hNYlEUiF4qviI3ASAzGcJBblsEZcxkIszNfGWrsIUby4mTq4CiEhwB4gTIRhUdNjSA34An3/a
ZCwNhJJLJS+iEAEseVFasYG2Lw05gco+mgT8RSsIjsDEvpT3G0chAogowLSWJvAsC4UKIMKDEKii
M1IKAUSkBIlZKNyXEgRBEESlCIL/AWnRvqKOwy4iAAAAAElFTkSuQmCC"""

icon = base64.b64decode(icon_base_64)
temp_png = "app.png"
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