# End-to-End-Chest-Cancer-Classification-using-MLFlow-DVC-Deep-Learning-Project-

Deep Learning • VGG16 Transfer Learning • Flask API • Docker • AWS EC2 • ECR • GitHub Actions CI/CD

## Overview

This project implements an **end-to-end Deep Learning pipeline** for **Chest CT Scan Classification** (Adenocarcinoma vs Normal) using **VGG16 Transfer Learning**.

The project is **production-ready** with:

- Modular ML pipeline
- MLflow for experiment tracking
- DVC for pipeline orchestration
- Flask API for predictions
- Docker containerization
- AWS EC2 deployment with CI/CD via GitHub Actions

## Problem Statement

Early detection of **Adenocarcinoma**, a type of lung cancer, is critical.  
This project automates CT scan classification into:

- **Adenocarcinoma**
- **Normal**

## Why VGG16?

**VGG16** is a deep CNN pretrained on ImageNet that provides:

- Strong feature extraction for medical images
- Faster training via transfer learning
- Prevention of overfitting for small datasets
- High stability and reproducibility

**Approach:** Freeze convolutional layers, train a custom dense head for classification.\

## VGG16 Architecture (Used)

```bash
Input (224x224x3)
↓
VGG16 Convolution Base (Frozen)
↓
Flatten Layer
↓
Dense(256, ReLU)
↓
Dropout(0.5)
↓
Dense(2, Softmax)
```

## Project Architecture

```bash
End-to-End-Chest-Cancer-Classification/
│
├── .github/workflows/ # CI/CD pipeline
│ └── .gitkeep
│
├── config/
│ ├── config.yaml # Pipeline configs
│ └── secrets.yaml # Optional secrets
│
├── research/
│ └── trials.ipynb # Experimentation notebooks
│
├── templates/
│ └── index.html # Flask frontend (if needed)
│
├── src/
│ └── cnnClassifier/
│ ├── init.py
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_validation.py
│ │ ├── data_transformation.py
│ │ ├── model_trainer.py # VGG16 model
│ │ └── model_evaluation.py
│ │
│ ├── config/
│ │ ├── init.py
│ │ └── configuration.py
│ │
│ ├── pipeline/
│ │ └── training_pipeline.py
│ │
│ ├── entity/
│ │ └── config_entity.py
│ │
│ ├── utils/
│ │ └── common.py
│ │
│ └── constants/
│ └── init.py
│
├── app.py # Flask API for prediction
├── dvc.yaml # DVC pipeline
├── params.yaml # Hyperparameters
├── requirements.txt
├── setup.py
└── Dockerfile
```

This structure follows best practices used in MLOps-based ML systems.

## Tech Stack

### Programming & Deep Learning

- Python 3.8
- TensorFlow / Keras
- VGG16 Transfer Learning
- NumPy, Pandas, OpenCV

### Web & API

- Flask (REST API)
- HTML templates (optional for web frontend)

### MLOps & Engineering Tools

- MLflow – Experiment tracking, metrics, and model logging
- DVC – Data & model versioning, pipeline orchestration
- Docker – Containerization for reproducibility
- AWS EC2 – Cloud hosting and scalable deployment
- AWS ECR – Docker image registry
- GitHub Actions – CI/CD automation

## Features

- End-to-End Deep Learning Pipeline: From data ingestion to model deployment.
- VGG16 Transfer Learning: Pretrained CNN for feature extraction and improved accuracy.
- Automated Data Processing: Includes data ingestion, validation, and transformation.
- Model Training & Evaluation: Modular scripts for training, validation, and metrics logging.
- Flask API: Provides real-time predictions via REST endpoints.
- Dockerized Application: Containerized for portability and reproducibility.
- Cloud Deployment: Hosted on AWS EC2 with optional CI/CD.
- MLflow Integration: Tracks experiments, metrics, and artifacts.
- DVC Integration: Version control for datasets, models, and pipeline reproducibility.
- CI/CD with GitHub Actions: Automatic build, push, and deployment workflow.
- Secure Deployment: AWS IAM policies and Dockerized environments ensure security.

## Workflows to update the file

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## MLflow

[Documentation] (https://mlflow.org/docs/latest/index.html)

## Local Development Setup?

### STEP 01 - Clone the Repository

Clone the repository

```bash
git clone   https://github.com/DataWithGanesh/End-to-End-Chest-Cancer-Classification-using-MLFlow-DVC-Deep-Learning-Project-.git
```

### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n books python=3.9.25 -y
conda activate cancer
```

### STEP 03 - Install Install Dependencies

```bash
pip install -r requirements.txt
```

### STEP 04 - Git Commandas to push the code into github

```bash
git add .
git commit -m "readme update"
git push origin main
```

### STEP 05 - CMD

```bash
mlflow ui
```

### STEP 06 - DagsHub

MLFLOW_TRACKING_URI"= https://dagshub.com/DataWithGanesh/End-to-End-Chest-Cancer-Classification-using-MLFlow-DVC-Deep-Learning-Project-.mlflow
MLFLOW_TRACKING_USERNAME= DataWithGanesh
MLFLOW_TRACKING_PASSWORD = ab2ede637e99a9bf83b9da9e605ec45255bc088f

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/DataWithGanesh/End-to-End-Chest-Cancer-Classification-using-MLFlow-DVC-Deep-Learning-Project-.mlflow
export MLFLOW_TRACKING_USERNAME=DataWithGanesh
export MLFLOW_TRACKING_PASSWORD=ab2ede637e99a9bf83b9da9e605ec45255bc088f
```

### STEP - 07 - DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

### About MLflow & DVC

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & taging your model

DVC

- Its very lite weight for POC only
- lite weight expriements tracker
- It can perform Orchestration (Creating Pipelines)

## AWS CI/CD Deployment Guide – Chest Cancer Classification

**Objective:** Automatically build, push, and deploy your Dockerized Flask application for chest cancer classification to AWS using CI/CD.

### 1. AWS Setup

#### Step 1: Login to AWS Console

- Go to AWS Console
- Ensure your account has administrator access.

#### Step 2: Create IAM User for Deployment

1. Go to IAM → Users → Add User
2. Create a programmatic access user.
3. Attach the following policies:

- AmazonEC2FullAccess – for managing EC2 instances
- AmazonEC2ContainerRegistryFullAccess – for ECR Docker registry access

4. Save the Access Key ID and Secret Access Key.

#### Step 3: Create ECR Repository

1. Go to ECR → Create repository
2. Name: chest-cancer-app
3. Note the repository URI:
   566373416292.dkr.ecr.us-east-1.amazonaws.com/chest-cancer-app

### 2. EC2 Setup

#### Step 1: Launch EC2

- OS: Ubuntu 22.04 LTS
- Instance Type: t2.micro (free-tier)
- Key Pair: Create or use existing SSH key
- Security Group:
  -- Port 22 (SSH)
  -- Port 5000 (Flask API)

#### Step 2: Connect to EC2

```bash
ssh -i yourkey.pem ubuntu@<EC2-PUBLIC-IP>
```

#### Step 3: Install Docker

```bash
# Optional: Update packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Allow current user to run Docker without sudo
sudo usermod -aG docker ubuntu
newgrp docker
```

#### Step 4: Configure EC2 as Self-Hosted Runner (Optional)

- GitHub → Settings → Actions → Runners → New self-hosted runner
- Select OS → Follow commands provided to register runner
- This allows GitHub Actions to deploy directly to EC2.

### 3. GitHub Repository Setup

#### Step 1: Add Secrets

Go to GitHub → Settings → Secrets → Actions:

```bash
Secret Name	                Value
AWS_ACCESS_KEY_ID	      Your IAM Access Key
AWS_SECRET_ACCESS_KEY	  Your IAM Secret Key
AWS_REGION	              us-east-1
AWS_ECR_LOGIN_URI	      566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME	      chest-cancer-app
```

### 4. Docker Setup

#### Dockerfile

```bash
# Base image
FROM python:3.8-slim-buster

# Install AWS CLI
RUN apt update -y && apt install awscli -y

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask app
CMD ["python3", "app.py"]
```

#### Build & Run Locally

```bash
docker build -t chest-cancer-app .
docker run -d -p 5000:5000 chest-cancer-app
```

Access app:

```bash
http://localhost:5000
```

### 5. GitHub Actions CI/CD Workflow

main.yaml file

### 6. Access Application

```bash
http://<EC2-PUBLIC-IP>:5000
```
