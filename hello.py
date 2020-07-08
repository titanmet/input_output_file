# -*- coding: utf-8 -*-

from text_oper import read_file, analise_content, write_result_in_file
from my_bot import TextBot
from tkinter import *

input_file_txt = r'input_text.txt'
output_file_txt = r'output_text.txt'
text_to_analise = read_file(input_file_txt)
uniq_word, text_unit, analise_result, all_words_count = analise_content(text_to_analise)
write_result_in_file(output_file_txt, analise_result)


def show_answer():
    sam.input = message_entry.get()
    sam.answer_the_question()
    txt.insert(END, '\n')
    txt.insert(END, sam.output)


sam = TextBot('...')
print(sam)
print(sam.output)
sam.answer_the_question()
print(sam.output)

root = Tk()
txt = Text(root, width=50, height=30, font=12)
txt.pack()

txt.insert(END, sam.output)
message_entry = Entry()
message_entry.place(relx=.5, rely=.9, anchor='c')
message_button = Button(text='Answer', command=show_answer)
message_button.place(relx=.7, rely=.9, anchor='c')

root.mainloop()
