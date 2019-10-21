def generate_encoder():
    letters = [chr(a + ord('а')) for a in range(32)]
    table = dict()
    for i, row in enumerate(letters):
        line = letters[i:] + letters[:i]
        for j, column in enumerate(letters):
            table[row, column] = line[j]
    print(*table.items(), sep="\n")
    return table


def encode(word, key_word, table):
    key_word_len = key_word * (max(1, len(word) // len(key_word) + 1))
    encoder_key = key_word_len[:len(word)]
    result = ""
    for i in range(len(word)):
        result += table[word[i], encoder_key[i]]
    return result


def decode(word, key_word):
    n = 32
    letters = {a: chr(a + ord('а')) for a in range(n)}
    rev_letters = {value: key for key, value in letters.items()}
    result = ""
    for i in range(len(word)):
        result += letters[(rev_letters[word[i]] + n - rev_letters[key_word[i % len(key_word)]]) % n]
    return result


def decode_from_file(filename, key):
    f_input = open(filename).read().split()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    for word in f_input:
        f_output.write(decode(word, key))
        f_output.write(" ")
    return f_output_name


def encode_from_file(filename, key):
    encoder = generate_encoder()

    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    f_input = f_input.replace("\n", " ")

    for word in f_input.split(" "):
        f_output.write(encode(word, key, encoder))
        f_output.write(" ")
    return f_output_name


path = "data/task_6/"


def test_all():
    key = "мяч"
    file_1 = path + "test_input_1.txt"
    file_2 = path + "test_input_2.txt"

    result1 = encode_from_file(file_1, key)
    decode_from_file(result1, key)

    result2 = encode_from_file(file_2, key)
    decode_from_file(result2, key)


def test_functions():
    word = "вкусно"
    key = "ключ"
    encoder = generate_encoder()
    encoded = encode(word, key, encoder)
    print(encoded)

    decoded = decode(encoded, key)
    print(decoded)


test_all()
