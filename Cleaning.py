import pandas as pd


def read_and_clean(xls, header, drop_col, csv):
    df = pd.read_excel(xls, header=header)
    df_2 = pd.read_csv(csv)
    crosswalk = df_2.set_index('old_column')['new_column'].to_dict()
    cols_to_multiply = [6, 9, 12] + list(range(15, 24)) + [-1]
    df.iloc[:, cols_to_multiply] = df.iloc[:, cols_to_multiply
                                           ].apply(pd.to_numeric,
                                                   errors='coerce')
    df.iloc[:, cols_to_multiply] *= 0.00386102  # unit from hect to mi^2
    df = df.rename(columns=crosswalk)  # original file in portuguese
    df.drop(df.columns[drop_col], axis=1, inplace=True)  # drop duplicate cols
    return df


df = read_and_clean('Tabela-Os_Invasores.xlsx', 1, 24, 'crosswalk.csv')
# Original Data Source: de Olho nos Ruralistas 'Os Invasores' Report
# https://deolhonosruralistas.com.br/2023/05/11/report-invaders-reveals-companies-and-sectors-behind-overlaps-in-indigenous-lands-in-brazil/

df.to_csv('invaders.csv', index=False, header=True)
