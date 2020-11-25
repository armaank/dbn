"""datahandler.py
manages preprocessing and organization of all datasets

"""
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

    # re-encode file as utf-8
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

    # open text file for reading and writing, create and open target text file
    # for reading and writing
    with open(fpath, "r+", encoding="utf-8") as f, open(
        new_fpath, "w+", encoding="utf-8"
    ) as e:

        # regex for determing where 'start' label in json-like format begins
        regex = r"((\'|\"), (?:^|\W)start(?:$|\W))"
        pattern = re.compile(regex)

        # loop through all lines in the text file
        for line in f.readlines():

            # find regex match in the line
            m = pattern.search(line)

            line = str(line)
            # remove newlines from MIT/GSD
            line = line.replace('\\n', " ")

            # removes "{'text': '" and everything after  "'/", 'start'",
            # re-adds newline
            line = line[10: m.span()[0]] + "\n"

            # write cleaned line to the destination file
            e.writelines(line)


class DataHandler:
    """performs basic tasks to organize a dataset"""

    def __init__(self, root_dir: str, seed: int):
        """sets up Datahandler class to process dataset

        Parameters
        ----------
        root_dir: str
            root directory of the dataset
        seed: int
            random seed for dataset permutation
        Returns
        -------
        none

        """
        self.seed = seed
        np.random.seed(seed)

        self.root_dir = root_dir

        self.inst_dict = self.get_insts()
        self.n_inst = len(self.inst_dict)

        self.stats = self.get_stats()

        paths = []
        inst = []
        for inst_dir in self.inst_dict.values():
            for fname in os.listdir(inst_dir):
                paths.append(os.path.join(inst_dir, fname))
                inst.append(os.path.basename(inst_dir))

        # randomly permute corpus
        #indicies = np.arange(paths.shape[0])
        #np.random.shuffle(indicies)
        #paths = paths[indicies]
        #inst = inst[indicies]

        self.data = dict(zip((paths), (inst)))

    def get_insts(self) -> dict:
        """gets the subdirectories of the data, cooresdponding to each
        institution in the corpus

        Parameters
        ----------
        self

        Returns
        -------
        inst_dict: dict
            a dictionary with the name of each institution in the corpus and
            the cooresponding path to the data

        """
        entries = os.listdir(self.root_dir)

        if not entries:
            return "No data"
            exit()

        # loop through all files inthe directory, remove all regualar files,
        # keep directories
        for entry in entries:
            entry_path = os.path.join(self.root_dir, entry)
            if not os.path.isdir(entry_path):
                entries.remove(entry)

        # make dictionary with institution name as keys and the datapath as
        # values
        inst_dict = dict(
            zip((entries), (os.path.join(self.root_dir, entry) for entry in entries))
        )

        return inst_dict

    def get_stats(self) -> dict:
        """computes some basic statistics about a given corpus. number of words
        and docs per institution and total number of words and docs in the
        corpus

        Parameters
        ----------
        self

        Returns
        -------
        corpus_stats: list
            a list of dictionaries containing the number of words and documents
            for each institution in the dataset

        """
        corpus_stats = []

        # loop through all directories in the dataset
        for ii, inst in enumerate(self.inst_dict.keys()):

            docs = os.listdir(self.inst_dict[inst])
            # compute the number of documents for the institution
            n_docs = len(docs)
            # init word count
            wc = 0

            # loop through all documents in in the subdir, compute word count
            for doc in docs:
                with open(os.path.join(self.inst_dict[inst], doc)) as f:
                    for line in f:
                        words = str(line).split()
                        wc += len(words)

            # append statistics to the corpus stats list
            corpus_stats.append(
                dict(zip((["inst", "n_docs", "wc"]), ([inst, n_docs, wc])))
            )

        # compute total number of words in the entire corpus
        self.total_words = functools.reduce(
            operator.add, [inst_data["wc"] for inst_data in corpus_stats]
        )

        # compute the total number of documents in the entire corpus
        self.total_docs = functools.reduce(
            operator.add, [inst_data["n_docs"] for inst_data in corpus_stats]
        )

        return corpus_stats


def main():

    cur_dir = os.getcwd()
    data_dir = os.path.join(cur_dir, "data")
    save_dir = os.path.join(data_dir, "preproc")

    # loop through each directory and preprocess the files
    for dir_name in os.listdir(data_dir):

        print("preprocessing {} lectures".format(dir_name))

        dir_path = os.path.join(data_dir, dir_name)

        for fname in os.listdir(dir_path):

            fpath = os.path.join(dir_path, fname)

            preprocess(fpath, save_dir)

    print("done")


if __name__ == "__main__":

    main()
