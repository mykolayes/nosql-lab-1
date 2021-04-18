from Bio import SeqIO
from io import StringIO


def find_max_and_return_key(obj):
    max_value = 0
    max_key = ''
    for key, value in obj.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


def analyze_wild_type(sequences_ref, regions):
    sequences = sequences_ref.where(u'seq_len', u'<=', 377).where(u'regions', u'array_contains_any', regions).stream()
    wild_type_stats = [{
        u'A': 0,
        u'T': 0,
        u'G': 0,
        u'C': 0,
    } for _ in range(378)]
    for sequence in sequences:
        seq = sequence.to_dict()['seq']
        for idx in range(len(seq)):
            nucleoid = seq[idx]
            if nucleoid in wild_type_stats[idx]:
                wild_type_stats[idx][nucleoid] += 1
            else:
                wild_type_stats[idx][nucleoid] = 1
    wild_type = list(map(find_max_and_return_key, wild_type_stats))
    return wild_type


def get_wild_type(sequences):
    wild_type_stats = [{
        u'A': 0,
        u'T': 0,
        u'G': 0,
        u'C': 0,
    } for _ in range(378)]
    for sequence in sequences:
        for idx in range(len(sequence)):
            nucleoid = sequence[idx]
            if nucleoid in wild_type_stats[idx]:
                wild_type_stats[idx][nucleoid] += 1
            else:
                wild_type_stats[idx][nucleoid] = 1
    wild_type = ''.join(list(map(find_max_and_return_key, wild_type_stats)))
    return wild_type
