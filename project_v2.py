import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("соедини 4")
root.geometry("800x800")
my_font = ctk.CTkFont(family="Roboto", size=30)


def move(x, y, flag, flag_player):
    if flag == "grey":
        if flag_player == 1:
            print(0)



widget_label = ctk.CTkLabel(master=root)
widget_label.configure(text="ходит игрок:", font=my_font, )

var_radiobuttons = ctk.IntVar()
widget_radiobutton_1 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=1)
widget_radiobutton_1.configure(text="№1", font=my_font, hover="enable")
widget_radiobutton_2 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=2)
widget_radiobutton_2.configure(text="№2", font=my_font,state = "disabled", hover="enable")
var_radiobuttons.set(1)

widget_unactive_textbox = ctk.CTkTextbox(master=root)
widget_unactive_textbox.configure(font=my_font, width=310, height=140)
widget_unactive_textbox.insert(0.0, "правила:\nпобедитель:")
widget_unactive_textbox.configure(state="disabled")

frame = ctk.CTkFrame(master=root)

image_Circle_object = Image.open("images/Circle.png")
image_Circle_ctk_utility = ctk.CTkImage(dark_image=image_Circle_object, size=(20, 20))
image_Cross_object = Image.open("images/Cross.png")
image_Cross_ctk_utility = ctk.CTkImage(dark_image=image_Cross_object, size=(20, 20))
image_GreyBackground_object = Image.open("images/GreyBackground.png")
image_GreyBackground_ctk_utility = ctk.CTkImage(dark_image=image_GreyBackground_object, size=(90, 90))
image_WhiteBackground_object = Image.open("images/WhiteBackground.png")
image_WhiteBackground_ctk_utility = ctk.CTkImage(dark_image=image_WhiteBackground_object, size=(90, 90))

rows, columns = 3, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
widget_label.grid(row=0, column=0, columnspan=2, padx=(0,35), pady=(35,0))
widget_radiobutton_1.grid(row=1, column=0, padx=(50, 0), pady=(0, 20))
widget_radiobutton_2.grid(row=1, column=1, pady=(0, 20))
widget_unactive_textbox.grid(row=0, column=2, rowspan=2, padx=(0, 45), pady=(20))
frame.grid(row=2, column=0, columnspan=3)

flag_player = 1

rows, columns = 6, 7
for i in range(rows):
    frame.rowconfigure(index=i, weight=1)
for j in range(columns):
    frame.columnconfigure(index=j, weight=1)

matrix_labels = []
for i in range(6):
    matrix_labels.append([0] * 7)

for i in range(6):
    for j in range(7):
        matrix_labels[i][j] = ctk.CTkLabel(master=frame)
        matrix_labels[i][j].configure(text="", image=image_WhiteBackground_ctk_utility)
        if i == 5:
            matrix_labels[i][j].configure(text="", image=image_GreyBackground_ctk_utility)
        matrix_labels[i][j].grid(row=i, column=j, padx=1, pady=1)

matrix_flag = []
for i in range(6):
    matrix_flag.append([0] * 7)

for i in range(6):
    for j in range (7):
        matrix_flag[i][j] = "white"
        if i == 5:
            matrix_flag[i][j] = "grey"

for i in range(6):
    for j in range(7):
        matrix_labels[i][j].bind("<Bkuuoui", move(i, j, matrix_flag[i][j], flag_player))

root.mainloop()
