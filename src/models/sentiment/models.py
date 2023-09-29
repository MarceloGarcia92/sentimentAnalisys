from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, Flatten


def model_creation(vocab_size, embedding_dim, max_words):
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim, input_length=max_words))
    model.add(Flatten())
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.summary()

    return model