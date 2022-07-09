"""get_models
simple script to get the Adaily-A and Adaily-B models
"""

import os
import tarfile
import requests


def main():
    """main

    main method
    """

    # source of dataset
    url = "https://ee.cooper.edu/~kohli/dbn/models/saved_directions/"
    fname = "saved_directions.tar.gz"

    # download tarfile

    src_url = os.path.join(url, fname)

    response = requests.get(src_url, stream=True)

    if response.status_code == 200:
        print("success")
        # use same filepath at destination as source
        os.makedirs("./saved_directions", exist_ok=True)
        dest_path = os.path.join("./saved_directions", fname)
        with open(dest_path, "wb") as f:
            f.write(response.raw.read())

    # extract tar
    dataset = tarfile.open(dest_path)
    dataset.extractall("./saved_directions/")

    # clean up
    os.remove(f"./saved_directions/{fname}")


if __name__ == "__main__":

    main()
