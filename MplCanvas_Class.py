from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pylab
import numpy as np

from Handler_Class import Handler


class MplCanvases(FigureCanvas):

    def __init__(self, fileName, dictColor, doubleSpinBoxsValue):

        margins = {
            "left": 0.040,
            "bottom": 0.060,
            "right": 0.990,
            "top": 0.990
        }

        las = Handler(fileName)
        carottages = las.keys
        carottages2 = carottages
        # fig, ax = plt.subplots()
        fig = plt.figure()
        fig.subplots_adjust(**margins, wspace=0.3, hspace=0)

        print(dictColor)

        i = self.GetGroupToPlot(carottages, dictColor, doubleSpinBoxsValue, las, carottages2)
        # self.GetCanvas(i, carottages2, dictColor, las)

        super(MplCanvases, self).__init__(fig)

    def GetGroupToPlot(self, carottages, dictColor, doubleSpinBoxsValue, las, carottages2):

        i = 1

        for carottage in carottages:

            if carottage == 'GK_T' or carottage == 'BK_T':
                a = pylab.subplot(1, 4, i)
                self.ax1 = pylab.axes(a)
                self.ax2 = self.ax1.twiny()
                allValue = []

                if 'GK_T' in carottages:
                    x, y = las.GetCarottageValue('GK_T')
                    carottages.pop(carottages.index('GK_T'))

                    self.GetPlotAx1(x, y, dictColor, doubleSpinBoxsValue, 'GK_T')
                    allValue.append(x)

                x, y = las.GetCarottageValue('BK_T')

                self.GetPlotAx2(x, y, dictColor, doubleSpinBoxsValue, 'BK_T')
                allValue.append(x)

                self.ax1.set_xticklabels([])
                self.ax2.set_xticklabels([])
                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('GK_T, BK_T')

                i += 1

            if carottage == 'PS_T' or carottage == 'IK_T':
                a = pylab.subplot(1, 4, i)
                self.ax1 = pylab.axes(a)
                self.ax2 = self.ax1.twiny()
                allValue = []

                if 'PS_T' in carottages:
                    x, y = las.GetCarottageValue('PS_T')
                    carottages.pop(carottages.index('PS_T'))

                    self.GetPlotAx1(x, y, dictColor, doubleSpinBoxsValue, 'PS_T')
                    allValue.append(x)

                x, y = las.GetCarottageValue('IK_T')

                self.GetPlotAx2(x, y, dictColor, doubleSpinBoxsValue, 'IK_T')
                allValue.append(x)

                self.ax1.set_xticklabels([])
                self.ax2.set_xticklabels([])
                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PS_T, IK_T')

                i += 1

            if carottage == 'PZ_T' or carottage == 'MPZ_T' or carottage == 'MGZ_T' or carottage == 'MBK_T':
                a=pylab.subplot(1, 4, i)
                self.ax1 = pylab.axes(a)
                self.ax2 = self.ax1.twiny()
                self.ax3 = self.ax1.twiny()
                self.ax4 = self.ax1.twiny()
                allValue = []

                if 'PZ_T' in carottages:
                    x, y = las.GetCarottageValue('PZ_T')
                    carottages.pop(carottages.index('PZ_T'))

                    self.GetPlotAx1(x, y, dictColor, doubleSpinBoxsValue, 'PZ_T')
                    allValue.append(x)

                if 'MPZ_T' in carottages:
                    x, y = las.GetCarottageValue('MPZ_T')
                    carottages.pop(carottages.index('MPZ_T'))

                    self.GetPlotAx2(x, y, dictColor, doubleSpinBoxsValue, 'MPZ_T')
                    allValue.append(x)

                if 'MGZ_T' in carottages:
                    x, y = las.GetCarottageValue('MGZ_T')
                    carottages.pop(carottages.index('MGZ_T'))

                    self.GetPlotAx3(x, y, dictColor, doubleSpinBoxsValue, 'MGZ_T')
                    allValue.append(x)

                if 'MBK_T' in carottages:
                    x, y = las.GetCarottageValue('MBK_T')
                    carottages.pop(carottages.index('MBK_T'))

                    self.GetPlotAx4(x, y, dictColor, doubleSpinBoxsValue, 'MBK_T')
                    allValue.append(x)

                self.ax1.set_xticklabels([])
                self.ax2.set_xticklabels([])
                self.ax3.set_xticklabels([])
                self.ax4.set_xticklabels([])
                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('PZ_T, MPZ_T,\nMGZ_T, MBK_T')

                i += 1

            # for NumberGZ in range(1, 5):
            if carottage == 'GZ1_T' or carottage == 'GZ2_T' or carottage == 'GZ3_T' or carottage == 'GZ4_T' or carottage == 'GZ5_T':
                a = pylab.subplot(1, 4, i)
                self.ax1 = pylab.axes(a)
                self.ax2 = self.ax1.twiny()
                self.ax3 = self.ax2.twiny()
                self.ax4 = self.ax3.twiny()
                self.ax5 = self.ax4.twiny()
                allValue = []

                if 'GZ1_T' in carottages:
                    x, y = las.GetCarottageValue('GZ1_T')
                    carottages.pop(carottages.index('GZ1_T'))

                    self.GetPlotAx1(x, y, dictColor, doubleSpinBoxsValue, 'GZ1_T')
                    allValue.append(x)

                if 'GZ2_T' in carottages:
                    x, y = las.GetCarottageValue('GZ2_T')
                    carottages.pop(carottages.index('GZ2_T'))

                    self.GetPlotAx2(x, y, dictColor, doubleSpinBoxsValue, 'GZ2_T')
                    allValue.append(x)

                if 'GZ3_T' in carottages:
                    x, y = las.GetCarottageValue('GZ3_T')
                    carottages.pop(carottages.index('GZ3_T'))

                    self.GetPlotAx3(x, y, dictColor, doubleSpinBoxsValue, 'GZ3_T')
                    allValue.append(x)

                if 'GZ4_T' in carottages:
                    x, y = las.GetCarottageValue('GZ4_T')
                    carottages.pop(carottages.index('GZ4_T'))

                    self.GetPlotAx4(x, y, dictColor, doubleSpinBoxsValue, 'GZ4_T')
                    allValue.append(x)

                if 'GZ5_T' in carottages:
                    x, y = las.GetCarottageValue('GZ5_T')
                    carottages.pop(carottages.index('GZ5_T'))

                    self.GetPlotAx5(x, y, dictColor, doubleSpinBoxsValue, 'GZ5_T')
                    allValue.append(x)


                    # for NumberGZ in range(1, 5):  # Гавна посмотри воняет
                    #     if f'GZ{NumberGZ}_T' in carottages:
                    #         x, y = las.GetCarottageValue(f'GZ{NumberGZ}_T')
                    #         carottages.pop(carottages.index(f'GZ{NumberGZ}_T'))
                    #
                    #         self.GetPlotAx(x, y, dictColor, f'GZ{NumberGZ}_T')
                    #         allValue.append(x)

                self.ax1.set_xticklabels([])
                self.ax2.set_xticklabels([])
                self.ax3.set_xticklabels([])
                self.ax4.set_xticklabels([])
                self.ax5.set_xticklabels([])
                pylab.grid(True)
                pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
                pylab.gca().invert_yaxis()
                pylab.title('GZ1-5_T')

                i += 1

        return i

    def GetCanvas(self, i, carottages, dictColor, las):

        pylab.subplot(1, 5, i)
        allValue = []

        title = ""

        for carottage in carottages:
            if carottage != 'DEPT':
                x, y = las.GetCarottageValue(carottage)
                carottages.pop(carottages.index(carottage))

                self.GetPlota(x, y, dictColor, carottage)

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

    def GetLog(self, NameCarottage):
        x, y = self.las.GetCarottageValue(NameCarottage)
        pylab.plot(x, y)
        pylab.yscale('log')

    # def GatFiveGraphic(self, carottages, dictColor, las):
    #     # self.GetGroupToPlot(self, carottages, dictColor, las)
    #     a = pylab.subplot(1, 5, 5)
    #     allValue = []
    #
    #     for carottage in carottages:
    #         self.ax = pylab.axes(a)
    #         x, y = las.GetCarottageValue(carottage)
    #         carottages.pop(carottages.index(carottage))
    #         self.GetPlotAx(x, y, dictColor, doubleSpinBoxsValue, carottage)
    #         allValue.append(x)
    #         self.ax.set_xticklabels([])
    #
    #     pylab.grid(True)
    #     pylab.xlim(np.nanmin(allValue) - 1, np.nanmax(allValue) + 1)
    #     pylab.gca().invert_yaxis()
    #     pylab.title('Castom Graphic')
        # for numb in len(CarottName):
        #     ax2 = self.ax2.twiny()
    # def GetPlotAx(self, x, y, dictColor, nameCarottage):
    #     color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
    #     ax1 =
    #     ax2 = 0
    #     ax3 = 0
    #     ax4 = 0
    #     ax5 = 0
    #
    #     Ax = [ax1, ax2, ax3, ax4, ax5]
    #
    #     for i in range(5):
    #         if color != '':
    #             color = color.split(': ')
    #
    #             self.Ax[i].plot(x, y, color=color[1][:-1])
    #         else:
    #             self.Ax[i].plot(x, y)

    def GetPlotAx1(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax1.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax1.plot(x, y)
    def GetPlotAx(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax.plot(x, y)

    def GetPlotAx2(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax2.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax2.plot(x, y)

    def GetPlotAx3(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax3.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax3.plot(x, y)

    def GetPlotAx4(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax4.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax4.plot(x, y)

    def GetPlotAx5(self, x, y, dictColor, doubleSpinBoxsValue, nameCarottage):
        color = dictColor['Color'][dictColor['Name'].index(f'{nameCarottage}')]
        linewidth = doubleSpinBoxsValue['Value'][doubleSpinBoxsValue['Name'].index(f'{nameCarottage}')]

        if color != '':
            color = color.split(': ')
            self.ax5.plot(x, y, color=color[1][:-1], linewidth=linewidth)
        else:
            self.ax5.plot(x, y)