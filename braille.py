
templates = {
    (('x', 'o', 'o'), ('o', 'o', 'o')): 'a',
    (('x', 'x', 'o'), ('o', 'o', 'o')): 'b',
    (('x', 'o', 'o'), ('x', 'o', 'o')): 'c',
    (('x', 'o', 'o'), ('x', 'x', 'o')): 'd',
    (('x', 'o', 'o'), ('o', 'x', 'o')): 'e',
    (('x', 'x', 'o'), ('x', 'o', 'o')): 'f',
    (('x', 'x', 'o'), ('x', 'x', 'o')): 'g',
    (('x', 'x', 'o'), ('o', 'x', 'o')): 'h',
    (('o', 'x', 'o'), ('x', 'o', 'o')): 'i',
    (('o', 'x', 'o'), ('x', 'x', 'o')): 'j',
    (('x', 'o', 'x'), ('o', 'o', 'o')): 'k',
    (('x', 'x', 'x'), ('o', 'o', 'o')): 'l',
    (('x', 'o', 'x'), ('x', 'o', 'o')): 'm',
    (('x', 'o', 'x'), ('x', 'x', 'o')): 'n',
    (('x', 'o', 'x'), ('o', 'x', 'o')): 'o',
    (('x', 'x', 'x'), ('x', 'o', 'o')): 'p',
    (('x', 'x', 'x'), ('x', 'x', 'o')): 'q',
    (('x', 'x', 'x'), ('o', 'x', 'o')): 'r',
    (('o', 'x', 'x'), ('x', 'o', 'o')): 's',
    (('o', 'x', 'x'), ('x', 'x', 'o')): 't',
    (('x', 'o', 'x'), ('o', 'o', 'x')): 'u',
    (('x', 'x', 'x'), ('o', 'o', 'x')): 'v',
    (('o', 'x', 'o'), ('x', 'x', 'x')): 'w',
    (('x', 'o', 'x'), ('x', 'o', 'x')): 'x',
    (('x', 'o', 'x'), ('x', 'x', 'x')): 'y',
    (('x', 'o', 'x'), ('o', 'x', 'x')): 'z',
    (('o', 'o', 'o'), ('o', 'o', 'o')): ' '
}

if __name__ == '__main__':

    braille_patterns = []

    with open('./DATA21.txt', 'r') as file:

        lines = [line.rstrip() for line in file.readlines()]

        for i in range(0, len(lines), 3):

            braille_line = [lines[i], lines[i + 1], lines[i + 2]]

            for j in range(0, len(braille_line[0]), 2):

                columns = ((braille_line[0][j],
                            braille_line[1][j],
                            braille_line[2][j]),
                           (braille_line[0][j + 1],
                            braille_line[1][j + 1],
                            braille_line[2][j + 1]))

                braille_patterns.append(columns)

            braille_patterns.append('\n')


    last_line = ''

    for figure in braille_patterns:
        if figure == '\n':
            last_line += '\n'
            print(last_line)
            last_line = ''
        else:
            last_line += templates[figure]




