with open('ipconfig.txt') as file:
    file_content = file.read()

file_content = file_content.split('\n')
dict1 = {}
key = None
for content in file_content:
    if content.strip() != '':
        if content.endswith(':'):
            key = content
            key = key.replace(':', '')
            dict1[key] = " "
        else:
            if key:
                dict1[key] += content + '\n'

for k, v in dict1.items():
    if '*' in k:
        new_key = k.replace('*', '_')
        with open(f'{new_key}', 'w') as file1:
            file1.write(f'{v}')
    else:
        with open(f'{k}', 'w') as file2:
            file2.write(f'{v}')


