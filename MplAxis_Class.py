from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab
import numpy as np
import seaborn as sns

from Handler_Class import Handler

# вход кол-во холстов, макс кол-во граф в холсте
class MplAxis(FigureCanvas):

    def __init__(self, fileName, lenHolst = 4, lenGraphics = 13):

        self.las = Handler(fileName)
        self.carottages = self.las.keys
        self.lenHolst = lenHolst
        self.lenGraphics = lenGraphics
        # fig = []
        # carottages2 = carottages

        # x, _ = las.GetCarottageValue('GK_T')

        fig = self.GetAxisX(lenHolst = 6)
        # fig.append(fig1)
        super(MplAxis, self).__init__(fig)

    def GetAxisX(self,lenHolst, step=2):

        margins = {
            "left": 0.040,
            "bottom": 0.2,
            "right": 0.990,
            "top": 0.990
        }

        fig = plt.figure()
        fig.subplots_adjust(**margins)

        for CarottageName in self.carottages:

            x, _ = self.las.GetCarottageValue(CarottageName)

            if CarottageName == 'PZ_T':
                i = 1
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GK_T':
                i = 2
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'PS_T':
                i = 3
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GZ1_T':
                i = 4
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'MPZ_T':
                i = 1 + lenHolst
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'BK_T':
                i = 2 + lenHolst
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'IK_T':
                i = 3 + lenHolst
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GZ2_T':
                i = 4 + lenHolst
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'MGZ_T':
                i = 1 + lenHolst * 2
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GZ3_T':
                i = 4 + lenHolst * 2
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'MBK_T':
                i = 1 + lenHolst * 3
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GZ4_T':
                i = 4 + lenHolst * 3
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

            if CarottageName == 'GZ5_T':
                i = 4 + lenHolst * 4
                pylab.subplot(5, lenHolst, i)

                ax = pylab.gca()

                pylab.yticks([])

                ax.spines['left'].set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                x1 = int(np.nanmin(x))
                x2 = int(np.nanmax(x))

                pylab.xlim(np.nanmin(x), np.nanmax(x))

                plt.plot(0, 0, label=CarottageName, color='red')
                ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                plt.xticks(range(x1, x2, 2))

        return fig