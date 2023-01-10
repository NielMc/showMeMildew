import streamlit as st
from app_pages.multipage import MultiPage


from app_pages.summary import summary_body
from app_pages.cherry_leaf_visualizer import leaf_visualizer_body
from app_pages.show_me_mildew import show_me_mildew_body
from app_pages.hypothesis import hypothesis_body
from app_pages.performance import performance_metric_body


app = MultiPage(app_name="Show Me Mildew")


app.add_page("Quick Project Summary", summary_body)
app.add_page("Cherry Leaf Visualizer", leaf_visualizer_body)
app.add_page('Show Me Mildew', show_me_mildew_body)
app.add_page("Hypothesis and Visualization", hypothesis_body)
app.add_page('Performance Metric', performance_metric_body)

app.run() 










