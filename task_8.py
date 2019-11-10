chars = {chr(a + ord('А')): a for a in range(64)}
chars.update({' ': 64, ',': 65, '.': 66, '?': 67, '!': 68, '-': 69, '(': 70, ')': 71, '\'': 72, '"': 73, '&': 74,
              ':': 75, ';': 76, '*': 77, '\\': 78, '/': 79, '<': 80, '>': 81, '\n': 82})
chars.update({chr(a - 83 + ord('0')): a for a in range(83, 93)})
inverted_chars = {value: key for key, value in chars.items()}
chars_num = len(chars)


def generate_dict(phrase):
    ans = dict()
    unused_letters = set(chars.keys())

    for cur_ch in phrase:
        if cur_ch in unused_letters:
            unused_letters.remove(cur_ch)
            pair = unused_letters.pop()
            ans[cur_ch] = pair
            ans[pair] = cur_ch

    for char in chars.keys():
        if char in unused_letters:
            ans[char] = char
    rev_ans = {value: key for key, value in ans.items()}

    return ans, rev_ans


def encode(c, e_dict):
    return e_dict[c]


def decode(c, d_dict):
    return d_dict[c]


def decode_from_file(filename, d_dict):
    f_input = open(filename).read()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    for i, char in enumerate(f_input):
        f_output.write(decode(char, d_dict))
    return f_output_name


def encode_from_file(filename, e_dict):
    f_input = open(filename, encoding="utf-8").read().split("-----\n")[1]
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    for i, char in enumerate(f_input):
        f_output.write(encode(char, e_dict))
    return f_output_name


path = "data/task_8/"


def test_all():
    file_1 = path + "test_input_1.txt"
    file_2 = path + "test_input_2.txt"
    phrase_1 = open(file_1).readline().replace(" ", "")
    phrase_2 = open(file_2).readline().replace(" ", "")

    e_dict_1, d_dict_1 = generate_dict(phrase_1)
    e_dict_2, d_dict_2 = generate_dict(phrase_2)

    result1 = encode_from_file(file_1, e_dict_1)
    decode_from_file(result1, d_dict_1)

    result2 = encode_from_file(file_2, e_dict_2)
    decode_from_file(result2, e_dict_2)


test_all()
