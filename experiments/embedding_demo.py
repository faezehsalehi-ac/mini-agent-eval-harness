from sentence_transformers import SentenceTransformer , util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat.",
    "A Kitchen was resting on the rug.",
    "The stock market crashed today.",
]

embeddings = model.encode(sentences)

for i in range (len(sentences)):
    for j in range(i+1, len(sentences)):
        similarity = util.cos_sim(embeddings[i], embeddings[j])
        print(f"'{sentences[i]}' vs '{sentences[j]}' -> similarity: {similarity.item():.2f}")