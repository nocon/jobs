from .determine_date import determine_date
import unittest
import datetime

class KnownValues(unittest.TestCase):
    known_values = (
        ('Aug 3', datetime.datetime(2016, 8, 3)),
        ('09 Oct 2016 ', datetime.datetime(2016, 10, 9)),
        ('Posted Aug 19', datetime.datetime(2016, 8, 19)),
        ('Today', datetime.date.today()),
    )

    def test_to_date(self):
        for text, date in self.known_values:
            result = determine_date(text)
            self.assertEqual(result, date)

if __name__ == '__main__':
    unittest.main()