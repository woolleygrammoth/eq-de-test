import unittest
from fetch import fetch_raw_data

class TestSetup(unittest.TestCase): 
    def test_fetch_raw_data(self): 
        raw = fetch_raw_data()
        # select a row to probe the structure
        test_row = raw['list'][0] 
        # check that our columns are where we expect
        self.assertTrue('dt' in test_row)
        self.assertTrue('main' in test_row)
        self.assertTrue('temp' in test_row['main'])
        self.assertTrue('temp_min' in test_row['main'])
        self.assertTrue('temp_max' in test_row['main'])
        self.assertTrue('wind' in test_row)
        self.assertTrue('speed' in test_row['wind'])

if __name__ == '__main__': 
    unittest.main()