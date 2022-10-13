import PyInstaller.__main__
import shutil
import os
import time
import math

def Main(PyFile):

    PyInstaller.__main__.run([
        f'{PyFile}.py',
        '--onefile',
        '--windowed',
    ], )

    if os.path.exists(f'{os.getcwd()}\\dist\\data'):
        shutil.rmtree(f'{os.getcwd()}\\dist\\data')

    shutil.copytree(f'{os.getcwd()}\\data', f'{os.getcwd()}\\dist\\data')

if __name__ == "__main__":
    t = time.time()

    Main("DesktopVisualApp")

    sec = (time.time() - t)
    min = math.floor(sec / 60)
    print(f'{min} min, {round((sec - min * 60), 2)} sec')