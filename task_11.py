chars = {chr(a + ord('А')): a for a in range(64)}
chars.update({' ': 64, ',': 65, '.': 66, '?': 67, '!': 68, '-': 69, '(': 70, ')': 71, '\'': 72, '"': 73, '&': 74,
              ':': 75, ';': 76, '*': 77, '\\': 78, '/': 79, '<': 80, '>': 81, '\n': 82})
chars.update({chr(a - 83 + ord('0')): a for a in range(83, 93)})
inverted_chars = {value: key for key, value in chars.items()}
chars_num = len(chars)
char_code_length = 7


def my_xor(a, b):
    if a != b:
        return "1"
    else:
        return "0"


def xor_text(bins, key):
    bin_key = "".join([bin(chars[c])[2:].zfill(char_code_length) for c in key])
    ans = ""
    for i, c in enumerate(bins):
        ans += my_xor(c, bin_key[i % len(key)])
    return ans


def encode(text, key):
    bins = "".join([bin(chars[c])[2:].zfill(char_code_length) for c in text])
    return xor_text(bins, key)


def decode(bins, key):
    text = ""
    bins = xor_text(bins, key)

    for i in range(0, len(bins), char_code_length):
        text += inverted_chars[int(bins[i: i + char_code_length], 2)]
    return text


def decode_from_file(filename, key):
    f_input = open(filename).read()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    bins = f_input
    f_output.write(decode(bins, key))
    return f_output_name


def encode_from_file(filename, key):
    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    text = f_input
    f_output.write(encode(text, key))
    return f_output_name


def generate_key(text, key):
    bin_key = "".join([bin(chars[c])[2:].zfill(char_code_length) for c in key])
    text_len = len(text)
    gamma = ""

    while len(gamma) < text_len:
        res = my_xor(bin_key[0], bin_key[4])
        gamma += res
        bin_key = bin_key[1:] + res

    # print(gamma)
    return gamma


path = "data/task_11/"


def test_all():
    key = "что такое гамма? слишком сложный вопрос."
    file_1 = path + "test_input_1.txt"
    file_2 = path + "test_input_2.txt"

    key_1 = generate_key(open(file_1).read(), key)
    result1 = encode_from_file(file_1, key_1)
    decode_from_file(result1, key_1)

    key_2 = generate_key(open(file_2).read(), key)
    result2 = encode_from_file(file_2, key_2)
    decode_from_file(result2, key_2)


test_all()
