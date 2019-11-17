from math import ceil


def encode(text, key):
    keys = {i: c for i, c in enumerate(key)}
    matrix = {k: [] for k in key}
    for i, c in enumerate(text):
        matrix[keys[i % len(key)]].append(c)

    for lst in matrix.values():
        if len(lst) < ceil(len(text) / len(key)):
            lst.append("#")
    matrix = sorted(matrix.items())

    result_matrix = []
    for i in range(ceil(len(text) / len(key))):
        for _, value in matrix:
            result_matrix.append(value[i])
    ans = "".join(result_matrix)

    return ans


def decode(text, key):
    keys = sorted(key)
    key_num = {i: char for i, char in enumerate(keys)}

    matrix = {k: [] for k in keys}
    for i, c in enumerate(text):
        matrix[key_num[i % len(key)]].append(c)

    ans = ""
    for i in range(ceil(len(text) / len(key))):
        for c in key:
            ans += matrix[c][i]
    return ans.replace("#", "")


def decode_from_file(filename, key):
    f_input = open(filename).read()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    f_output.write(decode(f_input, key))
    return f_output_name


def encode_from_file(filename, key):
    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    f_output.write(encode(f_input, key))
    return f_output_name


path = "data/task_10/"


def test_all():
    key = "сложныйшифр"
    file_1 = path + "test_input_1.txt"
    file_2 = path + "test_input_2.txt"

    result1 = encode_from_file(file_1, key)
    decode_from_file(result1, key)

    result2 = encode_from_file(file_2, key)
    decode_from_file(result2, key)


test_all()
