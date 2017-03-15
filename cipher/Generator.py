from random import choice
from string import ascii_uppercase
from Shifter import Shifter
import Conf


def main():
    file_ = "../data/Data100-{0}-{1}.psv".format(Conf.str_len, Conf.shift_dist)

    # encoding function
    encoding_func = Shifter(Conf.shift_dist, ascii_uppercase).shift

    # generate random strings from the class set
    rands = generate_rand(Conf.size, Conf.str_len, ascii_uppercase)

    # map the set with a provided function
    mapped = map_(rands)(encoding_func)

    # save to file as pipe separated values
    with open(file_, 'w') as file_:
        for s in mapped:
            file_.write("{0}|{1}\n".format(s[0], s[1]))


def generate_rand(quan, length, class_set):
    acc = []
    for j in range(quan):
        acc.append(''.join(choice(class_set) for i in range(length)))
    return acc


def map_(xs):
    def with_(f):
        return map(lambda x: (x, ''.join(f(x))), xs)
    return with_


if __name__ == "__main__":
    main()
