import lasio
import os

class Handler():

    def __init__(self, name, *args, **kwargs):
        super(Handler, self).__init__()
        self.name = name

        self.dictionary = lasio.read(rf'{os.getcwd()}\\data\\GIS_md\\{name}')

        self.keys = self.dictionary.keys()


    def GetCarottageValue(self, CarrotName):
        self.carottageName = self.dictionary[CarrotName]
        x = self.carottageName
        y = self.dictionary['DEPT']
        return x, y

    @staticmethod
    def GetFileNames():
        return [filenames for filenames in os.listdir("data\\GIS_md")]