def nolifs(list_f):
    """ принимает список файлов и возвращает отсортированный список файлов по колличествву строк """
    dict_file = {}
    for file_r in list_f:
        with open(file_r, encoding="utf-8") as f:
            i = 0
            for _ in f:
                i += 1
            dict_file[file_r] = i
    dict_file = sorted(dict_file, key=dict_file.get)
    return dict_file

def ssf(sort_list_file, name_write_file):
    """ Принимает отсортированый список файлов и добавляет их
        по очереди в указанный файл + служебка"""
    with open(file_w, 'a', encoding="utf-8") as fw:
        i = 0
        for file_r in sort_f:
            i += 1
            with open(file_r, encoding="utf-8") as f:
                fw.write(f"\n{file_r}\n")
                fw.write(f"{i}\n")
                for str_r in f:
                    fw.write(f"{str_r}")

list_file = ['1.txt', '2.txt', '3.txt']

print(nolifs(list_file))

sort_f = nolifs(list_file)

file_w = 'total.txt'

ssf(sort_f, file_w)