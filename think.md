# SVM (support vector machine):

Each dimension (D) represents occurence of word (N) in corpus.
Use above to produce NxN matrix of distances between each point.
Matrix contains information for "classifier"...

d^2 = (x-z) . (x-z)
    = (x.x - 2(x.z) + z.z 

# "Markov classifier"
Build language model for each class.
Use MLE (with smoothing) to classify...

arg max\_i (F\_i(x))

where F\_i is the MM for class i, x is the corpus being classified.

We can compare the EER of these two models and decide which is better, this isn't really the objective, but
might be interesting.

- In theory, we want an "expert" model and the measurement we are concerned with is the EER.
- For SVM the distances between each class (cluster) may be useful.


#TODO
- FIX TEXTLESS CARDS
- currently produce weird "nan" results in dataset, replace with either an {empty} indicator or appropriate
empty string.
- Fix capitalisation in input strings (dataset), means rebuilding dataset
- allow apostrophe in word tokens


#Next Steps
- build the Markov model
- building generative model: fairly simple.
- fit a HMM based on corpus, hard.
- must account for:
    + sink words, words which do not occur in the training set, we should reserve a small volume of
      "probability mass" for transitioning to a sink word from ANYWHERE. The probability of moving from
      a sinkword to any other word is? (uniform?, based on term frequency?)
- must tokenize accounting for some special cases:
    + symbols {R} {G} {B} {U} {W} {T}

- many new cards are guaranteed to have novel words; their own names. This obudence of words which appear
    exactly once (hapaxes) may be a problem, could *replace* instances of a cards own name with a meta-token?

- So the questions I have now are:
    + How to actually go about fitting the model using a "perfect" dataset?
    + Transitioning from sink words to known words isn't too bad, but how to determine good value for
        transitioning to an unseen word?
    + How to handle high "Hapax" volume, is name:meta-token replacement valid?


# Tokenizer:

- The tokenizer is actually made a bit easy (I hope) by the regularity of the corpus. The world-class framing
    of card text means there a very few unexpected characters, and the history of mtg digitization means there
    are already clear de facto standards for encoding symbols as strings ({T} is the tap symbol, {B} blue mana
    etc.)

- I also added {START}, {END} and {THIS} meta tokens. {THIS} refers to the card name to which a text body
    belongs. Having these been in the same format as the symbols may have been a mistake but it will be easy
    to change if it does become an issue.


- SYMBOL KEY (case insensitive):
    {q} : untap
    {t} : tap
    {r,g,b,w,u,r/b,r/g etc.} : mana colours
    {x} : x costs
    {0-9} : colours costs
    {s} : snow costs
    {r/p,p} : phyrexian costs
    {e} : energy






