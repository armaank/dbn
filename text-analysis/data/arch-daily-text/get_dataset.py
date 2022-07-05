"""get_dataset
simple script to get the arch-daily-text dataset
"""
import os
import requests
import tarfile


def main():
    """main

    main method
    """

    # source of dataset
    url = "https://ee.cooper.edu/~kohli/dbn/datasets/arch-daily/arch-daily-text"

    archdailytext = "/arch-daily-text.tar.gz"

    # download preprocessed dataset
    src_url = url + archdailytext
    response = requests.get(src_url, stream=True)
    if response.status_code == 200:
        # use same filepath at destination as source
        os.makedirs("./arch-daily-text", exist_ok=True)
        dest_path = os.path.join("./arch-daily-text", "arch-daily-text.tar.gz")
        with open(dest_path, "wb") as f:
            f.write(response.raw.read())

    # extract tar
    dataset = tarfile.open(dest_path)
    dataset.extractall("./arch-daily-text")

    # clean up
    os.remove("./arch-daily-text/arch-daily-text.tar.gz")


if __name__ == "__main__":

    main()
