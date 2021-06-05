
import sys, pygame
import common
import pygameInterface  


for index in range(0, 2):
    alphabet = common.AlphabetRandomCreate();
    print("index is : ", index)
    randomValue = common.GetRandomValue(100)
    print("random alphabet is: ", alphabet)
    print("random value is: ", randomValue)
    alphabetDirInfor = common.RandomCreateAlphabetDir()
    print("random alphabet dir  is: ", alphabetDirInfor[0])
    print("random alphabet value is: ", alphabetDirInfor[1])
    print("random alphabet ascii value is: ", ord(alphabetDirInfor[1]))

CurrentAlphabit = pygame.K_a
print("current alphabet is: ", CurrentAlphabit)


alphabetInfo =  pygameInterface.GetCurrentBallRect()

print(" alphabet rect  is: ", alphabetInfo['rect'])
print(" alphabet rect  left is: ", alphabetInfo['rect'].left)
print(" alphabet rect  right is: ", alphabetInfo['rect'].right)
print(" alphabet rect  top is: ", alphabetInfo['rect'].top)
print(" alphabet rect  bottom is: ", alphabetInfo['rect'].bottom)

rightInfo =  pygameInterface.GetRightRect()
print(" right rect  is: ", rightInfo['rect'])
print(" right rect  dir is: ", rightInfo['dir'])

failInfo =  pygameInterface.GetFailRect()
#failInfo = GetFailRect()
print(" fail rect  is: ", failInfo['rect'])
print(" fail rect  dir is: ", failInfo['dir'])

