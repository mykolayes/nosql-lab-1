class SequenceDocument(object):
    def __init__(self, version, seq_len, fasta, seq, name=None, population=0,
                 regions=None, location=None):
        if regions is None:
            regions = [u'UND']
        if name is None:
            name = version
        if location is None:
            location = []
        self.version = version
        self.seq_len = seq_len
        self.fasta = fasta
        self.name = name
        self.population = population
        self.regions = regions
        self.location = location
        self.seq = seq

    @staticmethod
    def from_dict(source):
        document = SequenceDocument(
            version=source[u'version'],
            seq_len=source[u'seq_len'],
            fasta=source[u'fasta'],
        )
        if u'name' in source:
            document.name = source[u'name']
        if u'population' in source:
            document.population = source[u'population']
        if u'regions' in source:
            document.regions = source[u'regions']
        if u'location' in source:
            document.regions = source[u'location']
        return document

    def to_dict(self):
        return {
            u"version": self.version,
            u"seq_len": self.seq_len,
            u"fasta": self.fasta,
            u"name": self.name,
            u"population": self.population,
            u"regions": self.regions,
            u"seq": self.seq,
            u"location": self.location
        }

    def __repr__(self):
        return(
            f'Sequence Document(\
                version={self.version}, \
                fasta={self.fasta}, \
                seq={self.seq}, \
                name={self.name}, \
                population={self.population}, \
                seq_len={self.seq_len}, \
                regions={self.regions}\
            )'
        )