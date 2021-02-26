"""mplda
topic modeling for the entire arch. daily corpus with multiprocessing
"""
import multiprocessing
import os

import gensim
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import pyLDAvis.gensim

from datahandler import DataHandler

# fcns

stopwords = nltk.corpus.stopwords.words()


def filter_ngram(ngram: str, n: int) -> bool:
    tag = nltk.pos_tag(ngram)
    if tag[0][1] not in ["JJ", "NN"] and tag[1][1] not in ["NN"]:
        return False
    if n == 2:
        if ngram[0] in stopwords or ngram[1] in stopwords:
            return False
    if n == 3:
        if (
            ngram[0] in stopwords
            or ngram[-1] in stopwords
            or ngram[1] in stopwords
        ):
            return False
    if "n" in ngram or "t" in ngram:
        return False
    if "PRON" in ngram:
        return False
    return True


def merge_ngram(text: str, bigrams: str, trigrams: str) -> str:
    for gram in trigrams:
        text = text.replace(gram, "_".join(gram.split()))
    for gram in bigrams:
        text = text.replace(gram, "_".join(gram.split()))
    return text


def filter_stopwords(text: str) -> str:
    return [
        word for word in text.split() if word not in stopwords and len(word) > 2
    ]


def filter_pos(text: str) -> str:
    pos = nltk.pos_tag(text)
    filtered = [word[0] for word in pos if word[1] in ["NN"]]
    return filtered


def main() -> None:

    seed = 123
    data_dir = os.path.join(os.pardir, "ArtchDaily-Share", "preproc")
    print("Loading corpus")
    corpus = DataHandler(data_dir, seed)

    # print some various information from the corpus
    print("Total Word Count: {}".format(corpus.total_words))
    print("Number of Docs in the Corpus: {}".format(corpus.total_docs))

    docs_fpath = corpus.data.keys()

    # create dictionary for filename and text
    fpath_txt = {}
    for fpath in docs_fpath:
        with open(fpath, "r") as f:
            fpath_txt[fpath] = f.read()

    # make dataframe
    df = (
        pd.DataFrame.from_dict(fpath_txt, orient="index")
        .reset_index()
        .rename(index=str, columns={"index": "file_name", 0: "text"})
    )

    corpus = df["text"]
    print("Finished loading corpus")

    min_bigram_frequency = 50

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_documents(
        [doc.split() for doc in corpus]
    )
    finder.apply_freq_filter(min_bigram_frequency)
    bigram_scores = finder.score_ngrams(bigram_measures.pmi)

    bigram_pmi = pd.DataFrame(bigram_scores)
    bigram_pmi.columns = ["bigram", "pmi"]
    bigram_pmi.sort_values(by="pmi", axis=0, ascending=False, inplace=True)

    min_trigram_frequency = 50

    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    finder = nltk.collocations.TrigramCollocationFinder.from_documents(
        [doc.split() for doc in corpus]
    )
    finder.apply_freq_filter(min_trigram_frequency)
    trigram_scores = finder.score_ngrams(trigram_measures.pmi)

    trigram_pmi = pd.DataFrame(trigram_scores)
    trigram_pmi.columns = ["trigram", "pmi"]
    trigram_pmi.sort_values(by="pmi", axis=0, ascending=False, inplace=True)

    print("cell done")

    min_pmi = 5
    max_ngrams = 500

    filtered_bigram = bigram_pmi[
        bigram_pmi.apply(
            lambda bigram: filter_ngram(bigram["bigram"], 2) and min_pmi > 5,
            axis=1,
        )
    ][:max_ngrams]

    filtered_trigram = trigram_pmi[
        trigram_pmi.apply(
            lambda trigram: filter_ngram(trigram["trigram"], 3) and min_pmi > 5,
            axis=1,
        )
    ][:max_ngrams]

    bigrams = [
        " ".join(x)
        for x in filtered_bigram.bigram.values
        if len(x[0]) > 2 or len(x[1]) > 2
    ]
    trigrams = [
        " ".join(x)
        for x in filtered_trigram.trigram.values
        if len(x[0]) > 2 or len(x[1]) > 2 and len(x[2]) > 2
    ]

    print("cell done")

    corpus_w_ngrams = corpus.copy()
    corpus_w_ngrams = corpus_w_ngrams.map(
        lambda x: merge_ngram(x, bigrams, trigrams)
    )

    print("cell done")

    p = multiprocessing.Pool()
    corpus_w_ngrams = p.map(filter_stopwords, [doc for doc in corpus_w_ngrams])
    p.close()
    print("cell done")

    p = multiprocessing.Pool()
    final_corpus = p.map(filter_pos, [doc for doc in corpus_w_ngrams])
    p.close()
    print("cell done")

    dictionary = gensim.corpora.Dictionary(final_corpus)
    dictionary.filter_extremes(no_below=10, no_above=0.20)
    corpus_bow = [dictionary.doc2bow(doc) for doc in final_corpus]
    print("cell done")

    coherence = []
    for ii in range(3, 20):
        print("lda with {} topics".format(ii))
        Lda = gensim.models.ldamulticore.LdaMulticore
        ldamodel = Lda(
            corpus_bow,
            num_topics=ii,
            id2word=dictionary,
            passes=40,
            iterations=200,
            chunksize=100,  # probably want to increase the chunksize?
            eval_every=None,
        )
        print("fit model, computing coherence")
        cm = gensim.models.coherencemodel.CoherenceModel(
            model=ldamodel,
            texts=final_corpus,
            dictionary=dictionary,
            coherence="c_v",
        )
        coherence.append((ii,cm.get_coherence()))
        print("generating tsne viz")
        p = pyLDAvis.gensim.prepare(
            ldamodel, corpus_bow, dictionary, mds="tsne"
        )
        title = "topic_tsne_{}.html".format(ii)
        pyLDAvis.save_html(p, title)
        print("done")

    n_topics = [x[0] for x in coherence]
    cm = [x[1] for x in coherence]

    plt.plot(n_topics, cm)
    plt.scatter(n_topics, cm)
    plt.title("Number of Topics vs. Coherence")
    plt.xlabel("Number of Topics")
    plt.ylabel("Coherence")
    plt.xticks(n_topics)
    plt.savefig("topic_coherence_debug.png")
    plt.close()

    pass


if __name__ == "__main__":

    main()

    pass
