<h1>Breast Cancer Prediction GUI</h1>
<p>This project implements a Graphical User Interface (GUI) using Streamlit for breast cancer prediction. The prediction model utilized are Logistic Regression.
  The project aims to provide a user-friendly interface for predicting breast cancer based on input data. 
  The classification models are trained on the breast cancer dataset and incorporate feature selection and addressing class imbalance.</p>

<h2>Libraries Used</h2>
  <li>
    <ol>Pandas</ol>
    <ol>NumPy</ol>
<ol>Streamlit</ol>
<ol>Seaborn</ol>
<ol>Scikit-learn (sklearn)</ol>
  </li>
<h2>Project Procedures</h2>
<li>
  <lo><h3>Importing Necessary Libraries:</h3></lo>The program was written fully in python. The required libraries for data manipulation, visualization, and model building are imported.

<lo><h3>Importing the Breast Cancer Dataset:</h3></lo>The breast cancer dataset is imported for analysis and model training.

<lo><h3>Dataset Splitting:</h3></lo> The dataset is split into three subsets: training, testing, and validation data.

<lo><h3>Feature Selection:</h3></lo> Recursive Feature Elimination (RFE) is employed to select the most important features for model training.

<lo><h3>Handling Class Imbalance:</h3></lo> The trained dataset is checked for class imbalance. To address this issue, the target variables are grouped into strata based on their properties and characteristics. An equal number of data points are then sampled from each stratum to ensure representation from all classes using <b>Under Sampling Majority Technique</b>.

<lo><h3>Fitting New Features with Target Variables:</h3></lo>The selected features are fitted with the target variables.

<lo><h3>Model Evaluation:</h3></lo>
<h4>Fitting Recursive Feature Elimination Model with Test Dataset:</h4> The RFE model feature selection is fitted with the test dataset, and predictions are made using the model trained with the trained dataset.
<h4>Performance Metrics:</h4> Compute F1 score, precision score, and recall score. Display a chart of the confusion matrix.

<lo><h3>Model Deployment:</h3></lo>
 The models are deployed individually using pickle and loaded in PyCharm for building the GUI using Streamlit.
</li>
<p>
  Below is a picture of the Graphical User Interface
</p>
https://github.com/BaahRichmondWoode/Breast-Cancer-/blob/main/BREAST%20CANCER/Breast_Cancer_Interface.PNG
