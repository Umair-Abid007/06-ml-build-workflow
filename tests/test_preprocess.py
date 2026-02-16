import sys
import os
sys.path.append(os.path.abspath("src"))

from preprocess import preprocess_data

def test_preprocessing():
    df = preprocess_data("data/sample.csv")
    # DataFrame should not be empty
    assert not df.empty
    # No missing values should remain
    assert df.isnull().sum().sum() == 0
