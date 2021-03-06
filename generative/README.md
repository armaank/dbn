## Instructions

first, we'll need to run the setup.sh script. the usage is
```
setup.sh [filepath-to-dataset]
```
where `filepath-to-dataset` is the name of the directory where the dataset lives.
this might look something like this:
```
setup.sh /home/armaank/archml/data/ArtchDaily-Share/
```
this will setup a virtual environment, install requirements, and preprocess the dataset
(this last part might take a while fyi)


once this is done, we can start training a styleganv2 model. the main code is in the
`stylegan` folder. for training, the relevant scripts are `run_training.py` are
`settings.yaml`. You'll need to edit the `data_dir` field in the `settings.yaml` file to
match the same directory you suppled to the `setup.sh` script. Once that's done, you can
run:
```
python3 run_training.py settings.yaml --resume
```
this will take care of the training the model. Once you've run it, in another terminal
window run `nvidia-smi` to verify that your GPU is being used (you should see very high
usage)

You can also take a look at the `stylegan/readme.md` for more information.
