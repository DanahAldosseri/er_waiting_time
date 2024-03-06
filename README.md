
# Emergency Room Waiting Time Prediction 
## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Technologies Used](#Technologies-Used)
3. [Libraries Used](#Libraries-Used)
4. [Dataset Information](#Dataset-Information)
* [Size of the dataset](#Size-of-the-dataset)
* [Features used](#Features-used)
5. [Dataset Preprocessing](#Dataset-Preprocessing)
6. [Model Used](#Model-Used)
* [Model Evaluation](#Model-Evaluation)
7. [API Reference](#API-Reference)
* [API Endpoints](#API-Endpoints)
8. [Installation](#Installation)
9. [Deployment](#Deployment)
10. [Areas of Improvement](#Areas-of-Improvement)
## Project Overview
The  Emergency Room Waiting Time Prediction project aims to provide a predict of the ER waiting time using machine learning model, to manage patient flow more effectively.


## Technologies Used
Project is created with:
* Jupyter notebook (python)
* Visual studio code (python, html and css)
* Flask API
## Libraries Used
For data preprocessing:
*  pandas

For model building:
* xgboost
* sklearn
* joblib

For API building:
* flask
* wtforms
* flask_wtf
* datetime

## Dataset Information

The dataset were a real-world data from the hospital.

### Size of the dataset
* Orginal dataset size: (362359, 39)
* Cleaned dataset size: (278697, 8)

### Features used
* Facility
* Acuity level
* Building
* Admit mode
* Day of the week
* Age
## Dataset Preprocessing
The data cleaning was done by:
* Droping unnecessary columns.
* Droping coulmns that contains a masive amount of missing values.
* Dealing with columns that has the same values by keeping one column and droping the rest. 
* Droping rows that has Null/missing values.
* Adding columns.
## Model Used

The machine learning model used in this project is the xgboost regression model with grid seach to find the best parameters. 

The project has 5 models, model for each Acuity level. After the models were trained, each individual model is saved using joblib.

### Model Evaluation

The model's prefomrmance is evaluated using:
* Mean Absolute Error(MAE).
* Mean Squared Error(MSE).
## API Reference
A flask API was used with the help of HTML, CSS and JavaScript to devolpe a web application. 

### API Endpoints
#### To display the home page

```http
  GET /
```

#### To start prediction

```http
  POST /index
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `FACILITY` | `string` | SelectFiled |
| `ACUITY_LEVEL` | `string` | SelectFiled |
| `BUILDING` | `string` | SelectFiled |
| `ADMIT_MODE` | `string` | SelectFiled |
| `DAY_OF_WEEK` | `string` | datetime |
| `Age` | `integer` | **Required**. IntegerFiled |




## Installation

To install ER waiting time prediction project:

```bash
  git clone https://github-ent-p.kfshrc.edu.sa/CHI/er_waiting_time.git
  cd er_waiting_time
```
    
## Deployment

To deploy this project run the api python file using this command:

```bash
  python api.py
```


## Areas of Improvement
* Model preformance
* Data Preprocessing
