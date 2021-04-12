import kProcessor as kp

class kfIterator:
    def __init__(self, KF):
        self.it = KF.kf.begin()
        self.end = KF.kf.end()

    def __next__(self):
        if self.it != self.end:
            kmer = (self.it.getKmer(), self.it.getCount())
            self.it.next()
            return kmer

        else:
            raise StopIteration

class KF_iter:
    def __init__(self, KF):
        self.kf = KF

    def __iter__(self):
        return kfIterator(self)

