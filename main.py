import csv,re
def getNameLocAndYear(directory, n):
    with open(directory, 'r', encoding="utf-8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row[0])
            regexHandlerC1 = re.search(r'((?P<plocation>\w+([-]|([,]\s)|\s)?(\w+)?))\s(:|;)\s(?P<pname>\w+.*((\s\w+)|(\s.\s))*\s?)(,|\\)\s?(cop\.\s)?(?P<pyear>\d\d\d\d)?',row[0])
            regexHandlerC2 = re.search(r'(vol\.\s(?P<vol>\d+))?(,?\s?)((iss|nO|No|no|nr)(\.?)\s(?P<num>\d+))?\s?(([s]|[S])\.\s(?P<pagerange>\d+[-]\d+))?\s(art\.(?P<art>\w\d+))?',row[1])
            #print(n+1)
            #print(row[0])
            print(regexHandlerC2.group('vol'))
            print(regexHandlerC2.group('num'))
            print(regexHandlerC2.group('pagerange'))
            print(regexHandlerC2.group('art'))
            print(regexHandlerC1.group('pname'))
            print(regexHandlerC1.group('plocation'))
            print(regexHandlerC1.group('pyear'))
            print('---------')
            #plocation = r
            #pname =
            #pyear =


getNameLocAndYear("G:\MNGKW\details.csv", 0)

