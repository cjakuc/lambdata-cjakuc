import unittest
from my_lambdata.my_mod import DfFancy
import pandas as pd
from sklearn.model_selection import train_test_split


# Test DfFancy class
class TestMyMod(unittest.TestCase):

    def test_train_val_test(self):
        df = pd.DataFrame(data={'target': [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                                'cat1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                                'cat2': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']})
        df_fancy = DfFancy(df)
        train, test = train_test_split(df, random_state=42)
        train, val = train_test_split(train, random_state=42)
        train1, val1, test1 = df_fancy.set_train_val_test()
        self.assertEqual(train1, train)
        self.assertEqual(val1, val)
        self.assertEqual(test1, test)


if __name__ == '__main__':
    unittest.main()
