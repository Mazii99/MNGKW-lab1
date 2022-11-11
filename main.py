#Ekstrakcja danych z pliku csv przy użyciu wyrażeń regularnych
#Damian Tatarczuk WCY19KA1S0
import csv,re, os
class Extraction():
    def __init__(self, directory):
        self.directory = directory
        self.data = []
        self.regexForC1 = (r'((?P<plocation>\w+([-]|([,]\s)|\s)?(\w+)?))\s(:|;)\s(?P<pname>\w+.*(('
                               r'\s\w+)|(\s.\s))*\s?)(,|\\)\s?(cop\.\s)?(?P<pyear>\d\d\d\d)?')
        self.regexForC2 = (r'(\d\d\d\d,\s)?(t\.\s\d\d,\s)?(vol\.\s(?P<vol>\d+))?(,?\s?)((iss|nO|No|no|nr|num)(\.?)\s(?P<num>\d+))?\s?((['
        r's]|[S])\.\s(?P<pagerange>\d+[-]\d+))?\s(((nr\sart\.)|(Article\sID))\s(?P<art>\w\d+))?')
        self.header = ['no', 'vol', 'article number', 'pages in range', 'publisher name', 'publisher location', 'publisher year']
    def runExtraction(self):
        self.openReadFile()
        self.getData()
        self.extractData()
        self.openWriteFile()
        self.writeData()
        self.readFile.close()
        self.writeFile.close()
    def openReadFile(self):
        self.readFile = open(self.directory, 'r', encoding="utf-8")

    def openWriteFile(self):
        if os.path.exists('analyzed.csv'):
            os.remove('analyzed.csv')
        self.writeFile = open('analyzed.csv', 'a+', encoding="utf-8", newline='')
    def getData(self):
        self.csvreader = csv.reader(self.readFile)
    def extractData(self):
        for row in self.csvreader:
            regexHandlerC1 = re.search(self.regexForC1, row[0])
            regexHandlerC2 = re.search(self.regexForC2, row[1])
            num = regexHandlerC2.group('num')
            vol = regexHandlerC2.group('vol')
            art = regexHandlerC2.group('art')
            pagerange = regexHandlerC2.group('pagerange')
            pname = regexHandlerC1.group('pname')
            plocation = regexHandlerC1.group('plocation')
            pyear = regexHandlerC1.group('pyear')
            self.data.append([num, vol, art, pagerange, pname, plocation, pyear])

    def writeData(self):
        with self.writeFile:
            csvwriter = csv.DictWriter(self.writeFile, fieldnames=self.header)
            csvwriter.writeheader()
            csvwriter = csv.writer(self.writeFile)
            csvwriter.writerows(self.data)

extraction = Extraction("G:\MNGKW\details.csv") #Należy podać lokalizację pliku csv do ekstrakcji danych
extraction.runExtraction()