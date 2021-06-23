import os
import operator

list_of_files_txt = {}
new_list = []

''' Функция считает количество строк в тексте файла и сортирует словарь по значениям '''
def calc_(in_file_):
    with open(in_file_, 'r', encoding='utf-8') as file_:
        count_lines = 0
        for val in file_:
            count_lines += 1
        list_of_files_txt[in_file_] = count_lines

    file_.close()
    sorted_result = sorted(list_of_files_txt.items(), key=operator.itemgetter(1))
    return sorted_result

'''Функция выбирает в директории файлы по расширению TXT '''
def reader_file(file_path, path_dir):
    for i in path_dir:
        if i[-3:] == 'txt':
           result = calc_(i)
    resulr_finally = writer_file(result)

'''Функция создет файл и записывает результат '''
def writer_file(input_dict):
    for value in input_dict:
        with open(value[0], 'r', encoding='utf-8') as file_:
            text = file_.read()
            new_list.append(value[0] + '\n')
            new_list.append(str(value[1]) + '\n')
            new_list.append(text + '\n')
            print()

    with open('total_file.txt', 'w', encoding='utf-8') as file_writer:
                for line in new_list:
                    file_writer.write(line)
    file_writer.close()


file_path_ = os.getcwd()
path_dir = os.listdir(file_path_)
reader_file(file_path_, path_dir)
