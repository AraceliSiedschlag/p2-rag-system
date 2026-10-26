# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I picked the supreme court opinions because I feel like more recently the supreme court continues to hear and make more landmark rulings so being able to use a RAG to understand those seems efficient. I think it is important to understand what is happening in the judicial world because it continues to have effects in our everyday lives swiftly and effectively. Additionally, supreme court documents are long and complicated so being able to just ask questions seems helpful. I think that rerank will win out because it utilizes all model, I don't think just using one is enough. I think bm25 will do the worst because its complicated wording so it wouldn't search as well. I have already ran uv run p2 score but I don't remember the numbers so I am writing this now before doing EVAL.md file stuff.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

One fork in the road for this project was choosing the model to use for dense. I chose to use bge-small but I looked at two bge-small and potion. By not choosing potion I gave up a slightly higher score on identifier questions but potion ran faster. I measured both on my supreme court corpus and the shared corpus getting 0.622 against 0.562 and 0.562 and 0.475 respectively. So, I gave up speed and a higher score on identifier questions (0.571 vs 0.333 shared) for better scores on paraphrase questions and overall.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

Throughout this process I feel like Claude gives more questions and suggestions and lots of options making it difficult to overrule an agent, however, one time during this project that I overruled an agent was choosing the number of characters, not suggested, to read for the rerank_chars. Claude suggested a table of characters (600,3000,6000,10000) to choose from but I chose to do 2500 characters for my reranker because that felt more reasonable than 3000. 

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number that I do not trust is the +0.105 MRR for rerank_chars. The reason that I do not fully trust this is that the interval contains zero. This could be because 30 questions cannot detect the difference because the minimum detectable difference for this pair is 0.180 and the +0.105 is well under it. Additionally, the score is from one run, to trust it more the score should be averaged and ran fresh. It was also scored on my own gold set which was found to be too narrow which could've hurt the score making it less accurate.  To trust this more would require testing with more questions, repeat runs, or fixing the gold set. Looking at nDCG@10 from the same run it rose by 0.089 with an interval completely above zero showing that there is gain and is distinguishable. Additionally, it helped 13 questions, hurt 5, and left 12 unchanged, but none of this was tested with repeat runs or additional questions.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

One thing that is wrong with my system is that the gold set is too narrow. This was discovered in my failure analysis  where answers that failed normally still found relevant parts but that were not in my gold set. To show that the gold set is too narrow someone could look at o25 what was returned and what the gold set included, this would show that more documents than were chosen for the gold set were relevant. So to fix this I would expand my gold set to incorporate more documents related to the questions. 
