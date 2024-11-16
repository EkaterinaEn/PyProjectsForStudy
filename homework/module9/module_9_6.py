import itertools


def all_variants(text):
    for l in range(1, len(text) + 1):
        for t in list(itertools.combinations(text, l)):
            yield ''.join(t)


variants = all_variants("abc")

for i in variants:
    print(i)
