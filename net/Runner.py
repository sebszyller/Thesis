from itertools import *
from keras.layers import Convolution1D
from keras.layers import Dense
from keras.layers import GlobalMaxPooling1D
from keras.models import Sequential


class Runner:
    def __init__(self):
        raise Exception("Runner is static, don't try to instantiate it.")

    @staticmethod
    def run(xs, ys, epochs, batch_size, model):
        model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
        model.fit(xs, ys, nb_epoch=epochs, batch_size=batch_size)
        return model.evaluate(xs, ys)

    @staticmethod
    def construct_model(layers, dim, funcs):
        model = Sequential()
        for i in range(0, layers):
            model.add(Dense(dim, input_dim=dim, init="uniform", activation=funcs[i])) if i == 0 \
                else model.add(Dense(dim, init="uniform", activation=funcs[i]))
        return model

    @staticmethod
    def run_many(xs, ys, activations, conf):
        # create combinations of activation functions
        opts = [activations for _ in range(conf.layers)]
        combs = [comb for comb in product(*opts)]

        # construct and run models
        inputs = len(xs[0])
        models = [Runner.construct_model(conf.layers, inputs, comb) for comb in combs]
        scores = [Runner.run(xs, ys, conf.epochs, conf.batch_size, model) for model in models]

        # compare results
        for score, activations in zip(scores, combs):
            print "\nfor activations {0}: accuracy: {1}".format(activations, score[1] * 100)

    @staticmethod
    def run_one(xs, ys, activations, conf):
        inputs = len(xs[0])
        model = Runner.construct_model(conf.layers, inputs, activations)
        score = Runner.run(xs, ys, conf.epochs, conf.batch_size, model)
        print "\nfor activations {0}: accuracy: {1}".format(activations, score[1] * 100)

    @staticmethod
    def run_adv(xs, ys, activations, conf):
        model = Sequential()
        model.add(
            Convolution1D(256, filter_length=4, border_mode="same", input_shape=(8, 256), activation=activations[0]))
        model.add(Convolution1D(256, filter_length=4, border_mode="same", activation=activations[1]))
        model.add(GlobalMaxPooling1D())
        model.add(Dense(8, init="uniform", activation=activations[4]))

        score = Runner.run(xs, ys, conf.epochs, conf.batch_size, model)
        print "\nfor activations {0}: accuracy: {1}".format(activations, score[1] * 100)
