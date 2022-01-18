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
- Get dataset
Card Table:
|Card Name|Initial printing|red|green|black|blue|white|text*|
|str      | str(set)       |1/0|1/0  |1/0  |1/0 |1/0  | str |

Set Table:
|set|date|

text* may be expanded to an occurence (bag of words) vector.

- Remove all card printings beyond the first from dataset
- Remove all hint text from cards, usually contained in ()




