from datetime import datetime


def read_file(file_input_txt):
    file = open(file_input_txt, "r", encoding="utf-8")
    read_lines = file.readlines()
    processing_data = ""
    for x in range(len(read_lines)):
        processing_data = processing_data + " " + read_lines[x]
    file.close()
    return processing_data


def analise_content(text):
    delimiter = ' '
    text_unit = text.split(delimiter)
    uniq_word = filtr_uniq(text_unit)
    print(uniq_word)
    words_count = []
    all_words_count = len(text_unit)
    uniq_word_count = len(uniq_word)
    words_count.append(all_words_count)
    words_count.append(uniq_word_count)
    analise_result = []
    for word in range(len(uniq_word)):
        analise_result.append(
            'количество включений слова "' + str(uniq_word[word]) + '" ' + str(text_unit.count(uniq_word[word])))
    return uniq_word, text_unit, analise_result, all_words_count


def filtr_uniq(spisok):
    spisok_uniq = []
    for x in range(len(spisok)):
        if spisok_uniq.count(spisok[x]) < 1:
            spisok_uniq.append(spisok[x])
    return spisok_uniq


def write_result_in_file(file_path_to_write, content_data):
    date = datetime.now()
    file = open(file_path_to_write, "a", encoding='utf-8')
    file.write('дата записи: ' + str(date) + '\n')
    for element in range(len(content_data)):
        file.write(str(content_data[element]) + '\n')
    file.close()
