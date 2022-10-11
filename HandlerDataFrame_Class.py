import pandas as pd
import matplotlib.pyplot as plt
import lasio

class HandlerDataFrame():

    def __init__(self, name, *args, **kwargs):
        super(HandlerDataFrame, self).__init__()
        self.name = name

        self.dictionary = lasio.read(rf'C:\\Users\\kiril\\OneDrive\\Рабочий стол\\For programist\\Programs\\DekstopVisual\\data\\GIS_md\\{name}')

        self.keys = self.dictionary.keys()


    def GetCarrotValue(self, CarrotName):
        self.CarrotName = self.dictionary[CarrotName]
        x = self.CarrotName
        y = self.dictionary['DEPT']
        return x, y

    # def PrintGrathic(self):
    #     fig, ax1 = plt.subplots(figsize=(12, 4))
    #
    #     color = 'tab:red'
    #     ax1.set_xlabel("Depth, m")
    #     ax1.set_ylabel("pz_t", color=color)
    #     ax1.plot(self.DEPT, self.PZ_T, color=color, label=str(self.Keys[1]))
    #     ax1.tick_params(axis='y', labelcolor=color)

        # ax2 = ax1.twinx()
        #
        # color = 'tab:blue'
        # ax2.set_ylabel("gk_t", color=color)
        # ax2.plot(dept, gk_t, color=color, label=u'NGL')
        # ax2.tick_params(axis='y', labelcolor=color)
        #
        # ax3 = ax1.twinx()
        #
        # color = 'tab:green'
        # ax3.set_ylabel("mpz_t", color=color)
        # ax3.plot(dept, mpz_t, color=color, label=u'DTP')
        # ax3.tick_params(axis='y', size=12, labelcolor=color, pad=40)
        #
        # plt.grid(True)
        #
        # fig.tight_layout()
        #
        # plt.show()

def Main():
    las1 = HandlerDataFrame('1.las')
    las2 = HandlerDataFrame('2.las')
    print(las1.GetCarrotValue('PZ_T'))
    print(las1.keys)


if __name__ == '__main__':
    Main()





