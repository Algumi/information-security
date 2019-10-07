def generate_encoder():
    letters = [chr(a + ord('а')) for a in range(32)]
    table = dict()
    for row in letters:
        for i, column in enumerate(letters):
            table[row, column] = letters[i:] + letters[:i]
    return table

print(*generate_encoder().items(), sep="\n")
