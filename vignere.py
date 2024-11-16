import string

FORWARD = string.ascii_lowercase
REFLECT = "".join(reversed(string.ascii_lowercase))

def index(chars):
    counts = {}
    for i, char in enumerate(chars):
        counts[char] = i
    return counts

SCORES_FORWARD = index(FORWARD)
SCORES_REFLECT = index(REFLECT)

def key_char_generator(key):
    while True:
        for char in key:
            yield char

def encode(query, key, scores):
    serocs = {val: key for key, val in scores.items()}
    query = query.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    key_generator = key_char_generator(key)

    builder = ""
    for query_letter, key_letter in zip(query, key_generator):
        query_score = scores[query_letter]
        key_score = scores[key_letter]
        resultant_score = (query_score + key_score) % 26
        resultant_letter = serocs[resultant_score]
        #print(resultant_letter, query_letter, query_score, key_letter, key_score)

        builder += resultant_letter

    return builder

def decode(query, key, scores):
    serocs = {val: key for key, val in scores.items()}
    query = query.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    key_generator = key_char_generator(key)

    builder = ""
    for query_letter, key_letter in zip(query, key_generator):
        query_score = scores[query_letter]
        key_score = scores[key_letter]
        resultant_score = abs((query_score - key_score) % 26)
        resultant_letter = serocs[resultant_score]
        #print(resultant_letter, query_letter, query_score, key_letter, key_score)

        builder += resultant_letter

    return builder

#KEY = "HELLOANNE"
#QUERY = "IAMTHEKEY"
#print(decode(QUERY, KEY, SCORES))
# pexevexrc
#print(decode("LEOBWLOVKM", "IAMTHEKEYI", SCORES))
# DECIPHERME
#exit(0)


NO_LESSEN = ["godfrey", "gudfrei", "godfrey", "gadfrea"]
WITH_LESSEN = ["lessen " + word for word in NO_LESSEN]
NO_LESSEN_BACK = ["".join(reversed(godfree)) for godfree in NO_LESSEN]
WITH_LESSEN_BACK = ["".join(reversed(lessen_godfree)) for lessen_godfree in WITH_LESSEN]

MYSTERIES = [
    "Clcpapct Avgdc",
    "Psntmd",
    "Epinog Bspac",
    "Bpson Lgug",
    "Nycdkgn",
]
MYSTERIES_BACK = ["".join(reversed(mystery)) for mystery in MYSTERIES]

for scores in (SCORES_FORWARD, SCORES_REFLECT):
    for godfree_types in (NO_LESSEN, WITH_LESSEN, NO_LESSEN_BACK, WITH_LESSEN_BACK):
        for godfree in godfree_types:
            for mysteries in (MYSTERIES, MYSTERIES_BACK):
                for mystery in mysteries:
                    #print("--- %s :: %s ---" % (godfree, mystery))
                    a = decode(mystery, godfree, scores)
                    b = decode(godfree, mystery, scores)
                    az = "".join(reversed(a))
                    bz = "".join(reversed(b))
                    print("Encoded: %-20s Key: %-20s Decoded %-20s / %-20s" % (mystery, godfree, a, az))
                    print("Encoded: %-20s Key: %-20s Decoded %-20s / %-20s" % (godfree, mystery, b, bz))
