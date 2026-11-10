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
- why: This is our starting point; we will compare further runs with these numbers. We ran it twice with different seeds to find out how much the result can change by chance alone.
- validation: 0.4894 (seed 0); 0.4912 (seed 1)
- what it means: The two results differ by only 0.002, which is within the margin of error. The worst cities are Busan and Osaka. Maybe because their photos are filled with a lot of junk, and they had a smaller base of photos in the first place, while Tokyo had the largest number of photos.

## 2026-11-10 b1 (Track B)
- changed: Trained `src/train_b.py` as provided with its default ResNet18 at 224 pixels for 4 epochs; saved the submission.
- why: Also a starting point, for Track B, so we can compare further runs with it.
- validation: 0.5013
- what it means: Even though the model was the same as in Track A (ResNet18), the approach was a little different: 4 full passes over the photos, about 177,000 photos shown instead of 250,000. But the numbers are relatively similar (0.501 vs 0.489-0.491). So we can assume that we need to change the approach in a different way to get better results.

## 2026-11-10 mistakes of baseline seed 0 (Track A)
What the most confident mistakes have in common:
1. Unrelated single objects with nothing that tells the city apart: food, animals, and a lot of cars (just a random car). These are junk and should not be in the training photos.
2. Very generic scenery without any specific elements: just a random tree, a random building, or a random street with a random car. Nothing in the photo belongs to one city only.

## 2026-11-10 my rule for cleaning the training photos (Track A, step 7)
- rule (written before dropping anything): Drop all training photos that cannot be considered a street view or scenery of any kind: food, animals, car close-ups, indoor photos, and photos of people (portraits). Keep ordinary street photos even when they look generic, because the final test photos are street photos too.

## 2026-11-10 curated (Track A)
- changed: dropped 98 non-street training photos following my rule above; starter recipe unchanged
- why: Keeping irrelevant photos where it is impossible to tell the city from the start does not help training at all. They got into the data by accident and have nothing to do with what the classifier is for.
- validation: 0.5005 (before: baseline 0.4894)
- what it means: The junk did affect the model's results, and cleaning up the photos gave the first noticeable improvement.

## 2026-11-10 noflip (Track A)
- changed: removed the random left-right flip from the starter recipe; all training photos
- why: I assumed that the writing (Hangul, Japanese and Chinese characters) is important at least for telling the country apart, and a mirrored photo turns it into mirror writing.
- validation: 0.4861 (before: baseline 0.4894)
- what it means: The result got slightly worse, so my hypothesis was wrong. I made the assumption as a human: when I play GeoGuessr, I first look for small details like Japanese characters and know it is Japan. The model does not look at photos the way a human does.

## 2026-11-10 balanced (Track A)
- changed: every city drawn equally often (weight 1 / number of photos of that city); all training photos
- why: In the baseline, most mistakes were other cities taken for Tokyo. I noticed that Tokyo had both the most photos and the most mistakes, so the model picked the "safest" answer, Tokyo, because it saw so many Tokyo photos.
- validation: 0.5074 (before: baseline 0.4894); Busan 0.37 -> 0.47, Osaka 0.33 -> 0.45, Tokyo 0.64 -> 0.51
- what it means: The score went up and Tokyo's share dropped, so my assumption was right. For fair results, the model should see every city equally often.

## 2026-11-10 balanced_curated (Track A)
- changed: balanced recipe together with my curated selection
- why: Both curated and balanced showed positive results on their own, so I assumed that combining them would give an even better result.
- validation: 0.5049 (before: balanced 0.5074, curated 0.5005)
- what it means: The result is basically the same and sits between balanced and curated. I think balancing was the most important part, and combining the two did not add much.

## 2026-11-10 b2 (Track B)
- changed: MobileNetV3-Large instead of ResNet18, 320 px instead of 224, cities balanced, 6 epochs
- why: To see how the model behaves when the training conditions change, without changing the photos themselves, and with the cities balanced.
- validation: 0.5566 (before: b1 0.5013)
- what it means: Changing the conditions does have an impact, but I still think balancing the cities made the biggest difference.

## What I would try next
- Run balanced and balanced_curated with more seeds, to check whether cleaning the photos really adds nothing once the cities are balanced. I still think the idea has potential.
- Try my curated selection in Track B too (b2 without the 98 dropped photos).
- Add my own phone photos of the five cities, so the model sees photos like the final test photos.
