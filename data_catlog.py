'''transform data'''
import pandas as pd
import matplotlib.pyplot as plt
from transform import get_data


def country_vs_perday_total_sale():
    """total sale per day from diff country"""
    test_data_df = get_data()
    test_data_df['InvoiceDate'] = pd.to_datetime(
        test_data_df['InvoiceDate']).dt.date
    test_data_df['totalSaleAmount'] = test_data_df.apply(
        lambda row: row['UnitPrice']*row['Quantity'], axis=1)
    test_data_df = test_data_df[['totalSaleAmount', 'InvoiceDate', 'Country']].groupby(
        ['Country', 'InvoiceDate'], as_index=False).sum()
    return test_data_df


def country_vs_perday_total_customer():
    """customer perday from diff country"""
    test_data_df = get_data()
    test_data_df['InvoiceDate'] = pd.to_datetime(
        test_data_df['InvoiceDate']).dt.date
    test_data_df = test_data_df[['InvoiceDate', 'Country','CustomerID']].groupby(
        ['Country', 'InvoiceDate','CustomerID'], as_index=False).sum()
    return test_data_df

def country_vs_order_quantity():
    """country vs total quantity"""
    test_data_df = get_data()
    test_data_df['InvoiceDate'] = pd.to_datetime(
        test_data_df['InvoiceDate']).dt.date
    test_data_df = test_data_df[['Country', 'Quantity','Country']].groupby(
        ['Country','Quantity'], as_index=False).sum()
    return test_data_df

if __name__=='__main__':
    country_vs_perday_total_customer()
    country_vs_order_quantity()
    country_vs_perday_total_customer()
  