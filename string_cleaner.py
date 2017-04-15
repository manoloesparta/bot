def string_cleaner(string):
    nuevo = ''
    while True:
        inicio = string.find('>', len(nuevo))
        final = string.find('<', inicio)
        nuevo += string[inicio:final+1]
        if inicio == -1:
            break

    nuevo = nuevo.split('<>')
    nuevo = list(filter(None, nuevo))

    visto = set()
    nuevo_2 = []
    for i in nuevo:
        if i not in visto:
            visto.add(i)
            nuevo_2.append(i)

    nuevo = ''.join(nuevo_2)

    return nuevo[1:-1]

if __name__ == '__main__':
    para = input()
    print(string_cleaner('>' + para + '<'))