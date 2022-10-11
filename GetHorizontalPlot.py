import os

import pandas as pb
import matplotlib.pyplot as plt
import seaborn

from HandlerDataFrame_Class import HandlerDataFrame

def Main():
    for i in range(78):

        if i+1 <= 10:
            las = HandlerDataFrame(f'{i+1}.las')
        else:
            las = HandlerDataFrame(f'{i+1}-1.las')

        # объеденить данные, если одна скважика, или разбить на скважины, хз что в этих данных
        carrotages = las.keys # truple ([]) - все виды

        if os.path.exists(f'{os.getcwd()}\\graphics\\{i+1}-las') == False:
            os.makedirs(f'{os.getcwd()}\\graphics\\{i+1}-las')

        for carrotage in carrotages:
            x, y = las.GetCarrotValue(carrotage)

            fig, ax = plt.subplots(figsize=(4, 10))

            plt.plot(x, y)

            plt.savefig(f'{os.getcwd()}\\graphics\\{i+1}-las\\{carrotage}-{i}.png')

            fig.clear()
            # plt.show()

if __name__ == "__main__":
    Main()