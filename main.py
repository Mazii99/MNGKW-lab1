#Ekstrakcja danych z pliku csv przy użyciu wyrażeń regularnych
#Damian Tatarczuk WCY19KA1S0
import csv, re, os

class Extractor():
    def __init__(self, Column1= None, Column2 = None):
        self.data = []  # lista do przechowywania danych z ekstrakcji
        self.regexForC1 = (r'((?P<plocation>\w+([-]|([,]\s)|\s)?(\w+)?))\s(:|;)\s(?P<pname>\w+.*(('
                           r'\s\w+)|(\s.\s))*\s?)(,|\\)\s?(cop\.\s)?(?P<pyear>\d\d\d\d)?')  # wyrażenie regularne dla 1 kolumny
        self.regexForC2 = (
            r'(\d\d\d\d,\s)?(t\.\s\d\d,\s)?(vol\.\s(?P<vol>\d+))?(,?\s?)((iss|nO|No|no|nr|num)(\.?)\s(?P<num>\d+))?\s?((['
            r's]|[S])\.\s(?P<pagerange>\d+[-]\d+))?\s(((nr\sart\.)|(Article\sID))\s(?P<art>\w\d+))?')  # wyrażenie regularne dla 2 kolumny
        self.Column1 = Column1
        self.Column2 = Column2
    def extractNum(self, row): #Metoda zwracająca dane z ekstrakcji wartości num
        regexHandlerC2 = re.search(self.regexForC2, row)
        if regexHandlerC2.group('num') is None:
            return ''
        else:
            return regexHandlerC2.group('num')
    def extractVol(self, row): #Metoda zwracająca dane z ekstrakcji wartości vol
        regexHandlerC2 = re.search(self.regexForC2, row)
        if regexHandlerC2.group('vol') is None:
            return ''
        else:
            return regexHandlerC2.group('vol')
    def extractArt(self, row): #Metoda zwracająca dane z ekstrakcji wartości art
        regexHandlerC2 = re.search(self.regexForC2, row)
        if regexHandlerC2.group('art') is None:
            return ''
        else:
            return regexHandlerC2.group('art')
    def extractPageRange(self, row): #Metoda zwracająca dane z ekstrakcji wartości pages in range
        regexHandlerC2 = re.search(self.regexForC2, row)
        if regexHandlerC2.group('pagerange') is None:
            return ''
        else:
            return regexHandlerC2.group('pagerange')
    def extractName(self, row): #Metoda zwracająca dane z ekstrakcji wartości publisher name
        regexHandlerC1 = re.search(self.regexForC1, row)
        if regexHandlerC1.group('pname')  is None:
            return ''
        else:
            return regexHandlerC1.group('pname')
    def extractLocation(self, row): #Metoda zwracająca dane z ekstrakcji wartości publisher location
        regexHandlerC1 = re.search(self.regexForC1, row)
        if regexHandlerC1.group('plocation') is None:
            return ''
        else:
            return regexHandlerC1.group('plocation')
    def extractYear(self, row): #Metoda zwracająca dane z ekstrakcji wartości publisher year
        regexHandlerC1 = re.search(self.regexForC1, row)
        if regexHandlerC1.group('pyear') is None:
            return ''
        else:
            return regexHandlerC1.group('pyear')
    def extractData(self): #Metoda która wywołuje wszystkie metody do ekstrakcji w celu zapisania danych w liście data
        for rowC1, rowC2 in self.Column1, self.Column2 :
            self.data.append([self.extractNum(rowC2), self.extractVol(rowC2), self.extractArt(rowC2), self.extractPageRange(rowC2), self.extractName(rowC1), self.extractLocation(rowC1), self.extractYear(rowC1)])
