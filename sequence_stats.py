from itertools import combinations
from statistics import mean, mode

import numpy as np
from Levenshtein import distance
from textdistance import levenshtein


def base_distances(sequences, base_sequence):
    distances = []
    for sequence in sequences:
        dist = distance(str(sequence), str(base_sequence))
        distances.append(dist)
    return distances


def pair_distances(sequences):
    distances = []
    for seq1, seq2 in combinations(sequences, 2):
        dist = distance(str(seq1), str(seq2))
        distances.append(dist)
    return distances


def get_distribution_histograms(distances):
    hist = np.histogram(distances)
    hist = hist[0]
    total = sum(hist)
    parted_hist = [i / total for i in hist]
    return hist, parted_hist


def get_base_sequences_parts(database):
    rCRS_part = None
    RSRS_part = None
    base_sequences = database.collection(u'sequences').where(u'seq_len', u'==', 16569).stream()

    for base_sequence_doc in base_sequences:
        base_sequence = base_sequence_doc.to_dict()
        if base_sequence['name'] == 'NC_012920':
            rCRS_part = base_sequence['seq'][16023:16400]
        if base_sequence['name'] == 'RSRS':
            RSRS_part = base_sequence['seq'][16023:16400]

    return rCRS_part, RSRS_part
