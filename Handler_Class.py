import lasio
import os

class Handler():

    def __init__(self, name, *args, **kwargs):
        super(Handler, self).__init__()
        self.name = name

        self.dictionary = lasio.read(rf'{os.getcwd()}\\data\\GIS_md\\{name}')

        self.keys = self.dictionary.keys()


    def GetCarrotValue(self, CarrotName):
        self.CarrotName = self.dictionary[CarrotName]
        x = self.CarrotName
        y = self.dictionary['DEPT']
        return x, y

def Main():
    las = Handler('1.las')
    print(las.GetCarrotValue('PZ_T'))
    print(las.keys)


if __name__ == '__main__':
    Main()





