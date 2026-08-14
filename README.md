# Vodafone Billing Predictor - ML + GitHub Actions

A simple classroom example showing how a Vodafone billing prediction model can be trained automatically using GitHub Actions.

## Project Flow

Customer Billing Data
        |
        v
   billing.csv
        |
        v
   train.py
        |
        v
 Linear Regression
        |
        v
   Quality Gate
   MAE <= 10
        |
        v
 billing_model.pkl
        |
        v
   predict.py

## 1. Install Python

Use Python 3.11 or later.

## 2. Create a virtual environment

Windows:

    python -m venv .venv
    .venv\Scripts\activate

Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate

## 3. Install dependencies

    pip install -r requirements.txt

## 4. Train locally

    python train.py

This creates:

    billing_model.pkl

## 5. Test prediction

    python predict.py

## 6. Push to GitHub

    git init
    git add .
    git commit -m "Initial Vodafone billing ML project"
    git branch -M main
    git remote add origin YOUR_GITHUB_REPOSITORY_URL
    git push -u origin main

After the push, GitHub Actions automatically:

1. Checks out the code
2. Installs Python
3. Installs ML libraries
4. Trains the model
5. Evaluates the model
6. Applies the MAE quality gate
7. Runs a prediction
8. Uploads billing_model.pkl as a workflow artifact

## Important MLOps Concept

The workflow demonstrates:

Data -> Training -> Evaluation -> Quality Gate -> Model Artifact

If MAE is greater than 10, the GitHub Action fails.

If MAE is 10 or lower, the model is accepted and uploaded as an artifact.

## Classroom Exercise

Change a value in data/billing.csv and push again:

    git add data/billing.csv
    git commit -m "Update billing data"
    git push

Then open the Actions tab in GitHub and observe the automatic retraining.

## Note

The billing values are synthetic classroom data and are not real Vodafone customer data.
