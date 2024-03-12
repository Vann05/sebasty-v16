import os
from tensorflow.keras.layers import Dense, Dropout
from neuralintents.assistants import BasicAssistant

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

own_layers = [
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5)
]

assistant = BasicAssistant('answer.json', hidden_layers=own_layers)

assistant.fit_model(epochs=50)
assistant.save_model()
