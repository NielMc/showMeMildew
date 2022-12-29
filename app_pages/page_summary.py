
import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information on Powdery mildew**\n"

        f"* Powdery mildew is a fungal disease that affects a wide vareity of plants.\n "

        f"* it grows well in very humid enviroments with moderate temperatures. greenhouses "
        f"provide the perfect conditions for the disease to spread.\n"

        f"* it is easy to spot the affliction by the white powdery spores on the leaves"
        f"and stem, typically on the leaves at the base of the plant but, as the disease"
        f"spreads, can be seen further up the plant and with larger and denser clusters of spores \n"
        
        f"**Project goals**\n"
        f"the goal of this webapp is to identify, through a machine learning algorithm, leaves that"
        f"have been affected with powdery mildew.\n"
        f"currently this process is done manually which will take on average, 30 minutes per tree."
        f"this app will be able to identify instantly whether a tree is a suspected carrier of the"
        f"disease, leaving further inspection and resulting treatment to the trees owner.\n\n"

        f"**Project Dataset**\n"

        f"* The available dataset contains 5643 out of +27 thousand images taken from "
        f"blood smear workflow (when a drop of blood is taken on a glass slide) of "
        f"malaria-parasitised and uninfected cells.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/DavidJPWard/showMeMildew/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry "
        f"leaf that is healthy from one that contains powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.  "
        )
