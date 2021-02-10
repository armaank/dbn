"""datahandler for csv files
note: I really should've done this with datahandler.py
only accomodates working with each csv file as a single blob of text
"""
import csv
import functools
import operator
import os
import re

import numpy as np

from chardet import detect  # for file format codecs


def get_encoding_type(fpath: str) -> str:
    """determines the encoding scheme used to save a particular file.
    Parameters
    ----------
    fpath: str
        pathname of the file
    Returns
    -------
    encoding_type: str
        name of the detected encoder
    """

    # open file with read binary permissions
    with open(fpath, "rb") as f:
        rawdata = f.read()

    encoding_type = detect(rawdata)["encoding"]

    return encoding_type


def preprocess(fpath: str, save_dir: str):
    """preprocess text from corpus. re-encodes file as utf-8 to account for
    non-conforming characters. removes extraneous timestamps, braces and
    quasi-json formatting. saves preprocessed text into a new directory
    Parameters
    ----------
    fpath: str
        pathname of text file
    save_dir: str
        path to a directory used to save the preprocessed corpus
    Returns
    -------
    none
    """

    # determine the codec used by the text file
    codec = get_encoding_type(fpath)

    tmp = "tmp.txt"


    #re-encode file as utf-8
    try:
        # open text file w/ read permissions, temp file w/ write permissions
        with open(fpath, "r", encoding=codec) as f, open(
            tmp, "w", encoding="utf-8"
        ) as e:

            text = f.read()
            f.close()

            e.write(text)
            e.close()

        # remove old encoding file and rename temporary file
        os.remove(fpath)
        os.rename(tmp, fpath)

    except UnicodeDecodeError:
        print("Decode Error")

    except UnicodeEncodeError:
        print("Encode Error")


    # create directory to save preprocessed text

    new_dir = os.path.join(save_dir, os.path.basename(os.path.dirname(fpath)))

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    new_fpath = os.path.join(new_dir, os.path.basename(fpath))
    new_fpath = new_fpath.replace(".csv", ".txt")
    # open text file for reading and writing, create and open target text file
    # for reading and writing
    with open(fpath, "r+", encoding="utf-8") as f, open(
        new_fpath, "w+", encoding="utf-8"
    ) as e:

        # regex for determing where 'start' label in json-like format begins
        #regex = r"((\'|\"), (?:^|\W)start(?:$|\W))"
        #pattern = re.compile(regex)

        # loop through all lines in the text file
        for line in csv.reader(f):

            line = line.pop()
            # find regex match in the line
            #m = pattern.search(line)

            #line = str(line)
            # remove newlines from MIT/GSD
            #line = line.replace('\\n', " ")

            # removes "{'text': '" and everything after  "'/", 'start'",
            # re-adds newline
            #line = line[10: m.span()[0]] + "\n"

            # write cleaned line to the destination file
            e.writelines(line)

def main():

    cur_dir = os.getcwd()
    data_dir = os.path.join(cur_dir,"..", "web_data","Projects")
    save_dir = os.path.join(data_dir, "..","preproc")

    # loop through each directory and preprocess the files
    for dir_name in os.listdir(data_dir):

        print("preprocessing {} project".format(dir_name))

        dir_path = os.path.join(data_dir, dir_name)

        for fname in os.listdir(dir_path):
            if "Text.csv" in fname:
                fpath = os.path.join(dir_path, fname)
                preprocess(fpath, save_dir)
            else:
                pass

    print("done")


if __name__ == "__main__":

    main()
