import random
import os


def AlphabetRandomCreate():
    
    #ascii 'a' to 'z'
    n = random.randint(97, 97+15)
    
    return chr(n);

def GetRandomValue(seed):

    #ascii 'a' to 'z'
    n = random.randint(0, seed)

    return n;

def GetCurrectDir():
    
    currentDir = os.path.abspath('.')
    currentDir = os.path.abspath('.') + '/pygame/resources/'
    return currentDir;

def GetAlphabetDir(alphabet):
    
    pwd = os.path.abspath('.')
    alphabetDir = os.path.abspath('.') + '/pygame/resources/'
    alphabetDir = alphabetDir + alphabet + '.png'    

    return alphabetDir;


def RandomCreateAlphabetDir():
    
    alphabet = AlphabetRandomCreate()
    alphabetDir = GetAlphabetDir(alphabet)

    return (alphabetDir, alphabet)





