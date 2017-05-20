from gensim.models import word2vec
data = word2vec.Text8Corpus('corpus80.txt')
model = word2vec.Word2Vec(data, size=200)

out = model.most_similar(positive=['delicious', 'meal'])
for x in out:
    print(x[0], x[1])
