import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

from resources.machine_learning.prediction_analysis import (
    predict,
    resize_image,
    plot_prediction_probabilities
)
from resources.manage_data import download_dataframe_as_csv

def show_me_mildew_body():
    st.write('### Objective')
    st.info(
        f"The Client wants a way of predicting if a given leaf"
        f" contains powdery mildew"
    )
    st.write('---')

    st.write('Upload an image and click **Make Prediction** to run the model')
    btn_predict = st.button("Make Prediction")
    images = st.file_uploader(
        'Upload Cherry leaf samples (You may select more than one.)',
        type='JPG', accept_multiple_files=True)

    if btn_predict:
        upload_and_run_model(images)

def upload_and_run_model(images):
    if images is not None:
        report = pd.DataFrame([])
        for image in images:
            img = (Image.open(image))
            st.info(f"Cherry Leaf Sample Image: **{image.name}**")
            img_array = np.array(img)
            img_height = img_array.shape[0]
            img_width = img_array.shape[1]
            st.image(
                img,
                caption=f"Sample Image Size: {img_width}px x {img_height}px")

            version = 'v1.0'
            resized_img = resize_input_image(img=img, version=version)
            prediction_prob, prediction_class = make_prediction(
                resized_img, version=version)

            plot_prediction_probabilities(prediction_prob, prediction_class)

            report = report.append({"Image Name": image.name, 'Prediction': prediction_class},
                                ignore_index=True)

        if not report.empty:
            st.success("Analysis Report")
            st.table(report)
            st.markdown(download_dataframe_as_csv(report), unsafe_allow_html=True)            