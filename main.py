import firebase_admin
from firebase_admin import credentials, firestore

from database_population import get_base_sequence_from_file, get_sequences_from_file
from excel_template import create_xls_file
from sequence_stats import get_base_sequences_parts
from wild_type import analyze_wild_type


def populate_sequences(database, sequences):
    for sequence in sequences:
        database.collection(u'sequences').add(sequence.to_dict())


def load_data_into_database(database):
    rCRS_sequence = get_base_sequence_from_file('rCRS.gb', 'genbank')
    populate_sequences(database, [rCRS_sequence])
    RSRS_sequence = get_base_sequence_from_file('RSRS.fasta', 'fasta')
    populate_sequences(database, [RSRS_sequence])
    sequences = get_sequences_from_file('sequences.gb', 'genbank')
    populate_sequences(database, sequences)


def populate_sequences_wild_type(database, regions):
    sequence_ref = database.collection(u'sequences')
    for region in regions.keys():
        wild_type_seq = ''.join(analyze_wild_type(sequence_ref, [region]))
        print(wild_type_seq)
        data = {
            u'seq': wild_type_seq,
            u'regions': [region],
            u'version': 1
        }
        db.collection(u'wild_types').add(data)


if __name__ == '__main__':
    cred = credentials.Certificate("nosql-bd-lab-3802d14487be.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    # RUN TIME = 51 sec
    # load_data_into_database(db)

    regions_1_task = {
        "Ukraine: Ivano-Frankovskaya oblast'": "IF",
        "Russia: Belgorodskaya oblast', Krasnogvardeysky rayon": "BK",
        "Russia: Belgorodskaya oblast', Grayvoronsky rayon": "BG",
        "Ukraine: L'vovskaya oblast', Stryi": "ST",
        "Ukraine: Cherkasskaya oblast'": "CH",
        "Ukraine: Khmelnitskaya oblast'": "KHM"
    }

    # RUN TIME = 3 sec
    populate_sequences_wild_type(db, regions_1_task)

    # rCRS_seq_part, RSRS_seq_part = get_base_sequences_parts(db)

    create_xls_file(db, regions_1_task)
