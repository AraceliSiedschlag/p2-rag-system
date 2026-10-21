# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.


All documents for bm25 and dense were chunked the same using pieces of 300 words, where each piece shares 50 words with the one before it.
Dense: The final dense used BAAI/bge-small-en-v1.5 model after testing 2 other models (potion-retrieval-32M and snowflake-arctic-embed-s) one where it was faster but scored lower and one that was about as slow and scored lower overall.
Hybrid: Hybrid was fused using the RRF function with k = 60 with two document rankings the one from bm25 and the one from dense. Four versions of hybrid were tested ending with bm25 getting a voting weight of one and the dense getting a voting weight of two and a depth of 100 for ranking. 
Rerank: This uses the hybrid top 20 documents with claude reading the first 600 characters of each one.  

Compared with the lab 12 and 13 code, dense saw pieces of each document rather than the document as a whole. Additionally, the caching of vectors changed because vectors were cached per piece of text instead of one cache file for the whole corpus as in the lab. Then for hybrid weights and depth were added which differed from the lab and it blended piece rankings which the lab did not need. Finally, rerank used a different starting system because it started with the weighted hybrid and it has a stricter schema where each number must be between 1 and 20.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.535 | 0.485 |
| rerank | 0.613 | 0.700 | 0.628 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.357 | 0.548 | 0.917 |
| hybrid | MRR@10 | 0.500 | 0.421 | 0.708 |
| hybrid | nDCG@10 | 0.356 | 0.425 | 0.704 |
| rerank | Recall@10 | 0.321 | 0.643 | 0.917 |
| rerank | MRR@10 | 0.429 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.338 | 0.654 | 0.936 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.292, +0.225] | 0.377 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.028 | [-0.172, +0.233] | 0.291 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.034 | [-0.242, +0.180] | 0.306 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.033, +0.117] | 0.110 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.028 | [-0.182, +0.113] | 0.215 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.005 | [-0.096, +0.097] | 0.141 | not distinguishable |
| rerank minus bm25 | Recall@10 | -0.013 | [-0.300, +0.275] | 0.420 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.193 | [-0.083, +0.462] | 0.398 | not distinguishable |
| rerank minus bm25 | nDCG@10 | +0.110 | [-0.168, +0.375] | 0.393 | not distinguishable |
| rerank minus dense | Recall@10 | +0.054 | [-0.033, +0.146] | 0.134 | not distinguishable |
| rerank minus dense | MRR@10 | +0.138 | [-0.046, +0.325] | 0.270 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.148 | [+0.022, +0.281] | 0.188 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.021 | [-0.062, +0.104] | 0.127 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.165 | [-0.013, +0.340] | 0.258 | not distinguishable |
| rerank minus hybrid | nDCG@10 | +0.143 | [+0.017, +0.266] | 0.181 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?


The differences that are distinguishable from zero are rerank which is higher than dense and higher than hybrid on nDCG, both of which have confidence intervals all above 0. Everything else includes zero so it is not distinguishable (MRR, Recall). At 20 questions the minimum detectable difference ranges from 0.11 to 0.42 depending on the pair and measure. For anything compared to bm25, it is larger about 0.29 to 0.42 because the others disagree from question to question. Most gaps are smaller than their MDD, such as hybrid minus bm25 on MRR, +0.028 against an MDD of 0.291, so 20 questions can't detect them. 
Lecture 12 claimed that no single retriever wins both types of questions and this project supports it because bm25 has a MRR 0.81 on same word questions and 0.33 for dense, bm25 gave 0 on different words question and a 0.714 for dense. In lecture 13 it was claimed that reranking improves on the first stage this was supported on nDCG, the two rerank higher rows they are left open on MRR and recall. However, lab 13 hybrid beat both of its parts on the articles, but hybrid, in this project, landed between bm25 and dense in numbers and they were not distinguishable, so whether fusion beats both of its parts on this corpus is left open.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 10 of 10 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I have chosen rerank because it had the highest practice MRR (0.700) and nDCG distinguishably higher than hybrid and dense and it reorders hybrid's top 20 so that the best pieces come first, and then the top 5 pieces go to the answer step. I did not change anything in `prompts/answer.txt` so it verified 8 of 8, declined 4 of 4.

a01: Supported yes - the quote gives the number (15 min) that the claim states and that death is an accident type required to call MSHA.

a05: Supported yes - the quote correctly claims that new miners should receive no less than 40 hours of training.  

a07: Supported yes - the quote correctly says the berms or guardrails shall be at least mid-axle height. The claim that the height requirement applied under parallel underground metal and nonmetal mine standard is supported by section 57.9300.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My corpus is the 2022 US Supreme Court opinions (55/58 cases to make token limit). It came from the official US Reports, volumes 598 to 600 all in PDF form. There are 401 documents split into 5-page parts coming in at 4.1 MB and about 628,353 words. The license is us-gov-public-domain because the opinions are written by federal judges in their official duties and their work cannot be copyrighted. Overall, it is allowed because it is the US federal government's work

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

10 queries were written by hand 20 were written by claude to make 30 queries total. I used 11 paraphrase, 10 identifier, 9 mixed classes in order to test and get an accurate understanding of how the model is doing. Additionally they are the same classes in stage 1, so the two corpuses can be compared class by class.

My relevance rule:
The answer must be stated, talking about the case isn't enough but it can answer in one sentence if needed and if quotes the dissent it must mention it is coming from the dissent. When being ranked on relevance there is a 2,1,0 scale 2 when the question is fully answered, 1 when it states a part of the answer to a question, and it is 'unlisted' if it is not relevant at all.

For the ten questions written by hand and the questions by claude the candidates were found by using bm25, hybrid, dense, and keyword search. Additionally, for hand written ones I knew where to find the answers because that is how the questions were created. Candidates came from the top 10 of any of the three systems, plus keyword matches. I was shown snippets of each part. From those I read all of the given snippets of text and decided if it answered the question fully (2), helped (1), if multiple of them answered it, or if it didn't help at all (so I left it out). I did not read all of every text unless the snippet didn't answer the question or was vague but for the most part I was able to get the answer from the snippets of text. Additionally, ingest removed the "J., dissenting" page headers, so I identified dissent parts from where each opinion begins.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.869 | 0.634 | 0.644 |
| dense | 0.814 | 0.622 | 0.606 |
| hybrid | 0.856 | 0.634 | 0.622 |
| rerank | 0.831 | 0.558 | 0.570 |
| ablation/rerank_chars | 0.900 | 0.663 | 0.659 |

30 judged queries; nDCG uses graded labels; a random ranking of the 401 documents would get recall@10 near 0.025.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | mixed (n=8) | identifier (n=10) | paraphrase (n=12) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.969 | 0.833 | 0.833 |
| bm25 | MRR@10 | 0.708 | 0.775 | 0.468 |
| bm25 | nDCG@10 | 0.721 | 0.722 | 0.529 |
| dense | Recall@10 | 0.906 | 0.667 | 0.875 |
| dense | MRR@10 | 0.812 | 0.517 | 0.583 |
| dense | nDCG@10 | 0.749 | 0.527 | 0.576 |
| hybrid | Recall@10 | 0.906 | 0.792 | 0.875 |
| hybrid | MRR@10 | 0.792 | 0.550 | 0.600 |
| hybrid | nDCG@10 | 0.737 | 0.579 | 0.581 |
| rerank | Recall@10 | 0.938 | 0.742 | 0.833 |
| rerank | MRR@10 | 0.750 | 0.439 | 0.528 |
| rerank | nDCG@10 | 0.679 | 0.512 | 0.547 |
| ablation/rerank_chars | Recall@10 | 0.906 | 0.775 | 1.000 |
| ablation/rerank_chars | MRR@10 | 0.737 | 0.600 | 0.665 |
| ablation/rerank_chars | nDCG@10 | 0.691 | 0.596 | 0.690 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.800 | 0.904 | -0.104 | [-0.350, +0.113] | not distinguishable |
| bm25 | MRR@10 | 0.750 | 0.577 | +0.173 | [-0.122, +0.438] | not distinguishable |
| bm25 | nDCG@10 | 0.706 | 0.613 | +0.093 | [-0.161, +0.325] | not distinguishable |
| dense | Recall@10 | 0.600 | 0.921 | -0.321 | [-0.604, -0.050] | claude higher |
| dense | MRR@10 | 0.650 | 0.608 | +0.042 | [-0.279, +0.333] | not distinguishable |
| dense | nDCG@10 | 0.540 | 0.638 | -0.099 | [-0.370, +0.160] | not distinguishable |
| hybrid | Recall@10 | 0.675 | 0.946 | -0.271 | [-0.546, -0.025] | claude higher |
| hybrid | MRR@10 | 0.617 | 0.643 | -0.027 | [-0.325, +0.259] | not distinguishable |
| hybrid | nDCG@10 | 0.563 | 0.651 | -0.089 | [-0.359, +0.176] | not distinguishable |
| rerank | Recall@10 | 0.675 | 0.908 | -0.233 | [-0.517, +0.042] | not distinguishable |
| rerank | MRR@10 | 0.531 | 0.571 | -0.040 | [-0.332, +0.243] | not distinguishable |
| rerank | nDCG@10 | 0.494 | 0.608 | -0.115 | [-0.351, +0.129] | not distinguishable |
| ablation/rerank_chars | Recall@10 | 0.725 | 0.988 | -0.263 | [-0.500, -0.050] | claude higher |
| ablation/rerank_chars | MRR@10 | 0.551 | 0.718 | -0.167 | [-0.440, +0.110] | not distinguishable |
| ablation/rerank_chars | nDCG@10 | 0.537 | 0.720 | -0.183 | [-0.427, +0.068] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | -0.017 | +0.200 | -0.217 | [-0.483, +0.008] | not distinguishable |
| MRR@10 | -0.032 | +0.100 | -0.132 | [-0.498, +0.223] | not distinguishable |
| nDCG@10 | -0.025 | +0.167 | -0.192 | [-0.452, +0.039] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.86 (10 queries), claude 0.82 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.056 | [-0.172, +0.067] | 0.177 | not distinguishable |
| dense minus bm25 | MRR@10 | -0.012 | [-0.172, +0.141] | 0.228 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.148, +0.058] | 0.150 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.014 | [-0.119, +0.083] | 0.146 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.000 | [-0.133, +0.128] | 0.190 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.022 | [-0.122, +0.060] | 0.132 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.042 | [-0.017, +0.108] | 0.095 | not distinguishable |
| hybrid minus dense | MRR@10 | +0.012 | [-0.047, +0.078] | 0.091 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.016 | [-0.017, +0.050] | 0.049 | not distinguishable |
| rerank minus bm25 | Recall@10 | -0.039 | [-0.161, +0.081] | 0.181 | not distinguishable |
| rerank minus bm25 | MRR@10 | -0.077 | [-0.212, +0.055] | 0.195 | not distinguishable |
| rerank minus bm25 | nDCG@10 | -0.074 | [-0.176, +0.020] | 0.145 | not distinguishable |
| rerank minus dense | Recall@10 | +0.017 | [-0.042, +0.075] | 0.088 | not distinguishable |
| rerank minus dense | MRR@10 | -0.065 | [-0.203, +0.067] | 0.195 | not distinguishable |
| rerank minus dense | nDCG@10 | -0.035 | [-0.109, +0.031] | 0.101 | not distinguishable |
| rerank minus hybrid | Recall@10 | -0.025 | [-0.117, +0.058] | 0.127 | not distinguishable |
| rerank minus hybrid | MRR@10 | -0.077 | [-0.207, +0.046] | 0.184 | not distinguishable |
| rerank minus hybrid | nDCG@10 | -0.052 | [-0.132, +0.018] | 0.110 | not distinguishable |
| ablation/rerank_chars minus bm25 | Recall@10 | +0.031 | [-0.094, +0.158] | 0.183 | not distinguishable |
| ablation/rerank_chars minus bm25 | MRR@10 | +0.028 | [-0.112, +0.164] | 0.200 | not distinguishable |
| ablation/rerank_chars minus bm25 | nDCG@10 | +0.015 | [-0.101, +0.123] | 0.160 | not distinguishable |
| ablation/rerank_chars minus dense | Recall@10 | +0.086 | [+0.017, +0.172] | 0.114 | ablation/rerank_chars higher |
| ablation/rerank_chars minus dense | MRR@10 | +0.040 | [-0.093, +0.171] | 0.194 | not distinguishable |
| ablation/rerank_chars minus dense | nDCG@10 | +0.053 | [-0.022, +0.129] | 0.110 | not distinguishable |
| ablation/rerank_chars minus hybrid | Recall@10 | +0.044 | [-0.033, +0.133] | 0.118 | not distinguishable |
| ablation/rerank_chars minus hybrid | MRR@10 | +0.028 | [-0.090, +0.148] | 0.173 | not distinguishable |
| ablation/rerank_chars minus hybrid | nDCG@10 | +0.037 | [-0.028, +0.103] | 0.095 | not distinguishable |
| ablation/rerank_chars minus rerank | Recall@10 | +0.069 | [-0.017, +0.178] | 0.143 | not distinguishable |
| ablation/rerank_chars minus rerank | MRR@10 | +0.105 | [-0.017, +0.228] | 0.180 | not distinguishable |
| ablation/rerank_chars minus rerank | nDCG@10 | +0.089 | [+0.015, +0.176] | 0.119 | ablation/rerank_chars higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/rerank_chars minus bm25 | Recall@10 | +0.031 | [-0.094, +0.158] | 0.183 | not distinguishable |
| ablation/rerank_chars minus bm25 | MRR@10 | +0.028 | [-0.112, +0.164] | 0.200 | not distinguishable |
| ablation/rerank_chars minus bm25 | nDCG@10 | +0.015 | [-0.101, +0.123] | 0.160 | not distinguishable |
| ablation/rerank_chars minus dense | Recall@10 | +0.086 | [+0.017, +0.172] | 0.114 | ablation/rerank_chars higher |
| ablation/rerank_chars minus dense | MRR@10 | +0.040 | [-0.093, +0.171] | 0.194 | not distinguishable |
| ablation/rerank_chars minus dense | nDCG@10 | +0.053 | [-0.022, +0.129] | 0.110 | not distinguishable |
| ablation/rerank_chars minus hybrid | Recall@10 | +0.044 | [-0.033, +0.133] | 0.118 | not distinguishable |
| ablation/rerank_chars minus hybrid | MRR@10 | +0.028 | [-0.090, +0.148] | 0.173 | not distinguishable |
| ablation/rerank_chars minus hybrid | nDCG@10 | +0.037 | [-0.028, +0.103] | 0.095 | not distinguishable |
| ablation/rerank_chars minus rerank | Recall@10 | +0.069 | [-0.017, +0.178] | 0.143 | not distinguishable |
| ablation/rerank_chars minus rerank | MRR@10 | +0.105 | [-0.017, +0.228] | 0.180 | not distinguishable |
| ablation/rerank_chars minus rerank | nDCG@10 | +0.089 | [+0.015, +0.176] | 0.119 | ablation/rerank_chars higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/rerank_chars against rerank (BASE = "rerank" in p2/retrievers/rerank_chars.py): it helped 13 queries, hurt 5 and left 12 unchanged.

| Query | Class | Origin | rerank RR | ablation/rerank_chars RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| o30 | paraphrase | claude | 0.000 | 1.000 | +1.000 | helped |
| o01 | mixed | hand | 0.500 | 1.000 | +0.500 | helped |
| o11 | identifier | claude | 0.500 | 1.000 | +0.500 | helped |
| o12 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| o17 | identifier | claude | 0.500 | 1.000 | +0.500 | helped |
| o19 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| o27 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| o28 | identifier | claude | 0.500 | 1.000 | +0.500 | helped |
| o07 | paraphrase | hand | 0.000 | 0.200 | +0.200 | helped |
| o29 | mixed | claude | 0.333 | 0.500 | +0.167 | helped |
| o14 | paraphrase | claude | 0.250 | 0.333 | +0.083 | helped |
| o22 | identifier | claude | 0.250 | 0.333 | +0.083 | helped |
| o08 | identifier | hand | 0.143 | 0.167 | +0.024 | helped |
| o24 | mixed | claude | 1.000 | 0.250 | -0.750 | hurt |
| o03 | paraphrase | hand | 1.000 | 0.500 | -0.500 | hurt |
| o16 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| o25 | paraphrase | claude | 0.333 | 0.200 | -0.133 | hurt |
| o05 | mixed | hand | 0.167 | 0.143 | -0.024 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

I expect raising the reranker's passage length from 600 to 2500 characters to raise MRR@10  by 5 point on my corpus because it will be able see more of the text and then be able to judge it better.

The thing that changed was rerank characters read previously it was 600 and now it is 2500 characters. After making that change the scores went up like I predicted, however, MRR@10 did not increase by 5 points but rather 10.5 points, but the change could not confirm the gain because the interval still contains 0. Additionally, nDCG@10 did change and the change was distinguishable with the whole interval above 0. With this change it now has the highest MRR but with no distinguishable difference. The size of effect my gold set could have seen would be 0.180 and mine was 0.105 which was below that and therefore cannot be called distinguishable. Looking at the questions the change helped o30 and o01 the most and hurt o24 and o03 the most. The reason that it helped those the most was that it could see further into the page and find out more details. It hurt the questions because it was general and saw more info so it ranked other things as relevant or I didn't mark as many articles as possible relevant that were.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 287,497 | 12,379 | 189.2 | 23,958 | 1,032 | 15.8 |
| traces/own-own-ablation-rerank_chars.jsonl | rerank_chars | 30 | 30 | 2 | 924,976 | 29,206 | 377.1 | 30,833 | 974 | 12.6 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 2 | 506,461 | 28,281 | 428.7 | 16,882 | 943 | 14.3 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 337,063 | 14,535 | 199.0 | 16,853 | 727 | 9.9 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 653,814 | 26,893 | 368.2 | 16,345 | 672 | 9.2 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.193 | [-0.462, +0.083] | 16,853 | 9.9 | not distinguishable |
| shared practice: dense minus rerank | 20 | -0.138 | [-0.325, +0.046] | 16,853 | 9.9 | not distinguishable |
| shared practice: hybrid minus rerank | 20 | -0.165 | [-0.340, +0.013] | 16,853 | 9.9 | not distinguishable |
| own: bm25 minus rerank | 30 | +0.077 | [-0.055, +0.212] | 16,882 | 14.3 | not distinguishable |
| own: dense minus rerank | 30 | +0.065 | [-0.067, +0.203] | 16,882 | 14.3 | not distinguishable |
| own: hybrid minus rerank | 30 | +0.077 | [-0.046, +0.207] | 16,882 | 14.3 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.07 | 2.4 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.75 | 25.0 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.44 | 14.7 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.07 | 3.4 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.39 | 19.3 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.32 | 15.8 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.15 | 3.6 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.51 | 12.9 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.63 | 15.8 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
