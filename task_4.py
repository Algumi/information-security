def generate_decoder():
    num = 93
    table = dict()
    chars = [chr(a + ord('А')) for a in range(64)]
    chars.extend(
        [' ', ',', '.', '?', '!', '-', '(', ')', '\'', '"',
         '&', ':', ';', '*', '\\', '/', '<', '>', '\n'])
    chars.extend([chr(a - 82 + ord('0')) for a in range(82, 92)])
    for i in range(10):
        for j in range(10):
            index = i * 10 + j
            if index < num:
                table[(i, j)] = chars[i * 10 + j]
            else:
                table[(i, j)] = None
    return table


def generate_encoder(decoder):
    return {value: key for key, value in decoder.items()}


def encode(char, encoder):
    return encoder[char]


def decode(num, decoder):
    return decoder[int(num[0]), int(num[1])]


def decode_from_file(filename):
    decoder = generate_decoder()
    f_input = open(filename).read().split()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")

    for num in f_input:
        f_output.write(decode(num, decoder))
    return f_output_name


def encode_from_file(filename):
    decoder = generate_decoder()
    encoder = generate_encoder(decoder)

    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")

    for char in list(f_input):
        f_output.write(str(encode(char, encoder)[0]) + str(encode(char, encoder)[1]))
        f_output.write(" ")
    return f_output_name


path = "data/task_4/"


def test_1():
    file_1 = path + "test_input_1.txt"
    result1 = encode_from_file(file_1)
    decode_from_file(result1)

    file_2 = path + "test_input_2.txt"
    result2 = encode_from_file(file_2)
    decode_from_file(result2)


test_1()
