import pandas as pd
import os
import sys

path_to_data = "../data/pre-processed/"
path_to_processed = "../data/processed/"

def process_data(override=False):

    if override == True:
        for folder in os.listdir(path_to_processed):
            for file in os.listdir(path_to_processed + '/' + folder):
                os.remove(path_to_processed + '/' + folder + '/' + file)

        folders = os.listdir(path_to_data)

    else:

        corto = os.listdir(path_to_processed)
        largo = os.listdir(path_to_data)
        folders = [x for x in largo if x not in corto]


    for country in folders:

        for file in os.listdir(path_to_data + country):

            dataframe = pd.read_csv(path_to_data + '/' + country + '/' + file)

            index = 0
            for elem in dataframe.Age:
                if "-" not in elem:
                    dataframe.Age[index] = elem

                else:
                    dataframe.Age[index] = elem.split('-')[1]
                index +=1

            index = 0

            tmp_df = pd.DataFrame(columns=["Age", "Count", "Gender"])

            for elem in dataframe.iterrows():
                elem = elem[1]

                tmp_df.loc[-1] = [elem["Age"], -1 * elem["M"], "Male"]  # adding a row
                tmp_df.index = tmp_df.index + 1  # shifting index

                tmp_df.loc[-1] = [elem["Age"], elem["F"], "Female"]  # adding a row
                tmp_df.index = tmp_df.index + 1  # shifting index

            tmp_df = tmp_df.sort_index(ascending=True)  # sorting by index


            try:
                tmp_df.to_csv(f'../data/processed/{country}/{file}')

            except OSError:
                os.mkdir(f'../data/processed/{country}')
                tmp_df.to_csv(f'../data/processed/{country}/{file}')


if __name__ == "__main__":

    if sys.argv[1] == "override":
        process_data(override=True)

    else:
        process_data()
