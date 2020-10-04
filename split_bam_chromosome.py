#Split the MC38 tumor bam file file by chromosome by using pysam
import pysam

with pysam.AlignmentFile("/home/rjing/Downloads/M3808O_SHL108A1_S10_001.markdup.realigned.bam") as bf:
    chromosomes = zip(bf.references, bf.lengths)

def split_PySam_by_chromosome(info):
    chromosome, length = info
    with pysam.AlignmentFile("/home/rjing/Downloads/M3808O_SHL108A1_S10_001.markdup.realigned.bam") as bf:
        with pysam.AlignmentFile(
                "MC38_%s.bam" % chromosome,
                "wb",
                template = bf) as outf:
            for alignment in bf.fetch(reference=chromosome):
                outf.write(alignment)

list(map(split_PySam_by_chromosome, chromosomes))