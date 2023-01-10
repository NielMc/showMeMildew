import streamlit as st


def hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"**Hypothesis**\n\n"
        f"* cherry leaves infected with mildew have white patched on the leaf face.\n\n"
    )
    st.info(
        f"**Validation**\n\n"
        f"* An Image Montage, shows that typically a leaf containing powdery mildew have white streak on them.\n\n"
        f"* As seen in the image montage, leafs infected with mildew typically have white patches on their face \n\n"
        f"* the average image illustrates this as the average image for a healthy leaf appears greener with a more"
        f" even texture when compared to a leaf with mildew\n\n"
        f" To see the Image Montage and the average images discussed above, click "
        f" on the **Cherry Leaf Visualizer** subheading in the sidebar"


    )