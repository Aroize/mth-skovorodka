from glob import glob
from random import random, sample

import numpy as np

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from serv.database import db_helper


def _count_and_save_simm_matrix():
    elmo_embs = []
    for emb_path in sorted(glob("Elmo_npys/*.npy")):
        emb = np.load(emb_path)
        elmo_embs.append(emb)
    simm = cosine_similarity(elmo_embs, elmo_embs)
    np.save("simm_matrix.npy", np.array(simm))


def get_simm_matrix():
    return np.load("simm_matrix.npy")


def get_starting_recommendations(u_id):
    # part_1 = []
    # articles_from_small_interests = []  # use diff +-3, if >10 resulting articles
    # if len(articles_from_small_interests) >= 10:  # sort by diff
    #     part_1.append(sample(articles_from_small_interests, 10))
    # else:
    #     part_1.append(sample(articles_from_small_interests, len(articles_from_small_interests)))

    articles_from_big_interests = db_helper.get_diff_range(u_id)  # use diff +-3, if >10 resulting articles
    part_2 = []
    if len(articles_from_big_interests) >= 20:  # sort by diff
        part_2.append(sample(articles_from_big_interests, 20))
    else:
        part_2.append(sample(articles_from_big_interests, len(articles_from_big_interests)))
    for i in range(len(part_2)):
        part_2[i] = {"id": part_2[i], "diff": db_helper.get_diff(part_2[i])}
    part_2 = sorted(part_2, key=lambda k: k["diff"])
    if len(part_2) == 0:
        print("Empty rec2")

    all_articles = db_helper.get_all_articles()  # anarchy
    part_3 = []
    if len(all_articles) >= 10:  # sort by diff
        part_3.append(sample(all_articles, 10))
    else:
        part_3.append(sample(all_articles, len(all_articles)))
    for i in range(len(part_3)):
        part_3[i] = {"id": part_3[i], "diff": db_helper.get_diff(part_3[i])}
    part_3 = sorted(part_3, key=lambda k: k["diff"])
    if len(part_3) == 0:
        print("Empty rec3")

    recs = part_2 + part_3
    return recs


def get_simm_recommendations(id, already_read):
    simm = get_simm_matrix()[id]
    if np.isclose(np.sum(simm), 0):
        raise ValueError("No such id")
    simm[already_read] = 0.0
    recs = (-simm).argsort()[:5]
    for i in range(len(recs)):
        recs[i] = {"id": recs[i], "diff": db_helper.get_diff(recs[i])}
    recs = sorted(recs, key=lambda k: k["diff"])
    return recs
