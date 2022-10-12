import os

import matplotlib.pyplot as plt

from Handler_Class import Handler

def Main():
    for i in range(78):

        if i+1 <= 10:
            las = Handler(f'{i+1}.las')
        else:
            las = Handler(f'{i+1}-1.las')

        carottages = las.keys

        if os.path.exists(f'{os.getcwd()}\\graphics\\{i+1}-las') == False:
            os.makedirs(f'{os.getcwd()}\\graphics\\{i+1}-las')

        for carottage in carottages:
            x, y = las.GetCarottageValue(carottage)

            fig, ax = plt.subplots(figsize=(4, 10))

            plt.plot(x, y)
            plt.gca().invert_yaxis()

            plt.savefig(f'{os.getcwd()}\\graphics\\{i+1}-las\\{carottage}-{i}.png')

            fig.clear()

if __name__ == "__main__":
    Main()