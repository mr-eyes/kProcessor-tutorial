import kProcessor as kp

class kfIterator:
    def __init__(self, KF):
        self.KF = KF.kf
        self.kf_type = KF.kf_type
        if KF.kf_type == "colored":
            self.CKF = KF.ckf
        self.it = KF.kf.begin()
        self.end = KF.kf.end()

    def __next__(self):

        if self.it != self.end:
            kmer_str = self.it.getKmer()
            kmer_hash = self.it.getHashedKmer()
            kmer_count = self.it.getCount()

            if self.kf_type == "colored":
                kmer_sources = self.CKF.getKmerSourceFromColor(kmer_count)
                kmer = (kmer_str, kmer_sources)
            else:
                kmer = (kmer_str, kmer_count)
            
            self.it.next()
            return kmer

        else:
            raise StopIteration

class KF_iter:
    def __init__(self, KF):
        self.kf = KF
        if "colored" in str(type(KF)):
            self.kf_type = "colored"
            self.ckf = KF
            self.kf = KF.getkDataFrame()
        else:
            self.kf_type = "default"
            self.kf = KF

    def __iter__(self):
        return kfIterator(self)