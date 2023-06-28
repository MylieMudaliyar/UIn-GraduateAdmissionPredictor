import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('new_model.pkl','rb'))

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:darkblue'>Welcome To UIn</h1><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: White;background-color:maroon'>A Graduate Admission Predictor</h1><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: White;background-color:lightblue'>Drop Your Scores</h3><br>", unsafe_allow_html=True)
 
    cgpa = st.slider("CGPA",0.0,10.0)
    gre = st.slider("GRE Score",0,340)
    toefl = st.slider("TOEFL Score",0,120)
    research = st.radio("Do You have Research Experience? (0 = NO, 1 = YES)",(0,1))
    sop_rating = st.slider("Rating of your SOP on a Scale 1-5",1.0,5.0)
    lor_rating = st.slider("Rating of your LOR on a Scale 1-5",1.0,5.0)
    uni_rating = st.slider("Rating of the University you wish to get in on a Scale 1-5",1,5)

    inputs = [[cgpa,gre,toefl,lor_rating,sop_rating,research,uni_rating]]

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(float)
        probability = updated_res.item()
        percentage = probability * 100
        formatted_percentage = "{:.2f}%".format(percentage)
        st.success('Your chance of getting in is {} .'.format(formatted_percentage))
        st.markdown("<h1 style='text-align: center; color: White;background-color: lightblue'>GOOD LUCK :)</h1><br>", unsafe_allow_html=True)
if __name__ =='__main__':
  main()

