import tskit
import itertools
import numpy as np
import sys

for fn in sys.argv[1:]:
    ts = tskit.load(fn)

    # introgression is from p2 to p3
    # p1 is the outgroup

    sample_sets = [ts.samples(k) for k in [4, 3, 2, 1]]
    assert len(sample_sets) == 4
    for x in sample_sets:
        assert len(x) > 0

    def abba(ts, sample_sets):
        n = np.array([len(x) for x in sample_sets])
        nn = np.prod(n)
        def f(x):
            abba = ((n[0] - x[0]) * x[1] * x[2] * (n[3] - x[3])
                    + x[0] * (n[1] - x[1]) * (n[2] - x[2]) * x[3]) / nn
            baba = (x[0] * (n[1] - x[1]) * x[2] * (n[3] - x[3])
                    + (n[0] - x[0]) * x[1] * (n[2] - x[2]) * x[3]) / nn
            bbaa = (x[0] * x[1] * (n[2] - x[2]) * (n[3] - x[3])
                    + (n[0] - x[0]) * (n[1] - x[1]) * x[2] * x[3]) / nn
            return np.array([abba, baba, bbaa])
        x = ts.sample_count_stat(
                sample_sets,
                f,
                3,
                span_normalise=False
        )
        return x


    f4 = ts.f4(sample_sets=sample_sets)
    ab = abba(ts, sample_sets)
    D = (ab[0] - ab[1]) / (ab[0] + ab[1])

    print(f"{fn}: f4 = {f4}, ABBA = {ab[0]:.2f}, BABA = {ab[1]:.2f}, BBAA = {ab[2]:.2f}, D = {D}")
