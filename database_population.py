from Bio import SeqIO

from SequenceDocument import SequenceDocument


def get_base_sequence_from_file(file_path, file_format):
    for sequence_record in SeqIO.parse(file_path, file_format):
        seq_id = str(sequence_record.id)
        seq = str(sequence_record.seq.upper())
        document = SequenceDocument(
            version=seq_id,
            seq_len=len(seq),
            fasta=sequence_record.format('fasta'),
            seq=str(seq),
            name=sequence_record.name
        )
        return document


def get_sequences_from_file(file_path, file_format):
    documents = []
    for sequence_record in SeqIO.parse(file_path, file_format):
        seq = sequence_record.seq.upper()
        location = []
        regions = None
        for feature in sequence_record.features:
            if feature.type == 'source':
                start = feature.location.start
                end = feature.location.end
                regions = feature.qualifiers.get('country', ['UND'])
                location = [start, end]
        document = SequenceDocument(
            version=str(sequence_record.id),
            seq_len=len(seq),
            fasta=sequence_record.format('fasta'),
            location=location,
            regions=regions,
            seq=str(seq)
        )
        documents.append(document)
    return documents
