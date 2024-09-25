# Set up Streamlit app

import streamlit as st


st.title('AI Web Scrapper for Job Search')
st.write('This is a web scrapper that uses AI to find jobs for you. Just enter the job title and location and let the AI do the rest!')
st.write('Created by: [Tijani Saheed](https://www.linkedin.com/in/sotijani/)')

job_title = st.text_input('Enter the job title')
location = st.text_input('Enter the location')

if st.button('Find Jobs'):
    st.write('Finding jobs...')
    st.write('Here are the jobs found:')
    st.write('Job 1')
    st.write('Job 2')
    st.write('Job 3')
    st.write('Job 4')
    st.write('Job 5')
    st.write('Job 6')

st.write('Thank you for using the AI Web Scrapper for Job Search!')
