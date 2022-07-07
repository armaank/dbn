# dbn - [Draw By Number](https://jessebassett.net/Thesis.html)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


This repo contains code used to analyze architecture prose and construct generative models used to create synthetic architecture schematics.


## Generative Models 

## Text Analysis 

Basic [topic models](https://colab.research.google.com/github/armaank/dbn/blob/main/text-analysis/topicmodel.ipynb) and [clustering](https://colab.research.google.com/github/armaank/dbn/blob/main/text-analysis/umap.ipynb) of architecture lectures and a cohort of architecture project descriptions. 



## Requirements 

## Structure 

Inside `./generative`, we have code to build generative models from image corpora. We first trained a StyleGan2 [[4](https://arxiv.org/abs/1912.04958), 
[5](https://github.com/Tetratrio/stylegan2_pytorch)] on an image corpus scrapped from architecture daily as well as other sources. We then developed a text to 
image model using our trained StyleGan2 and CLIP [[6](https://arxiv.org/abs/2103.00020)], using a latent space search method developed by 
[[7](https://arxiv.org/abs/2102.01645)]. Fig. 2 shows some raw samples from our text to image model, generated from 
[this colab notebook](https://colab.research.google.com/drive/1p8mfxWCvkI3pbgRiYIxsKjoFcEUhw0id#scrollTo=bfXK5iLY3rjQ).
See `./generative/readme.md` for instructions to replicate our generative models. 


## TODO:
* update colab link
* add photo 
* host dataset on ee site
* host models on ee site
* get colab notebooks working
* document colab notebooks
* clean up archlectures/generative
* add docs to datsets

## Acknolwedgments
We'd like to thank Federico Galatolo and the authors of [CLIP-GLASS](https://github.com/galatolofederico/clip-glass),
for providing open source implementations of their methods and guidance. 

## Authors

Jesse Bassett

Anna Konvicka

Armaan Kohli 
