from sys import argv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ggplot import *
from Loader import *
from Preprocessing import *
from Runner import *
from mpl_toolkits.mplot3d import Axes3D


def main():
    sns.set(color_codes=True)
    conf = Loader(argv[1])
    conf.print_config()

    # load file and remove the pipe separator
    from_file = conf.read_file()
    from_file_split = map(lambda line_: line_.split('|'), from_file)

    # to numpy arrays
    data = np.array(from_file_split)
    xs = map(lambda s: Preprocessing.hex_pair(s), data[:, 1])
    ys = map(lambda s: Preprocessing.hex_pair(s), data[:, 0])

    # convert chars to ints
    xs = np.array(Preprocessing.to_ints(xs, True))
    ys = np.array(Preprocessing.to_ints(ys, True))

    # run_as_model(xs, ys, conf)
    run_as_stat(xs, ys)


def run_as_model(xs, ys, conf):
    xs = np.asarray(map(lambda word: Preprocessing.map_to_classes(word), xs))
    ys = preprocessing.minmax_scale(ys)
    # Runner.run_many(xs, ys, ["linear", "relu", "tanh", "sigmoid"])
    Runner.run_one(xs, ys, ["tanh", "tanh", "tanh", "tanh", "tanh", "tanh", "tanh"], conf)
    # Runner.run_adv(xs, ys, ["relu", "relu", "relu", "tanh", "tanh"])


def run_as_stat(xs, ys):
    # reverse mapping: original -> cipher
    maps = np.array(Preprocessing.mapping(ys, xs))
    maps_x = maps[:, 0]
    maps_y = maps[:, 1]
    maps_z = maps[:, 2]
    maps_z_std = np.std(maps_z)
    maps_z_mean = np.mean(maps_z)

    # maps_filtered = np.array(filter(lambda arr:
    #                                 arr[2] < maps_z_mean - maps_z_std or
    #                                 arr[2] > maps_z_mean + maps_z_std, maps))

    # maps_x = maps_filtered[:, 0]
    # maps_y = maps_filtered[:, 1]
    # maps_z = maps_filtered[:, 2]

    plot_3d(maps_x, maps_y, maps_z)

    # plt.scatter(xs, ys)
    # plt.ylim((-10, 265))
    # plt.xlim((-10, 265))
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()


def plot(xs, y1):
    two_d = np.column_stack((xs, y1))
    df = pd.DataFrame(data=two_d, columns=["X", "Y"])
    p = ggplot(aes(x="X", y="Y"), data=df) + geom_point()
    p.show()


def plot_3d(xs, ys, zs):
    ax = plt.axes(projection='3d')
    fig = plt.figure()
    c = xs + ys
    ax.scatter(xs, ys, zs, c=c)
    plt.show()


if __name__ == "__main__":
    main()
