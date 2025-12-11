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
