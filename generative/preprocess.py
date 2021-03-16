"""preprocess
resizes images, converts to rgb colorspace
"""
import glob
import os
import sys

import PIL

from PIL import Image
from PIL import PngImagePlugin

# large jpg nonsense
LARGE_ENOUGH_NUMBER = 100
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024 ** 2)


def preprocess_img_dset(fpath: str, w: int = 256, h: int = 256) -> None:
    """recursively preprocesses all .jpg images in a given filepath. we resize
    images to wxh w/o preserving aspect ratio, convert to rbg if the image
    isn't rgb already and re-save in-place.

    somthing to explore in the future is filtering by name to remove different
    types of input images (i.e. photos). but for now, let's leave it up to
    the ineffectiveness of GANs to solve this problem for us.

    Parameters
    ----------
    fpath: str
        root directory that contains all of the images
    w: int
        desired width to crop to
    h: int
        desired height to crop to

    Returns
    -------
    none

    """

    print("starting pre-processing")
    for filename in glob.iglob(fpath + "**/*.jpg", recursive=True):
        if os.path.isfile(filename):
            try:
                img = Image.open(filename)
                img = img.resize((w, h))

                #if img.mode != "RGB":
                img = img.convert("LA") # converts to grayscale
                img.save(filename, "JPEG")

            except PIL.UnidentifiedImageError:
                os.remove(filename)
                continue

    print("done")

    pass


def main(fpath):

    preprocess_img_dset(fpath, 256, 256)

    pass


if __name__ == "__main__":

    fpath = sys.argv[1]

    main()

    pass
