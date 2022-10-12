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

    def __init__(self, fileName, dictColor):

        las = Handler(fileName)
        carottages = las.keys
        fig, ax = plt.subplots()
        i = 1

        for carottage in carottages:

            if carottage == 'GK_T' or carottage == 'BK_T':
                pylab.subplot(1, 4, i)
                allvalue = [] #aaa

                if 'GK_T' in carottages:
                    x, y = las.GetCarottageValue('GK_T')
                    carottages.pop(carottages.index('GK_T'))

                    self.GetPlot(x, y, dictColor, 'GK_T')
                    allvalue.append(x) #aaa

                x, y = las.GetCarottageValue('BK_T')

                self.GetPlot(x, y, dictColor, 'BK_T')
                allvalue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allvalue) - 1, np.nanmax(allvalue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('GK_T, BK_T')

                i += 1

            if carottage == 'PS_T' or carottage == 'IK_T':
                pylab.subplot(1, 4, i)
                allvalue = []  # aaa

                if 'PS_T' in carottages:
                    x, y = las.GetCarottageValue('PS_T')
                    carottages.pop(carottages.index('PS_T'))

                    self.GetPlot(x, y, dictColor, 'PS_T')
                    allvalue.append(x)  # aaa

                x, y = las.GetCarottageValue('IK_T')

                self.GetPlot(x, y, dictColor, 'IK_T')
                allvalue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allvalue) - 1, np.nanmax(allvalue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PS_T, IK_T')

                i += 1

            if carottage == 'PZ_T' or carottage == 'MPZ_T' or carottage == 'MGZ_T' or carottage == 'MBK_T':
                pylab.subplot(1, 4, i)
                allvalue = []  # aaa

                if 'PZ_T' in carottages:
                    x, y = las.GetCarottageValue('PZ_T')
                    carottages.pop(carottages.index('PZ_T'))

                    self.GetPlot(x, y, dictColor, 'PZ_T')
                    allvalue.append(x)  # aaa

                if 'MPZ_T' in carottages:
                    x, y = las.GetCarottageValue('MPZ_T')
                    carottages.pop(carottages.index('MPZ_T'))

                    self.GetPlot(x, y, dictColor, 'MPZ_T')
                    allvalue.append(x)  # aaa

                if 'MGZ_T' in carottages:
                    x, y = las.GetCarottageValue('MGZ_T')
                    carottages.pop(carottages.index('MGZ_T'))

                    self.GetPlot(x, y, dictColor, 'MGZ_T')
                    allvalue.append(x)  # aaa

                if 'MBK_T' in carottages:
                    x, y = las.GetCarottageValue('MBK_T')
                    carottages.pop(carottages.index('MBK_T'))

                    self.GetPlot(x, y, dictColor, 'MBK_T')
                    allvalue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allvalue) - 1, np.nanmax(allvalue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PZ_T, MPZ_T,\nMGZ_T, MBK_T')

                i += 1

            for NumberGZ in range(1, 5):
                if carottage == f'GZ{NumberGZ}_T':
                    pylab.subplot(1, 4, i)
                    allvalue = []  # aaa

                    for NumberGZ in range(1,5): # Гавна посмотри воняет
                        if f'GZ{NumberGZ}_T' in carottages:
                            x, y = las.GetCarottageValue(f'GZ{NumberGZ}_T')
                            carottages.pop(carottages.index(f'GZ{NumberGZ}_T'))

                            self.GetPlot(x, y, dictColor, f'GZ{NumberGZ}_T')
                            allvalue.append(x)  # aaa

                    pylab.grid(True)
                    pylab.xlim(np.nanmin(allvalue) - 1, np.nanmax(allvalue) + 1)
                    pylab.gca().invert_yaxis()
                    pylab.title('GZ1-5_T')

                    i += 1

        super(MplCanvases, self).__init__(fig)

    @staticmethod
    def GetPlot(x, y, dictColor, nameCarottage):

        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            pylab.plot(x, y, color=color[1][:-1])
        else:
            pylab.plot(x, y)