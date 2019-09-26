dictionary = {chr(a + ord('а')): a for a in range(32)}


def calculate_frequency(filename):
    f_input = open(filename, encoding="utf-8").read()
    ans = dict.fromkeys(dictionary.keys(), 0)
    num_chars = 0

    for char in f_input:
        if char in dictionary:
            ans[char] += 1
            num_chars += 1

    for key in ans.keys():
        ans[key] /= num_chars

    return ans


def write_answer_to_file(ans, filename):
    f_output_name = filename[:-4] + "_output.txt"
    f_output = open(f_output_name, "w+", encoding="utf-8")
    for item in ans.items():
        f_output.write(item[0])
        f_output.write(" -- {0:.4f}\n".format(item[1]))


path = "C:/Users/alex_/source/information_security/data/task_2/"


def test_1():
    file_1 = path + "test_input_1.txt"
    ans = calculate_frequency(file_1)
    write_answer_to_file(ans, file_1)
    return ans


print(test_1())
