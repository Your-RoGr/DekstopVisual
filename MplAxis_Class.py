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

    def __init__(self, fileName, lenHolst = 4, Graphics = []):

        self.las = Handler(fileName)
        self.carottages = self.las.keys
        self.lenHolst = lenHolst
        self.lenGraphics = Graphics
        # fig = []
        # carottages2 = carottages

        # x, _ = las.GetCarottageValue('GK_T')

        fig = self.GetAxisX(lenHolst = 4, Graphics=[])
        # fig.append(fig1)
        super(MplAxis, self).__init__(fig)

    def GetAxisX(self,lenHolst, Graphics=[], QuantityGraphics=5, step=2):

        margins = {
            "left": 0.040,
            "bottom": 0.060,
            "right": 0.990,
            "top": 1.2
        }

        fig = plt.figure()
        fig.subplots_adjust(**margins, wspace=0.375, hspace=0)

        if len(Graphics) > 5:

            QuantityGraphics = len(Graphics)

        if len(Graphics) > 0:

            i = 5

            for Graphic in Graphics:
                x, _ = self.las.GetCarottageValue(Graphic)

                if np.nanmin(x) > 0:

                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{Graphic} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                    i += 5

        for CarottageName in self.carottages:

            x, _ = self.las.GetCarottageValue(CarottageName)

            if np.nanmin(x) > 0:

                if CarottageName == 'PZ_T':
                    i = 1
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GK_T':
                    i = 2
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))
                    print()
                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'PS_T':
                    i = 3
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GZ1_T':
                    i = 4
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'MPZ_T':
                    i = 1 + lenHolst
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'BK_T':
                    i = 2 + lenHolst
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'IK_T':
                    i = 3 + lenHolst
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GZ2_T':
                    i = 4 + lenHolst
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'MGZ_T':
                    i = 1 + lenHolst * 2
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GZ3_T':
                    i = 4 + lenHolst * 2
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'MBK_T':
                    i = 1 + lenHolst * 3
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GZ4_T':
                    i = 4 + lenHolst * 3
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

                if CarottageName == 'GZ5_T':
                    i = 4 + lenHolst * 4
                    a = pylab.subplot(QuantityGraphics, lenHolst, i)
                    ax = pylab.axes(a)
                    ax.patch.set_alpha(0)

                    ax = pylab.gca()

                    pylab.yticks([])

                    ax.spines['left'].set_visible(False)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    x1 = int(np.nanmin(x))
                    x2 = int(np.nanmax(x))

                    pylab.xlim(np.nanmin(x), np.nanmax(x))

                    plt.plot(0, 0, label=f'{CarottageName} ус. ед.', color='red')
                    ax.legend(loc='lower left', prop={'family': 'Comic Sans MS', 'size': 8})
                    plt.xticks(np.arange(x1, x2, self.step(x1, x2)), rotation=90)

        return fig

    def step(self, x1, x2):

        step = (x2-x1)/10

        return step