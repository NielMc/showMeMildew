import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
from resources.machine_learning.evaluate import evaluate_test

def performance_metric_body():
    version = 'v1.0'
    output_path = f"outputs/{version}/"

    st.write("### Train, Validation and Test set: Label distribution")

    labels_distribution = plt.imread(f"{output_path}labels_distribution.png")
    st.image(labels_distribution,
             caption="Label Distribution on Train, Validation and Test sets")
    st.info(f"* The original dataset is split equally into the two labels of **healthy** and **powdery mildew**\n\n"
            f"* The dataset was split into 3 sets, train(70%), validation(10%) and test(20%)")
    st.write('---')

    if st.checkbox("Model History"):
        st.write('### Model History')
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f'{output_path}model_training_accuracy.png')
            st.image(model_acc, caption="Model Training Accuracy")
        with col2:
            model_loss = plt.imread(f'{output_path}model_training_losses.png')
            st.image(model_loss, caption='Model Training Losses')
        st.write('---')

    st.write('### Generalised Performance on Test Set')
    evaluate_test(version)