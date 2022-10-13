from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab
import numpy as np

from Handler_Class import Handler

class MplAxis(FigureCanvas):

    def __init__(self, fileName):

        las = Handler(fileName)
        carottages = las.keys
        # carottages2 = carottages

        x, _ = las.GetCarottageValue('GK_T')

        fig = self.GetAxisX(x, 'GK_T')

        super(MplAxis, self).__init__(fig)

    def GetAxisX(self, x, CarottageName, step=2):

        margins = {
            "left": 0.040,
            "bottom": 0.2,
            "right": 0.990,
            "top": 0.990
        }

        fig = plt.figure(figsize = (5, 0.5))
        ax = plt.gca()
        fig.subplots_adjust(**margins)

        plt.yticks([])

        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        pylab.xlim(np.nanmin(x), np.nanmax(x))

        x1 = int(np.nanmin(x))
        x2 = int(np.nanmax(x))

        pylab.xlim(np.nanmin(x),np.nanmax(x)-step-1)

        plt.plot(0, 0, label=CarottageName, color='red')
        ax.legend(loc='center', prop={'family': 'Comic Sans MS', 'size': 14})

        plt.xticks(range(x1, x2, step))

        return fig