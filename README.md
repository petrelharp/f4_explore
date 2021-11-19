0. Prerequisites: SLiM, tskit.

1. To simulate an introgression percentage of 0.01 (for intsance),
    run `slim -d P=0.01 intro_p2_to_p3.slim`. Each time you run this will
    create a new `.trees` file, like `intro_{seed}_0.0.trees`.

2. Run `python3 compute_D.py *.trees` to print out statistics for all the tree sequences.

3. Open the `plot_trees.ipynb` jupyter notebook, change the .trees filename at the top
    and execute to see the trees at a few places along the genome.
