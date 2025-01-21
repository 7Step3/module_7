def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        file.write(f'{string}\n')
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    string_position = {}
    for index, string in enumerate(strings, start=1):
        byte = file.tell()
        file.readline()
        string_position[(index, byte)] = string
    file.close()
    return  string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)