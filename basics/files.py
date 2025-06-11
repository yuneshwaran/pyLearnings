

fhand  = open('files_assets/textfile.txt')
print(type(fhand))
for  x in fhand:
    y = 1
    print(f'Line :{y}')
    if x.startswith('Vanilla'):
        print(f'\t{x}')
    else:
        print('Not found')