# DataTalk MidTerm Project 2023 November


## Data Source
https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis


## Project Description
There is one column call "complain". In that datasets, 0 is not complain and 1 is complain. I try to find out most related columns from dataset and train with LogisticRegression.

## Note for Files

Dockerfile is for Docker Build  
Notebook.ipynb is cleaning and working notebook
Pipfile and Pipfile.lock is for environment
app.py is for flask and load model
complain_forecast.pkl is model
data.tsv is source file
train.py is to retrain the model

## To retrain the Dataset
python train.py

## note for pipenv setup

pipenv --python 3.10  
pipenv install flask  
pipenv install gunicorn  
pipenv install numpy  
pipenv install scikit-learn==1.3.1  

## Build Docker

sudo docker build -t midterm-project-phyokyi .

## Run Docker

sudo docker run -it --rm -p 2001:2001 midterm-project-phyokyi

## Sample curl request for result "not complain"
curl -X POST -H "Content-Type: application/json" -d '{"kidhome": 0, "education_phd": 1, "education_2n_cycle": 0, "education_graduation": 0, "mntwines": 100, "mntgoldprods": 100, "year_birth": 1990, "income": 40000}' https://public_url/predict

## Sample curl request for result "complain"
curl -X POST -H "Content-Type: application/json" -d '{"kidhome": 0, "education_phd": 1, "education_2n_cycle": 0, "education_graduation": 0, "mntwines": 10, "mntgoldprods": 10, "year_birth": 1990, "income": 40000}' https://public_url/predict

## Working Screenshot
![image](https://github.com/phyokyi/datatalk_midterm_project_202311/assets/12389166/ab535356-1d2a-4947-8e15-67ba5bffe968)
