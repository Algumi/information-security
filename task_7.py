chars = {chr(a + ord('А')): a for a in range(64)}
chars.update({' ': 64, ',': 65, '.': 66, '?': 67, '!': 68, '-': 69, '(': 70, ')': 71, '\'': 72, '"': 73, '&': 74,
              ':': 75, ';': 76, '*': 77, '\\': 78, '/': 79, '<': 80, '>': 81, '\n': 82})
chars.update({chr(a - 83 + ord('0')): a for a in range(83, 93)})
inverted_chars = {value: key for key, value in chars.items()}
chars_num = len(chars)


def encode(c, key, i):
    return inverted_chars[(chars[c] + chars[key[i % len(key)]]) % chars_num]


def decode(c, key, i):
    return inverted_chars[(chars[c] + chars_num - chars[key[i % len(key)]]) % chars_num]


def decode_from_file(filename, key):
    f_input = open(filename).read()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    for i, char in enumerate(f_input):
        f_output.write(decode(char, key, i))
    return f_output_name


def encode_from_file(filename, key):
    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    for i, char in enumerate(f_input):
        f_output.write(encode(char, key, i))
    return f_output_name


path = "data/task_7/"


def test_all():
    key = "сложныйключ"
    file_1 = path + "test_input_1.txt"
    file_2 = path + "test_input_2.txt"

    result1 = encode_from_file(file_1, key)
    decode_from_file(result1, key)

    result2 = encode_from_file(file_2, key)
    decode_from_file(result2, key)


test_all()
