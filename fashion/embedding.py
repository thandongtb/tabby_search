import pickle
import numpy as np
from tqdm import tqdm
import os

class Embedding(object):
    def __init__(self, data_path = None):
        self.data = []
        self.embs = []
        self.paths = []
        self.img_ids = []
        if data_path and os.path.exists(data_path):
            self.data = pickle.load(open(data_path, "rb"))
            for d in self.data:
                self.img_ids.append(d['img_id'])
                self.paths.append(d['url'])
                self.embs.append(d['embed'])

    def embed_to_str(self, embed_raw):
        embed_str = ""
        for i in range(len(embed_raw)):
            prefix = "p"
            if embed_raw[i] < 0:
                prefix = "n"
            if int(embed_raw[i]) != 0:
                for j in range(0, np.abs(int(embed_raw[i]))):
                    embed_str += "{}{} ".format(prefix, i + 1)

        return embed_str

    def get_data(self):
        return self.data

    def get_embs(self):
        return self.embs

    def get_paths(self):
        return self.paths

    def get_img_ids(self):
        return self.img_ids

    def quantization_factor(self, Q=50, embed=None):
        words = []
        if embed:
            embed = list(np.floor(np.multiply(embed, Q)))

            for e in tqdm(embed):
                words.append(self.embed_to_str(e))
        return words

