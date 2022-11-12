#Ekstrakcja danych z pliku csv przy użyciu wyrażeń regularnych
#Damian Tatarczuk WCY19KA1S0
import csv,re, os
class Extraction():
    def __init__(self, directory): #kreator obiektu
        self.directory = directory # przypisanie ścieżki do pliku wejściowego z parametru kreatora do zmiennej
        self.data = [] # lista do przechowywania danych z ekstrakcji
        self.regexForC1 = (r'((?P<plocation>\w+([-]|([,]\s)|\s)?(\w+)?))\s(:|;)\s(?P<pname>\w+.*(('
                               r'\s\w+)|(\s.\s))*\s?)(,|\\)\s?(cop\.\s)?(?P<pyear>\d\d\d\d)?') # wyrażenie regularne dla 1 kolumny
        self.regexForC2 = (r'(\d\d\d\d,\s)?(t\.\s\d\d,\s)?(vol\.\s(?P<vol>\d+))?(,?\s?)((iss|nO|No|no|nr|num)(\.?)\s(?P<num>\d+))?\s?((['
        r's]|[S])\.\s(?P<pagerange>\d+[-]\d+))?\s(((nr\sart\.)|(Article\sID))\s(?P<art>\w\d+))?') # wyrażenie regularne dla 2 kolumny
        self.header = ['no', 'vol', 'article number', 'pages in range', 'publisher name', 'publisher location', 'publisher year'] # nagłówek do pliku wyjściowego
    def runExtraction(self): # metoda przeprowadzająca ekstrakcję fraz z pliku csv
        self.openReadFile()
        self.getData()
        self.extractData()
        self.openWriteFile()
        self.writeData()
        self.readFile.close()
        self.writeFile.close()
    def openReadFile(self): # metoda do otwierania pliku wejściowego
        self.readFile = open(self.directory, 'r', encoding="utf-8")

    def openWriteFile(self): # metoda do tworzenia i otwarcia pliku wyjściowego
        if os.path.exists('analyzed.csv'):
            os.remove('analyzed.csv')
        self.writeFile = open('analyzed.csv', 'a+', encoding="utf-8", newline='')
    def getData(self): # metoda do odczytu pliku wejściowego w formacie csv
        self.csvreader = csv.reader(self.readFile)
    def extractData(self): # metoda do ekstrakcji danych z pliku
        for row in self.csvreader:
            #przeszukanie pierwszych dwóch kolumn wiersza przy użyciu wyrażeń regularnych
            regexHandlerC1 = re.search(self.regexForC1, row[0])
            regexHandlerC2 = re.search(self.regexForC2, row[1])
            #przypisanie danych z obiektu klasy re.search przy użyciu metody group do zmiennych
            num = regexHandlerC2.group('num')
            vol = regexHandlerC2.group('vol')
            art = regexHandlerC2.group('art')
            pagerange = regexHandlerC2.group('pagerange')
            pname = regexHandlerC1.group('pname')
            plocation = regexHandlerC1.group('plocation')
            pyear = regexHandlerC1.group('pyear')
            #wpisanie danych do listy
            self.data.append([num, vol, art, pagerange, pname, plocation, pyear])

    def writeData(self): #metoda do zapisu danych do pliku wyjściowego
        with self.writeFile:
            csvwriter = csv.DictWriter(self.writeFile, fieldnames=self.header)
            csvwriter.writeheader()
            csvwriter = csv.writer(self.writeFile)
            csvwriter.writerows(self.data)
#utworzenie obiektu
extraction = Extraction("G:\MNGKW\details.csv") #Należy podać lokalizację pliku csv do ekstrakcji danych
#uruchomienie metody z obiektu klasy Extraction do przeprowadzenia ekstrakcji danych
extraction.runExtraction()