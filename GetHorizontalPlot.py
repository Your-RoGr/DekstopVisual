import pandas as pb
import matplotlib.pyplot as plt
import seaborn

# from HandlerDataFrame_Class import HandlerDataFrame

def Main():
    # объеденить данные, если одна скважика, или разбить на скважины, хз что в этих данных
    carrotages = func1() # truple ([]) - все виды

    for carrotage in carrotages:
        x, y = func2(carrotage)

        plt.plot(x, y)

if __name__ == "__main__":
    Main()