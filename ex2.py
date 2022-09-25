print(''.join(char for n, char in enumerate(
    input()) if not (char == 'о' and n % 2 == 0)))
