
import sys, pygame
import common

def GetCurrentBallRect():

    alphabetInfo = common.RandomCreateAlphabetDir();
    alphabetDict = {'alphabet':alphabetInfo[1], 'dir':alphabetInfo[0]}
    alphabetPicture = pygame.image.load(alphabetDict['dir'])
    alphabetRect = alphabetPicture.get_rect()

    return {'alphabet':alphabetInfo[1], 'picture':alphabetPicture, \
            'rect':alphabetRect, 'ball':alphabetPicture}

def GetRightRect():
    rightDir = common.GetCurrectDir()
    rightDir = rightDir + "right.png"
    rightPicture = pygame.image.load(rightDir)
    rightRect = rightPicture.get_rect()
    return {'rect':rightRect, 'dir':rightDir, 'ball':rightPicture}

def GetFailRect():
    failDir = common.GetCurrectDir()
    failDir = failDir + "fail.png"
    failPicture = pygame.image.load(failDir)
    failRect = failPicture.get_rect()
    return {'rect':failRect, 'dir':failDir, 'ball':failPicture}




