import streamlit as st
import pandas as pd
from resources.manage_data import load_pickle_file

def evaluate_test(version):
    st.dataframe(pd.DataFrame(
        load_pickle_file(f'outputs/{version}/evaluation.pk1'), index=['Loss', 'Accuracy']))