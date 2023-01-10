import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from resources.manage_data import load_pickle_file

def plot_prediction_probabilities(prediction_prob, prediction_class):

    '''
    plot prediction probability result
    '''

    probability_per_classification = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    probability_per_classification.loc[prediction_class] = prediction_prob
    for x in probability_per_classification.index.to_list():
        if x not in prediction_class:
            probability_per_classification.loc[x] = 1 - prediction_prob
    probability_per_classification = probability_per_classification.round(3)
    probability_per_classification['Diagnostic'] = probability_per_classification.index

    fig = px.bar(
        probability_per_classification,
        x='Diagnostic',
        y=probability_per_classification['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def predict(image, version):

    """
    Load and perform machine learning prediction on images provided
    """

    model = load_model(f'outputs/{version}/show_me_mildew_model.h5')
    prediction_probability = model.predict(image)[0, 0]

    labels = {'healthy': 0, 'powdery_mildew': 1}

    target_map = {v: k for k, v in labels.items()}
    predicted_classification = target_map[prediction_probability > 0.5]

    if predicted_classification == target_map[0]:
        prediction_probability = 1 - prediction_probability

    conclusion = "analysis shows the leaf "

    if predicted_classification.lower() == 'healthy':
        st.write(conclusion = f"{conclusion} is **{predicted_classification.lower()}**")
    else:
        st.write(conclusion = f"{conclusion} has **powdery mildew**.")
        
    return prediction_probability, predicted_classification

def resize_image(img, version):
    """
    Resize image to images size stored in the image shape pickle file

    """
    image_shape = load_pickle_file(
        file_name=f"outputs/{version}/image_shape.pk1")
    resized_image = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    return np.expand_dims(resized_image, axis=0)/255


