# dbn - [Draw By Number](https://jessebassett.net/Thesis.html)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


This repo contains code used to analyze architecture lectures and construct generative models used to create synthetic architecture schematics.


## Generative Models 

## Text Analysis 

## Requirements 

## Structure
`./topic` contains code to preprocess text and generate topic models. Specifically, these topic models were made to better understand 
Architecture Daily image captions and descriptions. We built these topic models with Latent Dirichlet Allocation using 
Gensim [[1](https://www.di.ens.fr/~fbach/mdhnips2010.pdf), [2](https://radimrehurek.com/gensim/index.html)], and visualized said models with pyLDAVis
[[3](https://github.com/bmabey/pyLDAvis)]. We found that loosely, for sufficiently many topics, the topics represented architectural programs. You can examine 
interactive topic models [here](https://ee.cooper.edu/~kohli/topics/), a sample is pictured in Fig. 1. See `./topic/readme.md` for instruction to replicate
our models. 

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
* update text analysis notebooks to colab
* clean up archlectures/generative
* add docs to datsets
* add hylinks to authors
* update ack

## Acknolwedgments
We'd like to thank (clip-glass authors, stylegan2-pytorch authors, clip, more here?)
for providing open source implementations of algorithms used for this project. 

## References
[1] https://www.di.ens.fr/~fbach/mdhnips2010.pdf

[2] https://radimrehurek.com/gensim/index.html

[3] https://github.com/bmabey/pyLDAvis

[4] https://arxiv.org/abs/1912.04958

[5] https://github.com/Tetratrio/stylegan2_pytorch

[6] https://arxiv.org/abs/2103.00020

[7] https://arxiv.org/abs/2102.01645


## Authors

Jesse Bassett

Anna Konvicka

Armaan Kohli 
