'''transform data'''
import pandas as pd
TEST_DATA = pd.read_csv('data.csv', encoding="ISO-8859-1")


def get_data():
    """return test data as DataFrame"""
    return TEST_DATA
