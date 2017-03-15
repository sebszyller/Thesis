from collections import defaultdict
from sklearn import preprocessing
import numpy as np


class Preprocessing:
    def __init__(self):
        raise Exception("Preprocessing is static, don't try to instantiate it.")

    @staticmethod
    def hex_pair(str_):
        return [str_[i:i + 2] for i in range(0, len(str_), 2)]

    @staticmethod
    def map_to_classes(word):
        zeros = np.zeros((len(word), 256))
        for idx in range(len(word)):
            zeros[idx, word[idx]] = 1
        return np.array(zeros)

    @staticmethod
    def log_transform(xs):
        return preprocessing.FunctionTransformer(np.log1p).transform(xs)

    @staticmethod
    def to_ints(arr, hex_=False):
        acc = []
        if hex_:
            for row in arr:
                acc.append(map(lambda c: int(c, 16), row))
        else:
            for row in arr:
                acc.append(map(lambda c: ord(c), row))
        return acc

    @staticmethod
    def at_relu(x):
        if x < 0:
            return 0
        else:
            return x

    @staticmethod
    def mapping(xs, ys):
        xs = xs.flatten()
        ys = ys.flatten()
        tupled = map(lambda y, x: (y, x), ys, xs)

        # group
        d1 = defaultdict(list)
        for k, v in tupled:
            d1[k].append(v)

        d2 = defaultdict(list)
        for d1_key in d1.keys():
            val_dict = defaultdict(int)

            # count the number of occurrences of each digit
            for val in d1[d1_key]:
                val_dict[val] += 1

            d2[d1_key].append(val_dict)

        all_three = []

        for key in d2.keys():
            d = d2[key]
            dnp = []
            for i in range(256):
                dnp.append(d[0][i])
                all_three.append([key, i, d[0][i]])

        return all_three
