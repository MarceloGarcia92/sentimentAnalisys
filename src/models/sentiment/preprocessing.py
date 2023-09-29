from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.models.sentiment.parametros import *

def seq_creation(text, x_sent_train, x_sent_test, max_words):
    tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token='<OOV>')
    tokenizer.fit_on_texts(text)

    seq_sent_train = tokenizer.texts_to_sequences(x_sent_train)
    pad_sent_train = pad_sequences(seq_sent_train, maxlen=max_words, padding=PADD_TYPE, truncating=TRUNC_TYPE)

    seq_sent_test = tokenizer.texts_to_sequences(x_sent_test)
    pad_sent_test = pad_sequences(seq_sent_test, maxlen=max_words, padding=PADD_TYPE, truncating=TRUNC_TYPE)

    return pad_sent_train, pad_sent_test