# import unittest

# class KnownValues(unittest.TestCase):
#     known_values = (
#         ('', (None, None, None, None)),
#         ('From £28,000 to £32,000 per annum', (28000, 32000, "£", "year")),
#         ('Up to €42,000 per annum ', (None, 42000, "€", "year")),
#         ('₤3500 per month'), (None, 3500, "£", "month")),
#         ('Up to £400 per day'), (None, 400, "£", "day")),

#     )

#     def test_to_renumeration(self):
#         for text, renumeration in self.known_values:
#             result = determine_date(text)
#             self.assertEqual(result, date)

# if __name__ == '__main__':
#     unittest.main()