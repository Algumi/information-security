dictionary = {chr(a + ord('А')): a for a in range(64)}
dictionary.update({' ': 64, ',': 65, '.': 66, '?': 67, '!': 68, '-': 69, '(': 70, ')': 71, '\'': 72, '"': 73, '&': 74,
                   ':': 75, ';': 76, '*': 77, '\\': 78, '/': 79, '<': 80, '>': 81, '\n': 82})
dictionary.update({chr(a - 82 + ord('0')): a for a in range(82, 92)})
inverted_dictionary = {value: key for key, value in dictionary.items()}


def encode(n, m, k, char):
    return (dictionary[char] * n + k) % m


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def decode(n, m, k, num):
    return inverted_dictionary[(num - k) * mod_inverse(n, m) % m]


def encode_from_file(n, m, k, filename):
    f_input = open(filename, encoding="utf-8").read()
    f_output_name = filename[:-4] + "_encoded_output.txt"
    f_output = open(f_output_name, "w+")
    for char in list(f_input):
        f_output.write(str(encode(n, m, k, char)))
        f_output.write(" ")
    return f_output_name


def decode_from_file(n, m, k, filename):
    f_input = open(filename).read().split()
    f_output_name = filename[:-4] + "_decoded_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")
    for num in f_input:
        f_output.write(decode(n, m, k, int(num)))
    return f_output_name


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a, b)


path = "C:/Users/alex_/source/information_security/data/task_1/"


def test_1():
    file_1 = path + "test_input_1.txt"
    n, m, k = 29, 92, 21
    if gcd(n, m) != 1:
        return "Incorrect N and M"
    result1 = encode_from_file(n, m, k, file_1)
    decode_from_file(n, m, k, result1)

    file_2 = path + "test_input_2.txt"
    result2 = encode_from_file(n, m, k, file_2)
    decode_from_file(n, m, k, result2)
    print(encode(n, m, k, "Ж"), inverted_dictionary[encode(n, m, k, "Ж")])
    print(decode(n, m, k, encode(n, m, k, "Ж")))
    print(encode(n, m, k, decode(n, m, k, encode(n, m, k, "Ж"))))
    return "It was ok"


print(test_1())
