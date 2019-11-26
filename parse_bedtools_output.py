# Script that parses the output from bedtools closest into a bed file with segments covering the area between the peaks
import sys

distances = open(sys.argv[1])
out_file = open(sys.argv[2], "w")

for pair in distances:
    d = pair.split()
    if d[-1] == "-1":
        print("Not found pair for %s" % pair)
        continue
    if len(d) < 13:
        print("Line is short, skipping: %s" % d)
        continue

    start1 = int(d[1])
    end1 = int(d[2])
    name1 = d[3]
    score1 = d[4]

    start2 = int(d[7])
    end2 = int(d[8])
    name2 = d[9]
    score2 = d[10]

    score = 1000 - int(d[-1])

    start = min(start1, start2)
    end = max(end1, end2)

    out_file.writelines(
        ["%s\t%d\t%d\t%s\t%d\t.\t%s\t%s\n" % (d[0], start, end, name1 + "-" + name2, score, score1, score2)])

distances.close()
out_file.close()

