import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('Leap Year Checker')
win.geometry('400x400+400+100')
win.resizable(0,0)

def leap_func():
    text_entry_number = int(text_entry.get(1.0, 'end'))
    length = len(str(text_entry_number))
    if length>=4 and str(text_entry_number)[-1] == '0' and str(text_entry_number)[-2] == '0':
        if text_entry_number % 400 == 0:
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, f'{text_entry_number} is a leap year with 366 days!')

        else:
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, f'{text_entry_number} is not a leap year!')
    elif text_entry_number % 4 == 0:
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, f'{text_entry_number} is a leap year with 366 days!')
    else:
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, f'{text_entry_number} is not a leap year!')


frame_top = tk.Frame(win, height=400, width=400, bg='light blue')
frame_top.pack(expand=True, fill=tk.BOTH)
text_entry = tk.Text(frame_top, width=20, height=1, bd=4, font='arial 10 bold')
text_entry.place(x=90, y=40)

check_btn = tk.Button(frame_top, text='Check', width = 10, bd=4, bg='white', font='arial 10 bold', command=leap_func)
check_btn.place(x=250, y=38)

text_result = tk.Text(frame_top, width=44, height=12, wrap='word')
text_result.place(x=20, y=85)








win.mainloop()