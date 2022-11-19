from unittest import TestCase
from main import Extractor
import csv

class TestExtractor(TestCase):
    def setUp(self):
        self.csvreader = csv.reader(open("details.csv", 'r', encoding="utf-8"))
        self.Extractor = Extractor()
    def test_extract_num(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractNum(row[1]),row[2])
    def test_extract_vol(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractVol(row[1]), row[3])

    def test_extract_art(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractArt(row[1]), row[4])

    def test_extract_page_range(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractPageRange(row[1]), row[5])

    def test_extract_name(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractName(row[0]), row[7])

    def test_extract_location(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractLocation(row[0]), row[8])

    def test_extract_year(self):
        for row in self.csvreader:
            with self.subTest():
                self.assertEqual(self.Extractor.extractYear(row[0]), row[9])
