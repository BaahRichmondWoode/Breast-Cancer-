# Importation fo data
import pandas as pd
import streamlit as st
import pickle as pk
from pandas import DataFrame

# Setting Title
st.title('Breast Cancer Prediction')
st.sidebar.header('Inputs Features')

#Uploading CSV file from destop
upload = st.sidebar.file_uploader('Upload your csv file',type=['csv'])
#Using Logistic Regression Model
def Logistic_Regression():
    if upload is not None:
        dataset_input = pd.read_csv(upload)
        # radius_se	compactness_worst	concave_worst	concave_points
        dataset_input = dataset_input[['radius_mean', 'texture_se', 'radius_worst', 'concavity_worst','concave points_worst']]
    else:
        def data_input():
            #Radius Mean
            radius_mean = st.sidebar.number_input('radius_mean',min_value=6.98100,max_value=28.1100)

            # Radius Worst
            radius_worst = st.sidebar.number_input('radius_worst', min_value=7.93000, max_value=36.04000)

            #Texture Standard Error
            texture_se= st.sidebar.number_input('texture_se',min_value=0.360200,max_value=4.885000)

            #Concavity Worst
            concavity_worst = st.sidebar.number_input('Concavity Worst',min_value=0.0,max_value=1.252)

            #Concave Points Worst
            concave_points = st.sidebar.number_input('Concave Points Worst',min_value=0.0,max_value=0.291)

            #st.write(concavity_worst)
            data= DataFrame({'radius_mean':[radius_mean],'radius_worst':[radius_worst],'concavity_worst':[concavity_worst],
                              'texture_se':[texture_se],'concave points_worst':[concave_points]})
            return data
        dataset_input = data_input()

    # Loading of the Logistic Trained Model
    with open('LogisticModel.pkl', 'rb') as f:
        model = pk.load(f)
    predicted = model.predict(dataset_input)
    button = st.sidebar.button('Predict')
    if button:
        st.dataframe(dataset_input)
        diagnosis = []
        for i in predicted:
            if i == 0:
                diagnosis.append('Bagnanit')
            else:
                diagnosis.append('Magninant')
        st.dataframe({'Predicted Value': diagnosis})
Logistic_Regression()
diagnosis = []