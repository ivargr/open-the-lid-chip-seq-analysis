import sys
import logging
logging.basicConfig(level=logging.INFO)

with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
    
        if i % 1000 == 0:
            logging.info("%d processed" % i)

        data = line.split()
        distance = float(data[6])
        if data[5] == "UPSTREAM":
            # Always 5'far, because "near" her is promoter
            data[5] = "5'far"
        elif data[5] == "DOWNSTREAM":
            if distance < 5000:
                data[5] = "3'near"
            else:
                data[5] = "3'far"
        elif data[5] == "INTRON" and data[4] == "1":
            data[5] = "1st_INTRON"


        print('\t'.join(data).strip())



        
