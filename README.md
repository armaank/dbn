# tbd

This repo contains code to construct topic models for text data scrapped from Architecture Daily, and generative models used to create synthetic imagery trained on images from Architecture Daily and other architecture websites. 

- webscrapper? 
- topic modeling for arch-daily text corpus
- generative model (styleganv2) for arch-daily + other image corpora
- text-to-image model via stylegav2 + CLIP

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
* change the name 'archlectures'
* cleanup archlectures/topic/data folder
* change the name 'generative'
* add readme to archlecture/topic
* update readme for generative
* clean up archlectures/generative
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

Anna Konvicka

Jesse Bassett

Armaan Kohli 
