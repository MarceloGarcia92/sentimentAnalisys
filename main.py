import mlflow

from src.models.sentiment import load_data, models, preprocessing, train
from src.models.sentiment.parametros import *

x, y, max_words, _ = load_data.load_from_spark("sat_sentiment_analysis")
x_train, x_test, y_train, y_test = train.split_data(x, y)
pad_sent_train, pad_sent_test = preprocessing.seq_creation(x, x_train, x_test, max_words)

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("sentiment_analysis")

mlflow.tensorflow.autolog(disable=True)

with mlflow.start_run(run_name='Embedding_model'):
    params = {
        'loss': 'binary_crossentropy',
        'optimizer':'adam',
        'epochs':50,
        'batch_size':5
    }

    mlflow.set_tag("Dense_model", "Dense")
    mlflow.log_params(params)

    model = models.model_creation(VOCAB_SIZE, EMBENDING_DIM, max_words)

    model.compile(loss=params['loss'], optimizer=params['optimizer'], metrics=['accuracy'])

    history = model.fit(pad_sent_train, y_train, 
                        validation_data=[pad_sent_test, y_test], 
                        epochs=params['epochs'], 
                        batch_size=params['batch_size'])
    
    mlflow.log_metric('Accuracy', history.history['accuracy'][-1])
    mlflow.tensorflow.log_model(model, 'tf_models')