import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import itertools
import random


def leaf_visualizer_body():
    version = 'v1.0'
    output_path = f"outputs/{version}"

    st.write('### Cherry Leaf Visualizer')
    st.info(
        f"The objective here is to visually differentiate between a **healthy**"
        f" cherry leaf and one which is infected with **powdery mildew**."
    )

    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"{output_path}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"{output_path}/avg_var_powdery_mildew.png")

        st.info(
            f"this plot shows the average image of a healthy leaf and one infected with mildew\n\n"
            f"* The healthy leaves appears to typically be more green in colour than one infected with mildew.\n\n"
            f"* a leaf infected with mildew appears to have a more uneven texture than a healthy leave,"
        )

        st.image(avg_healthy, caption="Healthy cherry leaf - Average and Variability")
        st.image(
            avg_mildew, caption="Powdery mildew cherry leaf - Average and Variability")
        st.write('---')

    if st.checkbox('Differences between Healthy and Powdery Mildew cherry leaves'):
        avg_diff = plt.imread(f"{output_path}/avg_diff.png")

        st.info(
            f"* The left and middle images plot the average as shown by the previous checkbox "
            f" the right image, the difference between variability, illustrates that the images"
            f" are more similar in the darker parts while being more different in the lighter parts"
        )

        st.image(avg_diff, caption='Difference between average images')
        st.write('---')

    if st.checkbox("Image Montage"):
        st.write(
            "To see a montage of sample images, select a classification and click the **Create Montage** button")
        st.write('a new montage of images will be generated when the **Create Montage** button is clicked')
        data_path = 'inputs/cherry_leaves_data/cherry-leaves/test'
        labels = os.listdir(data_path)
        label_to_display = st.selectbox(
            label="Choose label",
            options=labels,
            index=0
        )
        if st.button("Generate Montage"):
            st.info(
                f"**Observation**\n\n"
                f"* The mean dimensions of each image is 256px by 256px \n\n"
                f"* The mildew infected leaves have noticeable white patches "
                f" which differentiates them from healthy leaves"
            )
            image_montage(data_path, label_to_display,
                          nrows=3, ncols=3, figsize=(10, 12))
            st.write('---')


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:

        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.error(
                f"ERROR: You requested a montage with {nrows * ncols} spaces but"
                f"There are {len(images_list)} in your subset. "
                f"lower either nrows or ncols to create your montage. \n"

)
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        st.error(
            f"That label does not exist"
            f"please choose either: {labels}"
        )
