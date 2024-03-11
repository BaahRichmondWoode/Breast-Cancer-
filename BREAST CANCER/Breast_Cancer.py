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
model_selection= st.sidebar.selectbox('Select Model',['Logistic Regression','Decision Tree Model'])

#Using Logistic Regression Model
if model_selection == 'Logistic Regression':
    def Logistic_Regression():
        if upload is not None:
            dataset_input = pd.read_csv(upload)
            # radius_se	compactness_worst	concave_worst	concave_points
            dataset_input = dataset_input[['radius_mean','concavity_mean','concavity_worst','concave points_worst']]
        else:
            def data_input():
                #Radius Standard Error
                radius_se = st.sidebar.number_input('Radius_se',min_value=0.0,max_value=2.873)

                #Compactness Worst
                compactness_worst= st.sidebar.number_input('Compactness Worst',min_value=0.0,max_value=1.058)

                #Concavity Worst
                concavity_worst = st.sidebar.number_input('Concavity Worst',min_value=0.0,max_value=1.252)

                #Concave Points Worst
                concave_points = st.sidebar.number_input('Concave Points Worst',min_value=0.0,max_value=0.291)

                #st.write(concavity_worst)
                data= DataFrame({'radius_se':[radius_se],'compactness_worst':[compactness_worst],
                              'concavity_worst':[concavity_worst],'concave points_worst':[concave_points]})
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

# Decision Tree Model
elif model_selection == 'Decision Tree Model':
    def Decision_Tree_Model():
        if upload is not None:
            dataset_input = pd.read_csv(upload)
            dataset_input = dataset_input[['concave points_mean','radius_worst','texture_worst','concavity_worst']]
        else:
            def data_input():
                # Concave points mean
                Concave_points_mean= st.sidebar.number_input('Concave Points Mean', min_value=0.0, max_value=0.201200)

                # Radius Worst
                Radius_worst = st.sidebar.number_input('Radius Worst', min_value=7.93000, max_value=36.040000)

                # Texture Worst
                Texture_worst = st.sidebar.number_input('Texture Worst', min_value=12.0200, max_value=49.54000)

                # Concave Points Worst
                concave_points = st.sidebar.number_input('Concave Points Worst', min_value=0.0, max_value=0.291)

                # st.write(concavity_worst)
                data = DataFrame({'concave_se': [Concave_points_mean], 'radius_worst': [Radius_worst],
                                  'Texture_worst': [Texture_worst], 'concave points': [concave_points]})
                return data
            dataset_input = data_input()

        # Loading the Decision Tree Model
        with open('DecisionTree.pkl','rb') as f:
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
    Decision_Tree_Model()
diagnosis = []
