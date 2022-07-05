"""get_dataset
simple script to get the arch-lecture dataset
"""
import os
import requests
import tarfile


def main():
    """main

    main method
    """

    # source of dataset
    url = "https://ee.cooper.edu/~kohli/dbn/datasets/arch-lectures/"

    preprocessed = "preprocessed/preprocessed.tar.gz"
    raw_data = "raw_data/raw_data.tar.gz"

    # download preprocessed dataset
    src_url = url + preprocessed
    response = requests.get(src_url, stream=True)
    if response.status_code == 200:
        # use same filepath at destination as source
        os.makedirs("./preprocessed", exist_ok=True)
        dest_path = os.path.join("./preprocessed", "preprocessed.tar.gz")
        with open(dest_path, "wb") as f:
            f.write(response.raw.read())

    # extract tar
    dataset = tarfile.open(dest_path)
    dataset.extractall("./preprocessed")

    # clean up
    os.remove("./preprocessed/preprocessed.tar.gz")

    # download raw dataset
    src_url = url + raw_data

    response = requests.get(src_url, stream=True)
    if response.status_code == 200:

        os.makedirs("./raw_data", exist_ok=True)
        dest_path = os.path.join("./raw_data", "raw_data.tar.gz")
        with open(dest_path, "wb") as f:
            f.write(response.raw.read())

    # extract tar
    dataset = tarfile.open(dest_path)
    dataset.extractall("./raw_data")

    # clean up
    os.remove("./raw_data/raw_data.tar.gz")


if __name__ == "__main__":

    main()
