# MLOps-Assignment (Flask, HTML, CSS, Pycaret)
## Folder Structure 
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/c14b34d0-4a43-4e9c-bcec-cfda0f21722a)

---
## Deployment Guide 
### 1. Running of PyCaret notebooks to save the pipeline models (/models) stored locally in the pc
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/c9ce5c95-5742-4808-bb5e-756be74db3be)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/ff9dd021-ec38-4f40-888d-1eefb6ae7c51)
### 2. Open an anaconda promopt
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/71077f2e-27d5-4ecd-a858-361be49b4b00)
### 3. Activate the conda virtual pre-created with the relevant libraries installed (Flask, Mlflow, Pycaret)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/5365d8a2-9519-489c-8182-5a69a33a61c6)
### 4. Running and testing the web application for cardio in the environment
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/40e3af44-cd0b-4249-80be-149abb5ab1f0)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/69412df1-f62b-4ee1-bf20-6aca98474f76)
### 5. Leave the web app for cardio and open the one for resale price and test it out
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/ebb443f2-edb2-4f29-9c56-720eb3224461)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/4ba7f6a9-fefc-4f70-9345-f3052a646a8d)
### Conclusion: Now the applications can be used to predict MLops usage.




---
## Web Application (Resale Price Prediction) using Regression (Abinaya)
### Data Cleaning
#### I did some data cleaning for my dataset. There is this column name month. It is in YYYY/MM format. So I decided to split the year from the month column. The image below shows how I did it.
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/27313963-9487-4152-9146-48279ccf2eb1)
#### The end result:
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/8ed37ef0-fabc-4d24-9a16-885954953f16)
#### I also removed columns with low feature importance. I did modeling with all the columns to find out columns with low importance. The image below shows the feature importance chart
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/eae8df6f-3b5c-4e6f-956e-ae830b356543)
#### Below shows the code I used to remove the columns 
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/55572f68-cfce-44b1-88d7-43cdf142fa85)
#### I also checked for null values
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/aa2e1d24-d9bc-49b1-a236-9d906300988b)
### Modelling
#### The Set- Up
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/ef24bffd-38af-4278-b140-d2b5b25b59f5)
#### Comparing Models. My best Model is K-Neighbour Regression
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/d8be8297-dbd5-44b0-8f90-1fdbe5534299)
#### Plotting Best Model
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/be425834-7b5f-4be5-8efd-b6cf01726ed0)
#### Proof of Model Registration
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/d58cd6c6-e0b8-488b-9b01-fbf2fe3e324f)

![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/f46ce51a-0333-4b7c-a8a1-03f3ecee912f)
### Testing whether my model predicts
#### I created a new dataset with unique records to see whether my model predicts
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/93484029-b46d-4fb9-9a7a-aaa60bda3683)
### Web Application
#### The Layout
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/690de47c-3fd4-4105-bbdb-f5929ca844b9)
#### The Prediction
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/a9c533f7-aaed-4b7d-b53c-9b1904628c39)

### Task 4 (Hydra, DVC and Poetry)
#### Cookiecutter
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/eef7e6b8-4af7-4a93-8e24-45b3b648a697)
#### main.yaml file configuration
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/f626d558-84b2-4f79-a249-f3c44c429747)
#### Hydra code to automatically captures the parameters
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/463d1900-5edc-40b5-be12-987ef9bff053)
####  command to initialize a new Git repository in a directory
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/3ad6361c-3844-4122-a962-49df59477178)
#### command to initialize a new Data Version Control (DVC) repository for my project.
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/f734f21c-5a5b-428a-a3d3-e9003194adc3)
#### Initializing DVC
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/ea8ecd3d-d0a2-46bd-8536-86a4b8010192)
#### Monitoring the updates of the dataset using data version control
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/c51eb209-5c55-4f39-89cb-3890f5da8c9b)
#### Fulfiling requirements from the requirements.txt file using MakeFile
![image](https://github.com/YapSam/MLOps-Assignment-/assets/109716754/84672892-0d09-449f-865a-b557ed6373da)


## Web Application (Cardiovascular Issue Prediction) using Classification
### Modeling and Preprocessing
#### Setup with preprocessing methods for Classification 
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/360a600a-122c-4d2a-8826-654b4d1e9ee9)
#### Comparing Models. My best Model is Cat-Boost Classifier
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/db6d0c1f-e2f4-40ac-a423-077a7dcf09a8)
#### Plotting Best Model
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/61c2fc75-39c2-4d8c-9156-577e02b57ad2)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/53ef9110-3e5d-4e9e-8545-41338c356997)
#### Proof of Model Registration
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/4d5f289b-c1ed-4137-8d39-18d94843d4cf)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/cb6e8d23-5fc5-4814-b868-95da4b2da717)

### Prediction of unseen data
#### A dataset is created to see what the cv_status is predicted as
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/be1c33be-a614-4557-84c9-eee5477f46d3)

### Web Application
#### The Layout
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/cba7a004-c851-45ad-b149-54728a46d340)
#### Prediction Output
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/33b38d38-3191-43e8-bc82-5654e8f8e3c0)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/348e3a5d-2e98-4607-b5d3-47fe56e029a8)

### Task 4 (Hydra, DVC and Poetry)
#### Cookiecutter
#### config.yaml file configuration
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/e3975224-3430-4944-913d-d9edf7fe6e92)
#### Hydra code to automatically captures the parameters for .py and .ipynb files
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/4909ae44-f981-4b4e-a0da-011a01ddaaf8)
#### command to initialize a new Git repository in a directory and new Data Version Control (DVC) repository for my project
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/d03e47c0-5c59-496e-8879-61a29adbbb0e)
#### Initializing DVC
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/ca15b423-7242-4b08-9f8f-5ce84e725dc7)
#### Monitoring the updates of the dataset using data version control
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/d1c368f4-89ad-4a71-a40a-9bec8521c5a1)
#### Fulfiling requirements from the requirements.txt file using MakeFile, Poetry 
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/3ebb8f2a-04d6-4227-8a57-71e7e8f3efec)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/c5b733dc-164f-4193-9795-bf6864255bd9)
#### Attempt deployment to Pass server using Netlify (Failed)
![image](https://github.com/YapSam/MLOps-Assignment-/assets/133552118/f3d65382-b279-4cee-a318-e00ab2cfc969)

