dict_files = {}
list_files = ['1.txt', '2.txt', '3.txt']

for file in list_files:
    with open(file, 'r', encoding='utf8') as f:
        dict_files[file] = len(f.readlines())

sorted_dict = sorted(dict_files.items(), key=lambda item: item[1])

with open(sorted_dict[0][0], 'r', encoding='utf8') as content:
    text = content.read()
    with open('result.txt', 'w', encoding='utf8') as f:
        f.write(sorted_dict[0][0])
        f.write('\n')
        f.write(str(sorted_dict[0][1]))
        f.write('\n')
        f.write(text)
        f.write('\n')

for name, count in sorted_dict[1:]:
    with open(name, 'r', encoding='utf8') as content:
        text = content.read()
        with open('result.txt', 'a', encoding='utf8') as f:
            f.write(name)
            f.write('\n')
            f.write(str(count))
            f.write('\n')
            f.write(text)
            f.write('\n')
