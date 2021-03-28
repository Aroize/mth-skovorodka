from glob import glob
from random import random, sample

import numpy as np

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_big_themes():
    pass


def get_small_themes(big_theme):
    pass


def _count_and_save_simm_matrix():
    elmo_embs = []
    for emb_path in sorted(glob("Elmo_npys/*.npy")):
        emb = np.load(emb_path)
        elmo_embs.append(emb)
    # elmo_embs = pd.read_csv("ids.csv").to_list()
    simm = cosine_similarity(elmo_embs, elmo_embs)
    np.save("simm_matrix.npy", np.array(simm))


def get_simm_matrix():
    return np.load("simm_matrix.npy")


def get_starting_recommendations(interests, already_read, diff):
    recs = []
    articles_from_small_interests = []  # use diff +-3, if >10 resulting articles
    if len(articles_from_small_interests) >= 10:  # sort by diff
        recs.append(sample(articles_from_small_interests, 10))
    else:
        recs.append(sample(articles_from_small_interests, len(articles_from_small_interests)))

    articles_from_big_interests = []  # use diff +-3, if >10 resulting articles
    if len(articles_from_big_interests) >= 10:  # sort by diff
        recs.append(sample(articles_from_big_interests, 10))
    else:
        recs.append(sample(articles_from_big_interests, len(articles_from_big_interests)))

    all_articles = []  # anarchy
    if len(all_articles) >= 10:  # sort by diff
        recs.append(sample(all_articles, 10))
    else:
        recs.append(sample(all_articles, len(all_articles)))

    return recs


def get_simm_recommendations(id, diff, already_read):
    simm = get_simm_matrix()[id]
    if np.isclose(np.sum(simm), 0):
        raise ValueError("No such id")
    simm[already_read] = 0.0
    recs = (-simm).argsort()[:5]
    # TODO sort by diff
    return recs
