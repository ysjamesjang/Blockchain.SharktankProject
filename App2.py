import streamlit as st
import numpy as numpy
import pandas as pd

st.sidebar.title("GET FUNDING")

st.title("Shark Tank Smart Contract Marketplace")

st.write("Are you in need of funding for your next project or venture? The Shark Tank Marketplace is your place to find funding. From a single investor or a bunch of small investors, the Shark Tank Marketplace utilizes Smart Contracts to secure future deals in stone on the blockchain.")

st.sidebar.text_input('Input your Company Name here:') 

st.sidebar.text_input('Input your company webpage here:') 

st.sidebar.text_input('Input your company thesis here:') 

st.sidebar.slider("How much money are you looking to raise?", 1000,1000000)

st.sidebar.slider("How much equity percentage (%) are you providing to the investors?", 1,100)

st.title("START INVESTING")

st.title("For investors")
st.level3 = st.sidebar.slider("How much money are you looking to invest?", 1000,1000000)

df = pd.read_csv('concatenated.csv')

#option = st.sidebar.selectbox("Please select a company you would like to invest in.",("Parser.run", "CancerIQ","Invitation codes","YCharts","Groupon","EVENTup","ParkWhiz","Food Genius","OpenAirplane","GiveForward","Rocketmiles","Classkick","Shortlist","Narrative Science","Packback","Storymix Media","Opternative","Shiftgig","Visible","Fooda","Cloudbot","Raise","Fourkites","Sprout Social","SpotHero"))
option = st.selectbox("Please select a company you would like to invest in.",sorted(df['Company'].unique()))

st.write(df[df['Company']==option]['Slogan/Pitch'].iloc[0])


