# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt



# Press the green button in the gutter to run the script.
from People import People

if __name__ == '__main__':
    np.random.seed(0)

    plt.figure(figsize=(16, 16), dpi=100)

    plt.ion()

    p = People(5000, 3)

    for i in range(125):

        p.update()

        p.report()

        plt.pause(.1)

        plt.pause(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
