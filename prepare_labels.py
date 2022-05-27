import os
from os import path
import pandas as pd
import csv

def create_new_labels_file():
    """
    Creates new_labels.csv file if it does not exist
    """

    if not path.exists('new_labels.csv'):
        with open('new_labels.csv', 'w') as fp:
            print("Created new file")
            pass

def get_frame_names():
    """
    Gets all the frame names into out
    : returns all frame names
    """
    base_dir = "./data"

    dir_list = os.listdir(base_dir)

    out = []
    for i in dir_list:
        dir_list_2 = os.listdir(base_dir + '/' + str(i))

        for j in dir_list_2:
            out.append(os.path.splitext(j)[0])

    # sort the list based on clip names
    out.sort(key = lambda x: x[5:11])

    counter = 0
    for i in range(len(out)):
        out[counter: counter + 6] = sorted(out[counter: counter + 6], key = lambda x: x[-1])

        counter += 6
        i += 6
    return out

def add_labels_new_file():
    """
    Adds new frames and corresponding clips in new_labels csv
    """
    
    out = get_frame_names()

    new_df = pd.DataFrame()

    new_df["clip_name"] = out

    reader = list(csv.reader(open("./surgtoolloc2022_dataset/_release/training_data/labels.csv")))
    row_labels = []
    for row in reader[1:]:
        for i in range(6):
            row_labels.append(row[2])


    new_df["tools_present"] = row_labels

    new_df.to_csv('new_labels.csv')

add_labels_new_file()


