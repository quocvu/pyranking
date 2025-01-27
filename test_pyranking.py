import unittest
from pyranking import rank

score_fn = lambda x: x["year"]
languages = [
    {"name": "LISP", "year": 1958},
    {"name": "COBOL", "year": 1959},
    {"name": "C", "year": 1972},
    {"name": "SmallTalk", "year": 1972},
    {"name": "C++", "year": 1980},
    {"name": "Eiffel", "year": 1985},
    {"name": "Objective-C", "year": 1986},
    {"name": "ERLang", "year": 1986},
    {"name": "Haskell", "year": 1990},
    {"name": "Python", "year": 1991},
    {"name": "Ruby", "year": 1993},
    {"name": "R", "year": 1993},
    {"name": "Lua", "year": 1993},
    {"name": "PHP", "year": 1995},
    {"name": "Javascript", "year": 1995},
    {"name": "Java", "year": 1995},
    {"name": "Delphi", "year": 1995},
    {"name": "C#", "year": 2001},
    {"name": "Groovy", "year": 2003},
    {"name": "Scala", "year": 2003},
    {"name": "Go", "year": 2009},
]


class TestRankingFunction(unittest.TestCase):
    def verify(self, result, rank, year):
        self.assertEqual(result["rank"], rank)
        self.assertEqual(result["item"]["year"], year)

    def test_standard_competition_ranking(self):
        """
        competition ranking
        """
        res = rank(languages, score_fn, strategy="competition")
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 2009)
        self.verify(res[1], 2, 2003)
        self.verify(res[2], 2, 2003)
        self.verify(res[3], 4, 2001)
        self.verify(res[4], 5, 1995)
        self.verify(res[5], 5, 1995)
        self.verify(res[6], 5, 1995)
        self.verify(res[7], 5, 1995)
        self.verify(res[8], 9, 1993)
        self.verify(res[9], 9, 1993)
        self.verify(res[10], 9, 1993)
        self.verify(res[11], 12, 1991)
        self.verify(res[12], 13, 1990)
        self.verify(res[13], 14, 1986)
        self.verify(res[14], 14, 1986)
        self.verify(res[15], 16, 1985)
        self.verify(res[16], 17, 1980)
        self.verify(res[17], 18, 1972)
        self.verify(res[18], 18, 1972)
        self.verify(res[19], 20, 1959)
        self.verify(res[20], 21, 1958)

    def test_modified_competition_ranking(self):
        """
        modified competition ranking
        """
        res = rank(languages, score_fn, strategy="modified-competition")
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 2009)
        self.verify(res[1], 3, 2003)
        self.verify(res[2], 3, 2003)
        self.verify(res[3], 4, 2001)
        self.verify(res[4], 8, 1995)
        self.verify(res[5], 8, 1995)
        self.verify(res[6], 8, 1995)
        self.verify(res[7], 8, 1995)
        self.verify(res[8], 11, 1993)
        self.verify(res[9], 11, 1993)
        self.verify(res[10], 11, 1993)
        self.verify(res[11], 12, 1991)
        self.verify(res[12], 13, 1990)
        self.verify(res[13], 15, 1986)
        self.verify(res[14], 15, 1986)
        self.verify(res[15], 16, 1985)
        self.verify(res[16], 17, 1980)
        self.verify(res[17], 19, 1972)
        self.verify(res[18], 19, 1972)
        self.verify(res[19], 20, 1959)
        self.verify(res[20], 21, 1958)

    def test_dense_ranking(self):
        """
        dense ranking
        """
        res = rank(languages, score_fn, strategy="dense")
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 2009)
        self.verify(res[1], 2, 2003)
        self.verify(res[2], 2, 2003)
        self.verify(res[3], 3, 2001)
        self.verify(res[4], 4, 1995)
        self.verify(res[5], 4, 1995)
        self.verify(res[6], 4, 1995)
        self.verify(res[7], 4, 1995)
        self.verify(res[8], 5, 1993)
        self.verify(res[9], 5, 1993)
        self.verify(res[10], 5, 1993)
        self.verify(res[11], 6, 1991)
        self.verify(res[12], 7, 1990)
        self.verify(res[13], 8, 1986)
        self.verify(res[14], 8, 1986)
        self.verify(res[15], 9, 1985)
        self.verify(res[16], 10, 1980)
        self.verify(res[17], 11, 1972)
        self.verify(res[18], 11, 1972)
        self.verify(res[19], 12, 1959)
        self.verify(res[20], 13, 1958)

    def test_ordinal_ranking(self):
        """
        ordinal ranking
        """
        res = rank(languages, score_fn, strategy="ordinal")
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 2009)
        self.verify(res[1], 2, 2003)
        self.verify(res[2], 3, 2003)
        self.verify(res[3], 4, 2001)
        self.verify(res[4], 5, 1995)
        self.verify(res[5], 6, 1995)
        self.verify(res[6], 7, 1995)
        self.verify(res[7], 8, 1995)
        self.verify(res[8], 9, 1993)
        self.verify(res[9], 10, 1993)
        self.verify(res[10], 11, 1993)
        self.verify(res[11], 12, 1991)
        self.verify(res[12], 13, 1990)
        self.verify(res[13], 14, 1986)
        self.verify(res[14], 15, 1986)
        self.verify(res[15], 16, 1985)
        self.verify(res[16], 17, 1980)
        self.verify(res[17], 18, 1972)
        self.verify(res[18], 19, 1972)
        self.verify(res[19], 20, 1959)
        self.verify(res[20], 21, 1958)

    def test_fractional_ranking(self):
        """
        fractional ranking
        """
        res = rank(languages, score_fn, strategy="fractional")
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 2009)
        self.verify(res[1], 2.5, 2003)
        self.verify(res[2], 2.5, 2003)
        self.verify(res[3], 4, 2001)
        self.verify(res[4], 6.5, 1995)
        self.verify(res[5], 6.5, 1995)
        self.verify(res[6], 6.5, 1995)
        self.verify(res[7], 6.5, 1995)
        self.verify(res[8], 10, 1993)
        self.verify(res[9], 10, 1993)
        self.verify(res[10], 10, 1993)
        self.verify(res[11], 12, 1991)
        self.verify(res[12], 13, 1990)
        self.verify(res[13], 14.5, 1986)
        self.verify(res[14], 14.5, 1986)
        self.verify(res[15], 16, 1985)
        self.verify(res[16], 17, 1980)
        self.verify(res[17], 18.5, 1972)
        self.verify(res[18], 18.5, 1972)
        self.verify(res[19], 20, 1959)
        self.verify(res[20], 21, 1958)

    def test_asceneding_order(self):
        """
        rank in ascending order
        """
        res = rank(languages, score_fn, strategy="competition", reverse=True)
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 1, 1958)
        self.verify(res[1], 2, 1959)
        self.verify(res[2], 3, 1972)
        self.verify(res[3], 3, 1972)
        self.verify(res[4], 5, 1980)
        self.verify(res[5], 6, 1985)
        self.verify(res[6], 7, 1986)
        self.verify(res[7], 7, 1986)
        self.verify(res[8], 9, 1990)
        self.verify(res[9], 10, 1991)
        self.verify(res[10], 11, 1993)
        self.verify(res[11], 11, 1993)
        self.verify(res[12], 11, 1993)
        self.verify(res[13], 14, 1995)
        self.verify(res[14], 14, 1995)
        self.verify(res[15], 14, 1995)
        self.verify(res[16], 14, 1995)
        self.verify(res[17], 18, 2001)
        self.verify(res[18], 19, 2003)
        self.verify(res[19], 19, 2003)
        self.verify(res[20], 21, 2009)

    def test_start_ranking(self):
        """
        start ranking at 5
        """
        res = rank(languages, score_fn, strategy="competition", reverse=True, start=5)
        self.assertEqual(len(res), len(languages))
        self.verify(res[0], 5, 1958)
        self.verify(res[1], 6, 1959)
        self.verify(res[2], 7, 1972)
        self.verify(res[3], 7, 1972)
        self.verify(res[4], 9, 1980)
        self.verify(res[5], 10, 1985)
        self.verify(res[6], 11, 1986)
        self.verify(res[7], 11, 1986)
        self.verify(res[8], 13, 1990)
        self.verify(res[9], 14, 1991)
        self.verify(res[10], 15, 1993)
        self.verify(res[11], 15, 1993)
        self.verify(res[12], 15, 1993)
        self.verify(res[13], 18, 1995)
        self.verify(res[14], 18, 1995)
        self.verify(res[15], 18, 1995)
        self.verify(res[16], 18, 1995)
        self.verify(res[17], 22, 2001)
        self.verify(res[18], 23, 2003)
        self.verify(res[19], 23, 2003)
        self.verify(res[20], 25, 2009)
