# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 2026-11-10 baseline (Track A)
- changed: Trained the starter recipe with seeds 0 and 1.
- why:
- validation: 0.4894 (seed 0); 0.4912 (seed 1)
- what it means:

## 2026-11-10 b1 (Track B)
- changed: Trained `src/train_b.py` as provided with its default ResNet18 at 224 pixels for 4 epochs; saved the submission.
- why:
- validation: 0.5013
- what it means:
