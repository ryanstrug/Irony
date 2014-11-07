# Copyright (c) 2014 Ryan Strug. All Rights Reserved.

__author__ = 'ryan'

import unittest
from Flesch.Parser import Parser


class ParserTest(unittest.TestCase):
    def test_flesch_readability_index(self):
        # Scenarios
        parser = Parser(open('Data/Scenarios'))
        parser.count_objects()

        self.assertEqual(parser.sentences, 20)
        self.assertEqual(parser.syllables, 68)
        self.assertEqual(parser.words, 40)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 60.985)

        parser.file.close()

        # Lorem
        parser.file = open('Data/Lorem')
        parser.count_objects()

        self.assertEqual(parser.sentences, 4)
        self.assertEqual(parser.syllables, 142)
        self.assertEqual(parser.words, 69)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 15.221902)

        parser.file.close()

        # Book
        parser.file = open('Data/Book')
        parser.count_objects()

        self.assertEqual(parser.sentences, 1)
        self.assertEqual(parser.syllables, 40)
        self.assertEqual(parser.words, 21)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 24.377143)

        parser.file.close()

        # Quick
        parser.file = open('Data/Quick')
        parser.count_objects()

        self.assertEqual(parser.sentences, 1)
        self.assertEqual(parser.syllables, 12)
        self.assertEqual(parser.words, 9)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 84.9)

        parser.file.close()

        # Finnegan's Wake
        parser.file = open('Data/FinnegansWake')
        parser.count_objects()

        self.assertEqual(parser.sentences, 5)
        self.assertEqual(parser.syllables, 143)
        self.assertEqual(parser.words, 88)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 51.496)

        parser.file.close()

        # Invictus
        parser.file = open('Data/Invictus')
        parser.count_objects()

        self.assertEqual(parser.sentences, 5)
        self.assertEqual(parser.syllables, 129)
        self.assertEqual(parser.words, 103)
        self.assertEqual(round(parser.calculate_flesch_readability_index(), 6), 79.97066)

        parser.file.close()

    def test_get_level_description(self):
        self.assertEqual(Parser.get_level_description(9000), '5th grade')
        self.assertEqual(Parser.get_level_description(81), '6th grade')
        self.assertEqual(Parser.get_level_description(71), '7th grade')
        self.assertEqual(Parser.get_level_description(66), '8th grade')
        self.assertEqual(Parser.get_level_description(61), '9th grade')
        self.assertEqual(Parser.get_level_description(51), 'High school student')
        self.assertEqual(Parser.get_level_description(31), 'College student')
        self.assertEqual(Parser.get_level_description(0), 'College graduate')
        self.assertEqual(Parser.get_level_description(-9000), 'Law school graduate')


if __name__ == '__main__':
    unittest.main()
