from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab

from Handler_Class import Handler

class MplCanvas(FigureCanvas):

    def __init__(self, fileName, carottage):

        las = Handler(fileName)

        carottages = las.keys

        x, y = las.GetCarottageValue(carottages[carottage])

        fig, ax = plt.subplots(figsize=(4, 10))

        plt.plot(x, y)
        plt.gca().invert_yaxis()

        super(MplCanvas, self).__init__(fig)

class MplCanvases(FigureCanvas):

    def __init__(self, fileName):

        las = Handler(fileName)
        carottages = las.keys
        fig, ax = plt.subplots()
        i = 1

        for carottage in carottages:
            if carottage != 'DEPT':
                x, y = las.GetCarottageValue(carottage)

                pylab.subplot(1, len(carottages), i)
                pylab.grid(True)
                pylab.plot(x, y)
                pylab.gca().invert_yaxis()
                pylab.title(carottage)

                i += 1

        super(MplCanvases, self).__init__(fig)