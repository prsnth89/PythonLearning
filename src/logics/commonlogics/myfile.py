import os

from main.commonutils.utils import Utils


def printcurrentpath(self):
    screenshotName = Utils.getCurrentDateAndTime(self)
    imageFile = screenshotName + ".png"
    currentDir = os.path.realpath('')
    print(f'current dir--{currentDir}')
    print(f'screenshot name---{imageFile}')
    filePath = f'{currentDir}\{imageFile}'
    print(f'Filepath---{filePath}')


printcurrentpath()
