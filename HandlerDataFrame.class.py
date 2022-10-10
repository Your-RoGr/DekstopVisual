import pandas as pd

class HandlerDataFrame(pd.DataFrame):

    def __init__(self, path, *args, **kwargs):
        super(HandlerDataFrame, self).__init__()
        self.path = path

df = HandlerDataFrame("1.las", x=1)

df['a'] = [1, 2, 3]

print(df)