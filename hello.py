# -*- coding: utf-8 -*-

from text_oper import read_file,analise_content, write_result_in_file
input_file_txt = r'input_text.txt'
output_file_txt = r'output_text.txt'
text_to_analise = read_file(input_file_txt)
uniq_word, text_unit, analise_result, all_words_count = analise_content(text_to_analise)
write_result_in_file(output_file_txt, analise_result)


