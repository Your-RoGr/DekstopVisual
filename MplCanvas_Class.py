from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab
import numpy as np

from Handler_Class import Handler


class MplCanvases(FigureCanvas):

    def __init__(self, fileName, dictColor):

        las = Handler(fileName)
        carottages = las.keys
        carottages2 = carottages
        fig, ax = plt.subplots()

        i = 1

        self.GetGroupToPlot(i, carottages, dictColor, las, carottages2)
        self.GetCanvas(i, carottages2, dictColor, las) #aaa

        super(MplCanvases, self).__init__(fig)

    def GetGroupToPlot(self, i, carottages, dictColor, las, carottages2):

        for carottage in carottages:

            if carottage == 'GK_T' or carottage == 'BK_T':
                pylab.subplot(1, 4 + len(carottages2), i)
                allValue = []  # aaa

                if 'GK_T' in carottages:
                    x, y = las.GetCarottageValue('GK_T')
                    carottages.pop(carottages.index('GK_T'))

                    self.GetPlot(x, y, dictColor, 'GK_T')
                    allValue.append(x)  # aaa

                x, y = las.GetCarottageValue('BK_T')

                self.GetPlot(x, y, dictColor, 'BK_T')
                allValue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('GK_T, BK_T')

                i += 1

            if carottage == 'PS_T' or carottage == 'IK_T':
                pylab.subplot(1, 4 + len(carottages2), i)
                allValue = []  # aaa

                if 'PS_T' in carottages:
                    x, y = las.GetCarottageValue('PS_T')
                    carottages.pop(carottages.index('PS_T'))

                    self.GetPlot(x, y, dictColor, 'PS_T')
                    allValue.append(x)  # aaa

                x, y = las.GetCarottageValue('IK_T')

                self.GetPlot(x, y, dictColor, 'IK_T')
                allValue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PS_T, IK_T')

                i += 1

            if carottage == 'PZ_T' or carottage == 'MPZ_T' or carottage == 'MGZ_T' or carottage == 'MBK_T':
                pylab.subplot(1, 4 + len(carottages2), i)
                allValue = []  # aaa

                if 'PZ_T' in carottages:
                    x, y = las.GetCarottageValue('PZ_T')
                    carottages.pop(carottages.index('PZ_T'))

                    self.GetPlot(x, y, dictColor, 'PZ_T')
                    allValue.append(x)  # aaa

                if 'MPZ_T' in carottages:
                    x, y = las.GetCarottageValue('MPZ_T')
                    carottages.pop(carottages.index('MPZ_T'))

                    self.GetPlot(x, y, dictColor, 'MPZ_T')
                    allValue.append(x)  # aaa

                if 'MGZ_T' in carottages:
                    x, y = las.GetCarottageValue('MGZ_T')
                    carottages.pop(carottages.index('MGZ_T'))

                    self.GetPlot(x, y, dictColor, 'MGZ_T')
                    allValue.append(x)  # aaa

                if 'MBK_T' in carottages:
                    x, y = las.GetCarottageValue('MBK_T')
                    carottages.pop(carottages.index('MBK_T'))

                    self.GetPlot(x, y, dictColor, 'MBK_T')
                    allValue.append(x)  # aaa

                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PZ_T, MPZ_T,\nMGZ_T, MBK_T')

                i += 1

            for NumberGZ in range(1, 5):
                if carottage == f'GZ{NumberGZ}_T':
                    pylab.subplot(1, 4 + len(carottages2), i)
                    allValue = []  # aaa

                    for NumberGZ in range(1, 5):  # Гавна посмотри воняет
                        if f'GZ{NumberGZ}_T' in carottages:
                            x, y = las.GetCarottageValue(f'GZ{NumberGZ}_T')
                            carottages.pop(carottages.index(f'GZ{NumberGZ}_T'))

                            self.GetPlot(x, y, dictColor, f'GZ{NumberGZ}_T')
                            allValue.append(x)  # aaa

                    pylab.grid(True)
                    pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                    pylab.gca().invert_yaxis()
                    pylab.title('GZ1-5_T')

                    i += 1

    def GetCanvas(self, i, carottages, dictColor, las):

        pylab.subplot(1, 5, i)
        allValue = []

        title = ""

        for carottage in carottages:
            if carottage != 'DEPT':
                x, y = las.GetCarottageValue(carottage)
                carottages.pop(carottages.index(carottage))

                self.GetPlot(x, y, dictColor, carottage)

                allValue.append(x)
                title += "-" + carottage

        pylab.grid(True)
        pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
        pylab.gca().invert_yaxis()
        pylab.title(title)

        i += 1

    @staticmethod
    def GetPlot(x, y, dictColor, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            pylab.plot(x, y, color=color[1][:-1])
        else:
            pylab.plot(x, y)