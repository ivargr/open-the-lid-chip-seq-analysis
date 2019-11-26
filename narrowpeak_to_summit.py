# Simple script to convert narrowpeak format to bed format (where position is the peak summit)
import sys

narrowpeaks = open(sys.argv[1])

for line in narrowpeaks:
    l = line.split()
    chrom = l[0]
    start = int(l[1])
    end = int(l[2])

    summit_offset = int(l[9])
    score = l[8]

    print("%s\t%d\t%d\t%s\t%s\t%s" % (chrom, start + summit_offset, start + summit_offset + 1, l[3], score, l[5]))

narrowpeaks.close()
