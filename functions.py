import keras
import numpy as np
import streamlit as st
from keras import layers, models, optimizers  # modeling
from PIL import Image
from keras.models import Model
from keras.models import load_model
import tensorflow as tf

MODEL = "model.h5"


@st.cache(allow_output_mutation=True)
def load_model():
    print("loading model")
    model = keras.models.load_model(f"{MODEL}", compile=True)

    return model


def preprocess_image(img):
    image = Image.open(img).convert("RGB")
    p_img = image.resize((224, 224))

    return np.array(p_img) / 255.0


def predict(model, img):
    prob = model.predict(np.reshape(img, [1, 224, 224, 3]))

    if prob > 0.5:
        prediction = True
    else:
        prediction = False

    return prob, prediction
