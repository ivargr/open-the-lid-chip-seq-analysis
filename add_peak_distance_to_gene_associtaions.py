import logging
import sys

peak_pairs_file = open(sys.argv[1])
gene_associations = open(sys.argv[2])

peak_to_peak_distances = {}
for line in peak_pairs_file:
    l = line.split()
    pair_id = l[3]
    peaks_distance = 1000 - int(l[4])

    peak_to_peak_distances[pair_id] = peaks_distance


for i, line in enumerate(gene_associations):
    if i == 0:
        assert line.startswith("Region"), "Has no header"
        print(line.strip() + "\t.\t.\tPeak_to_peak_distance")
        continue

    l = line.split()
    pair_id = l[10]
    l.append(str(int(peak_to_peak_distances[pair_id])))

    print("\t".join(l))

    

