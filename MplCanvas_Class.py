from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab
import numpy as np

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

            if carottage == 'GK_T' or carottage == 'BK_T':
                pylab.subplot(1, len(carottages), i)
                if 'GK_T' in carottages:
                    x, y = las.GetCarottageValue('GK_T')
                    carottages.pop(carottages.index('GK_T'))
                    pylab.plot(x, y) # color = цвет

                x, y = las.GetCarottageValue('BK_T')

                pylab.plot(x, y) # color = цвет

                pylab.grid(True)
                pylab.gca().invert_yaxis()
                pylab.title('GK_T, BK_T')

                i += 1

            if carottage == 'PS_T' or carottage == 'IK_T':
                pylab.subplot(1, len(carottages), i)
                if 'PS_T' in carottages:
                    x, y = las.GetCarottageValue('PS_T')
                    carottages.pop(carottages.index('PS_T'))
                    pylab.plot(x, y) # color = цвет

                x, y = las.GetCarottageValue('IK_T')

                pylab.plot(x, y) # color = цвет

                pylab.grid(True)
                pylab.gca().invert_yaxis()
                pylab.title('PS_T, IK_T')

                i += 1

            if carottage == 'PZ_T' or carottage == 'MPZ_T' or carottage == 'MGZ_T' or carottage == 'MBK_T':
                pylab.subplot(1, len(carottages), i)
                if 'PZ_T' in carottages:
                    x, y = las.GetCarottageValue('PZ_T')
                    carottages.pop(carottages.index('PZ_T'))
                    pylab.plot(x, y) # color = цвет

                if 'MPZ_T' in carottages:
                    x, y = las.GetCarottageValue('MPZ_T')
                    carottages.pop(carottages.index('MPZ_T'))
                    pylab.plot(x, y) # color = цвет

                if 'MGZ_T' in carottages:
                    x, y = las.GetCarottageValue('MGZ_T')
                    carottages.pop(carottages.index('MGZ_T'))
                    pylab.plot(x, y) # color = цвет

                if 'MBK_T' in carottages:
                    x, y = las.GetCarottageValue('MBK_T')
                    carottages.pop(carottages.index('MBK_T'))
                    pylab.plot(x, y) # color = цвет

                pylab.grid(True)
                pylab.gca().invert_yaxis()
                pylab.title('PZ_T, MPZ_T,\nMGZ_T, MBK_T')

                i += 1

            for NamberGZ in range(1, 5):
                if carottage == f'GZ{NamberGZ}_T':
                    pylab.subplot(1, len(carottages), i)

                    for NamberGZ in range(1,5):
                        if f'GZ{NamberGZ}_T' in carottages:
                            x, y = las.GetCarottageValue(f'GZ{NamberGZ}_T')
                            carottages.pop(carottages.index(f'GZ{NamberGZ}_T'))
                            pylab.plot(x, y) # color = цвет

                    pylab.grid(True)
                    pylab.gca().invert_yaxis()
                    pylab.title('GZ1-5_T')

                    i += 1



        super(MplCanvases, self).__init__(fig)