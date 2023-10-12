import os , sys , glob , math
from tabulate import tabulate
from collections import defaultdict

searchWord = 'art'
stopWords = ['its','it','are','is','he','she','do','was','of','in','the','and','to','a']

#The path of the current script
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

#geting names and path of document files
txtfiles = []
for file in glob.glob(f'{script_directory}\\Documents\\*.txt'):
    txtfiles.append(file)


#Opening and reading documents files , making dictonary from all founded words
allWords = set()
for targetFile in txtfiles:
    with open(targetFile) as f:
        content = f.read()
    content = content.split()
    for word in content:
        allWords.add(word.lower())

#deleting stopwords
allWords -= set(stopWords)

#List of all words in all ducuments
contentsList = []
for targetFile in txtfiles:
    with open(targetFile) as f:
        content = f.read()
    content = content.lower()
    content = content.split()
    #deleting stopwords
    for stopWord in stopWords:
        content = [s for s in content if s != stopWord]
    contentsList.append(content)


#calculate fij for evry docoments
fijList = []
for content in contentsList:
    fijList.append(content.count(searchWord))

#Maximum frequency
MaxFrequncyList = []
for content in contentsList:
    maxFrequencyNumber = 0
    for word in content:
        if content.count(word) > maxFrequencyNumber:
            maxFrequency = [str(content.count(word)), word]
            maxFrequencyNumber = content.count(word)
    MaxFrequncyList.append(maxFrequency)


#tfij
tfijList = []
for i in range(len(fijList)):
    tfij = fijList[i] / int(MaxFrequncyList[i][0])
    tfij = float("{:.4f}".format(tfij))
    tfijList.append(tfij)

#idfij
N = len(txtfiles)
dfi = 0
for content in contentsList:
    if searchWord in content:
        dfi += 1
idfij = math.log(N, dfi)
idfij = float("{:.4f}".format(idfij))

#wij
wijList = []
for tfij in tfijList:
    wij = tfij * idfij
    wij = float("{:.4f}".format(wij))
    wijList.append(wij)

#Final list
names = []
for path in txtfiles:
    names.append(os.path.basename(path))
headers = ['Document','fij','Max frequency','Max frequency word','tfij','wij']
finalList = []
for i in range(len(txtfiles)):
    finalList.append([names[i],fijList[i],MaxFrequncyList[i][0],MaxFrequncyList[i][1]
                      ,str(tfijList[i]),wijList[i]])

print()
print('idfij = '+ str(idfij))
print()
print(tabulate(finalList, headers ,tablefmt="simple_grid"))
print()