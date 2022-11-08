import csv,re
def getData(directory):
    header =['no','vol', 'article number' ,'pages in range', 'publisher name', 'publisher location', 'publisher year']
    data = []
    with open(directory, 'r', encoding="utf-8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row[0])
            regexHandlerC1 = re.search(r'((?P<plocation>\w+([-]|([,]\s)|\s)?(\w+)?))\s(:|;)\s(?P<pname>\w+.*(('
                                       r'\s\w+)|(\s.\s))*\s?)(,|\\)\s?(cop\.\s)?(?P<pyear>\d\d\d\d)?',row[0])
            regexHandlerC2 = re.search(r'(vol\.\s(?P<vol>\d+))?(,?\s?)((iss|nO|No|no|nr)(\.?)\s(?P<num>\d+))?\s?((['
                                       r's]|[S])\.\s(?P<pagerange>\d+[-]\d+))?\s(art\.(?P<art>\w\d+))?',row[1])
            print(regexHandlerC2.group('num'))
            data.append([regexHandlerC2.group('num'),regexHandlerC2.group('vol'),regexHandlerC2.group('art'),regexHandlerC2.group('pagerange'),regexHandlerC1.group('pname'),regexHandlerC1.group('plocation'),regexHandlerC1.group('pyear')])
            print(regexHandlerC2.group('vol'))
            #vol.append(regexHandlerC2.group('vol'))
            print(regexHandlerC2.group('pagerange'))
            #pageRange.append(regexHandlerC2.group('pagerange'))
            print(regexHandlerC2.group('art'))
            #art.append(regexHandlerC2.group('art'))
            print(regexHandlerC1.group('pname'))
            #publisherName.append(regexHandlerC2.group('pname'))
            print(regexHandlerC1.group('plocation'))
            #publisherLocation.append(regexHandlerC2.group('plocation'))
            print(regexHandlerC1.group('pyear'))
            #publisherYear.append(regexHandlerC2.group('pyear'))
            print('---------')
    file.close()
    writeData(header, data)
def writeData(header, data):
    file = open('analyzed.csv','a+', encoding="utf-8", newline='')
    with file:
        csvwriter = csv.DictWriter(file, fieldnames = header)
        csvwriter.writeheader()
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)
def test():
    txt = '2019, vol. 9, iss. 1 s. 132-136 - tab. - Summ. - Bibliogr. 34 poz.'
    #matcher = re.compile(r'(vol\.\s(?P<vol>\d+))?')
    print(re.search(r'(vol\.\s(?P<vol>\d+))?',txt).groups())
#getData("G:\MNGKW\details.csv")

test()