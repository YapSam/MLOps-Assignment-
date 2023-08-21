# MLOps-Assignment (Flask, HTML, CSS, Pycaret)-
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














## Web Application (Cardiovascular Issue Prediction) using Classification
Exploratory Data Analysis 

