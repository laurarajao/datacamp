import streamlit as st
import numpy as np
from PIL import Image
import numpy as np
import streamlit as st
import functions
from keras.models import Model
from keras.models import load_model
import tensorflow as tf

MODEL = "model.h5"

st.title("Welcome to our application")
st.write("This is our application to detect pneumonia from Chest X-Ray images."
                                          "The model used is a Convolutional Neural Network (CNN) and in this "
                                         "moment has a test accuracy of "
                                         "87.1%.")

image = Image.open('poumon.jpg')
st.image(image)

st.markdown("Let's load an X-Ray Chest image.")

st.sidebar.markdown("Made by Elodie Bouisset, Camélia Mahraz and Laura Rajaosafara ")

st.sidebar.markdown(  """
    Add Camelia on Linkedin ! [![Follow](https://th.bing.com/th/id/R.261195b1b8c2a3df5376543a2125f4f3?rik=IvHrDZsC5EZ%2f%2fg&pid=ImgRaw&r=0)](https://www.linkedin.com/in/camelia-mahraz-13a1391a0)
    """)

st.sidebar.markdown(  """
    Add Laura on Linkedin ! [![Follow](https://th.bing.com/th/id/R.261195b1b8c2a3df5376543a2125f4f3?rik=IvHrDZsC5EZ%2f%2fg&pid=ImgRaw&r=0)](https://www.linkedin.com/in/laura-rajaosafara)
    """)

st.sidebar.markdown(  """
    Add Elodie on Linkedin ! [![Follow](https://th.bing.com/th/id/R.261195b1b8c2a3df5376543a2125f4f3?rik=IvHrDZsC5EZ%2f%2fg&pid=ImgRaw&r=0)](https://www.linkedin.com/in/elodie-bouisset-b151421a0/)
    """)



#Let's load the neural network model

# Take the image
img = st.file_uploader(label="Load X-Ray Chest image", type=['jpeg', 'jpg', 'png'], key="xray")

if img is not None:
    p_img = functions.preprocess_image(img)

    if st.checkbox('Zoom image'):
        image = np.array(Image.open(img))
        st.image(image, use_column_width=True)
    else:
        st.image(p_img)

    #Load the model
    loading_msg = st.empty()
    loading_msg.text("Predicting...")
    model = functions.load_model()

    #Prediction
    prob, prediction = functions.predict(model, p_img)

    loading_msg.text('')

    if prediction:
        st.markdown(unsafe_allow_html=True, body="<span style='color:red; font-size: 50px'><strong><h4>Pneumonia detected!</h4></strong></span>")
    else:
        st.markdown(unsafe_allow_html=True, body="<span style='color:green; font-size: 50px'><strong><h3>No pneumonia detected!</h3></strong></span>")
    
