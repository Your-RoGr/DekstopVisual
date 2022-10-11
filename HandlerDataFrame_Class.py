import pandas as pd
import matplotlib.pyplot as plt
import lasio

class HandlerDataFrame():

    def __init__(self, name, *args, **kwargs):
        super(HandlerDataFrame, self).__init__()
        self.name = name

        self.las = lasio.read(rf'C:\\Users\\kiril\\OneDrive\\Рабочий стол\\For programist\\Programs\\DekstopVisual\\data\\GIS_md\\{name}')

        self.CarrotsName = self.las.keys()

        self.DEPT = self.las['DEPT']

        self.PZ_T = self.las['PZ_T']
        self.GK_T = self.las['GK_T']
        self.MPZ_T = self.las['MPZ_T']
        self.MGZ_T = self.las['MGZ_T']
        self.MBK_T = self.las['MBK_T']
        self.BK_T = self.las['BK_T']
        self.PS_T = self.las['PS_T']
        self.IK_T = self.las['IK_T']
        self.GZ1_T = self.las['GZ1_T']
        self.GZ2_T = self.las['GZ2_T']
        self.GZ3_T = self.las['GZ3_T']
        self.GZ4_T = self.las['GZ4_T']
        self.GZ5_T = self.las['GZ5_T']

    def GetCarrotValue(self, CarrotName):
        y = self.las['DEPT']
        self.CarrotsName = self.las[CarrotName]
        x = self.CarrotsName
        return x

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
    print(las1.GetCarrotValue('PZ_T'))



if __name__ == '__main__':
    Main()





