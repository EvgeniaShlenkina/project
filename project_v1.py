# 19.02.2025
import customtkinter as ctk
from PIL import Image

def handle_pressing_widget_button():
    global widget_label, widget_button, widget_entry, widget_unactive_entry, widget_textbox, widget_unactive_textbox, \
        widget_combobox, var_radiobuttons, var_checkbox_1, var_checkbox_2

    print("Кнопка была нажата")

    text_widget_entry = widget_entry.get()
    print(f"Текст, введённый в однострочное поле для ввода: {text_widget_entry}")

    widget_unactive_entry.configure(state="normal")
    widget_unactive_entry.delete(0, "end")
    widget_unactive_entry.insert(0, text_widget_entry)
    widget_unactive_entry.configure(state="readonly")

    text_widget_textbox = widget_textbox.get(0.0, "end")
    print(f"Текст, введённый в многострочное поле для ввода:\n{text_widget_textbox}")

    widget_unactive_textbox.configure(state="normal")
    widget_unactive_textbox.delete(0.0, "end")
    widget_unactive_textbox.insert(0.0, text_widget_textbox)
    widget_unactive_textbox.configure(state="disabled")

    choice_combobox = widget_combobox.get()
    print(f"Элемент, выбранный в выпадающем списке: {choice_combobox}")

    choice_radiobuttons = var_radiobuttons.get()
    print(f"Был выбран {choice_radiobuttons}-ый переключатель")

    choice_checkbox_1 = var_checkbox_1.get()
    if choice_checkbox_1:
        print("Флажок 1 активен")
    else:
        print("Флажок 1 не активен")
    choice_checkbox_2 = var_checkbox_2.get()
    if choice_checkbox_2:
        print("Флажок 2 активен")
    else:
        print("Флажок 2 не активен")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("соедини 4")
root.geometry("1400x800")
my_font = ctk.CTkFont(family="Comic sans", size=30)

widget_label = ctk.CTkLabel(master=root)
widget_label.configure(text="ходит игрок", font=my_font)

var_radiobuttons = ctk.IntVar()
widget_radiobutton_1 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=1)
widget_radiobutton_1.configure(text="1", font=my_font)
widget_radiobutton_2 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=2)
widget_radiobutton_2.configure(text="2", font=my_font,state = "disabled")
var_radiobuttons.set(1)

widget_unactive_textbox = ctk.CTkTextbox(master=root)
widget_unactive_textbox.configure(font=my_font)
widget_unactive_textbox.insert(0.0, "правила:\nпобедитель:")
widget_unactive_textbox.configure(state="disabled")

frame = ctk.CTkFrame(master=root)

image_WhiteBackground_object = Image.open("images/белый фон.jpg")
image_WhiteBackground_ctk_utility = ctk.CTkImage(dark_image=image_WhiteBackground_object, size=(200, 200))
image_Cross_object = Image.open("images/крестик.jpg")
image_Cross_ctk_utility = ctk.CTkImage(dark_image=image_Cross_object, size=(200, 200))
image_Circle_object = Image.open("images/кружок.jpg")
image_Circle_ctk_utility = ctk.CTkImage(dark_image=image_Circle_object, size=(200, 200))

rows, columns = 3, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
widget_label.grid(row=0, column=0, columnspan=2)
widget_radiobutton_1.grid(row=1, column=0)
widget_radiobutton_2.grid(row=1, column=1)
widget_unactive_textbox.grid(row=0, column=2, rowspan=2)
frame.grid(row=2, column=0, columnspan=3)

root.mainloop()
