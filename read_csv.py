import pandas as pd
import logging
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)


def clean_data(flaw_csv_file):
    df = pd.read_csv(flaw_csv_file)
    
    # fill the null values
    # the code below is supposed to fail as there is a string value "age" in age column
    # so you need to remove that first to make it work
    # remove the non-int
    for x in df.index:
        if type(df.loc[x, 'Age']) == str:
            df.loc[x, 'Age'] = 20
    
    mean = df['Age'].mean()

    df.fillna({'Age':x}, inplace=True)

    # drop NaN
    df.dropna(inplace=True)

    # remove duplicates
    df.drop_duplicates(inplace=True)
    print(df.to_string())


def little_math(csv_file):
    df = pd.read_csv(csv_file)

    print(df.corr())

    df.plot()
    plt.show()

def read_csv_practice(csv_file):

    df = pd.read_csv('sample_data.csv')

    df_23 = df[df['Age'] == 23]

    # df has 1000 rows in total
    # print(df.head())
    # print(df.tail(10))
    print(df.info())
    # it only shows first and last 5 rows with a header
    # to show the entire table, you need to configure the default display value
    print(f'the max row is: {pd.options.display.max_rows}')
    # pd.options.display.max_rows = 1000
    # print(df)

    # df_germany.pop('Country')

    df_23.to_csv('age_23.csv', index=False)

def read_json_practice(json_file):

    df = pd.read_json(json_file)
    print(df.to_string)


def series_practice():
    
    # create a list
    a = ['first_one', 'second_one', 'third_one']
    a = {"day1": 420, "day2": 380, "day3": 390}

    # convert it into a Series
    series = pd.Series(a)

    logger.debug('this is from debug, default is warning')
    logger.critical('this is from critical')
    logger.warning(series)

def dataframe_practice(df):

    temp = df.loc['first_row']
    # print(temp)

    # when using [], it returns a dataframe
    temp_2 = df.loc[['first_row', 'second_row']]

    # print(temp_2)

    print(df)
    new_index = ['1', '2', '3']
    print(df.reindex(new_index)) 
    another_index = ['third_row', 'first_row', 'second_row']
    print(df.reindex(another_index))

    # get one column
    # print(df['calories'])
    # print(df.loc['calories'])


def mod_df(df):

    # add a column
    df['new_column'] = [5,6,7]

    # add another column in another way
    df.insert(2, 'another_column', [8,9,8])
    
    print(df)

    # delete column
    df.drop('new_column', axis=1, inplace=True)
    print(df)


def iteration(df):
    for index, row in df.iterrows():
        print(f'the index is {index} and the row is {row}')

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=['first_row', 'second_row', 'third_row'])
    
# series_practice()
# dataframe_practice()
# read_csv_practice('sample_data.csv')
# read_json_practice('generated.json')
# clean_data('flaw_data.csv')
# little_math('data.csv')
# mod_df(df)
iteration(df)