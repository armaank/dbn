# Name - tbd

This repo contains code to construct topic models for text data scrapped from Architecture Daily, and generative models used to create synthetic imagery trained on images from Architecture Daily and other architecture websites. 

- webscrapper? 
- topic modeling for arch-daily text corpus
- generative model (styleganv2) for arch-daily + other image corpora
- text-to-image model via styleganv2 + CLIP

## Structure
Inside `./topic`, we have code to preprocess text and generate topic models. Specifically, these topic models were made to better understand Architecture Daily image captions and descriptions. We built these topic models with Latent Dirichlet Allocation [ref to blei paper, gensim], and visualized said models with pyLDAVis [ref to pyldavis]. We found that loosely, for sufficiently many topics, the topics represented architectural programs. See Fig. [ref] for a sample and see [that website] for interactive samples. See `./topic/readme.md` for instructionto replicate our models. 


Inside `./generative`, we have code build generative models from image corpora. We first trained a StyleGanV2 [ref nvidia, other impl.] on an image corpus scrapped from architecture daily as well as other sources. We then developed a text to image model using our trained StyleGanV2 and CLIP [ref openai], using 
a genetic latent space search method developed by [clip-glass]. See below for raw samples from our text to image model, as well as a colab notebook. See `./generative/readme.md` for instructions to replicate our generative models. 



## TODO:
* change the name 'archlectures'
* cleanup archlectures/topic/data folder
* change the name 'generative'
* add readme to archlecture/topic
* update readme for generative
* clean up archlectures/generative
* add references


## References

## Authors
Anna Konvicka
Jesse Bassett
Armaan Kohli 
