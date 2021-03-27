from glob import glob
import numpy as np

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_starting_recommendations(interests, already_read, age):
    pass


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

df = pd.read_csv("ids.csv")
print(df.head())
del df["a"]
print(df.head())
df.to_csv("ids.csv", index=False)