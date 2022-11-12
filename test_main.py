from unittest import TestCase
from main import Extraction

import csv
class TestExtraction(TestCase):
    def setUp(self):
        self.extraction = Extraction("G:\MNGKW\details.csv")
        self.csvreader = csv.reader(open(self.extraction.directory, 'r', encoding="utf-8"))
        self.extraction.openReadFile()
        self.extraction.getData()
        self.extraction.extractData()
    def test_extractNum(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader): #test dla kolumny num
             with self.subTest():
                if row[0] is None:
                     row[0] = ''
                self.assertEqual(row[0], row2[2])

    def test_extractVol(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny vol
             with self.subTest():
                 if row[1] is None:
                     row[1] = ''
                 self.assertEqual(row[1], row2[3])
    def test_extractArt(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny art
             with self.subTest():
                 if row[2] is None:
                     row[2] = ''
                 self.assertEqual(row[2], row2[4])
    def test_extractPageRange(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny page range
             with self.subTest():
                 if row[3] is None:
                     row[3] = ''
                 self.assertEqual(row[3], row2[5])
    def test_extractPublisherName(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny publisher name
             with self.subTest():
                 if row[4] is None:
                     row[4] = ''
                 self.assertEqual(row[4], row2[7])
    def test_extractPublisherLocation(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny publisher location
             with self.subTest():
                 if row[5] is None:
                     row[5] = ''
                 self.assertEqual(row[5], row2[8])
    def test_extractPublisherYear(self):
         for (row, row2) in zip(self.extraction.data, self.csvreader):  # test dla kolumny publisher year
             with self.subTest():
                 if row[6] is None:
                     row[6] = ''
                 self.assertEqual(row[6], row2[9])