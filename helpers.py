import pandas as pd


def growth(df,processor_name):
    df = df.sort_index(ascending = False)
    growth = df.pct_change()
    growth = growth.dropna()
    print('Mean {} growth over 10 years: {}'.format(processor_name, growth.mean()))
    return growth.mean()