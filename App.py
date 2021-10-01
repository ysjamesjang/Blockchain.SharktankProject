import streamlit as st
import numpy as numpy
import pandas as pd

st.title("Shark Tank Smart Contract Marketplace")

st.write("Are you in need of a place to help find funding for your project or venture? The Shark Tank Marketplace is your place to find funding. From a single investor or a bunch of small investors, the Shark Tank Marketplace utilizes Smart Contracts to secure future deals in stone on the blockchain.")

level1 = st.slider("How much money are you looking to raise?", 1000,500000)

level2 = st.slider("How much equity percentage (%) are you providing to the investors?", 1,100)

st.sidebar.title("For investors")
level3 = st.sidebar.slider("How much money are you looking to invest?", 1000,500000)