# Sentiment Analysis - Amazn Alexa Review

## Project Overview

This project trains and evaluates multiple machine-learning models to classify Amazon Alexa customer reviews into three sentiment categories: **Negative**, **Neutral**, and **Positive**. We use TF-IDF vectorization on raw text and compare five classifiers:

- Logistic Regression  
- Support Vector Machine (linear kernel)  
- Support Vector Machine (RBF kernel)  
- Random Forest  
- XGBoost  

After training and cross-validation, **Logistic Regression** achieved the best balanced accuracy. All trained artifacts (TF-IDF vectorizer + model files) are stored under `trained_models/`. A minimal script (`run_model.py`) loads those pickles and predicts on custom text inputs.

---

## Data & Preprocessing

1. **Source**  
   We used the publicly available Amazon Alexa reviews dataset (TSV format).

2. **Cleaning**  
   - Removed rows with missing review text.  
   - Lowercased all text and removed punctuation.  
   - Performed tokenization and stop-word removal.  

3. **Vectorization**  
   - Built a TF-IDF vectorizer (unigrams + bigrams) on the training split.  
   - Serialized the fitted `TfidfVectorizer` as `trained_models/vectorizer.pkl` for inference.  

---

## Models Trained

Within `model_training.ipynb`, we trained, cross-validated, and evaluated:

1. **Logistic Regression**  
2. **SVM (Linear Kernel)**  
3. **SVM (RBF Kernel)**  
4. **Random Forest**  
5. **XGBoost**

Each model was evaluated on a held-out test set after 5-fold cross-validation.

---

## Results Summary

Below is a consolidated table of test-set performance for all five models:

| Model                | Test Accuracy | Balanced Accuracy | 5-Fold CV Score (± std) | Macro F1 | Negative F1 | Neutral F1 | Positive F1 |
|----------------------|---------------|-------------------|-------------------------|----------|-------------|------------|-------------|
| Logistic Regression  | 0.9233        | 0.7427            | 0.9877 (± 0.0038)       | 0.7380   | 0.651       | 0.600      | 0.963       |
| SVM (Linear Kernel)  | 0.9282        | 0.7220            | 0.9923 (± 0.0026)       | 0.7522   | 0.667       | 0.627      | 0.962       |
| SVM (RBF Kernel)     | 0.9266        | 0.6195            | 0.9988 (± 0.0021)       | 0.7071   | 0.433       | 0.727      | 0.961       |
| Random Forest        | 0.8825        | 0.5488            | 0.8813 (± 0.0465)       | 0.5682   | 0.460       | 0.304      | 0.941       |
| XGBoost              | 0.9380        | 0.7415            | 0.9752 (± 0.0525)       | 0.7627   | 0.762       | 0.556      | 0.971       |


---

## Running Inference

1. **Ensure Pickle Files Are Present**  
   - `trained_models/vectorizer.pkl`  
   - `trained_models/logistic_regression.pkl` (or whichever model you choose)


2. **Adjust `config.py` (if needed)**  
   ```python
   model_filepath  = "trained_models/logistic_regression.pkl"
   vectorizer_path = "trained_models/vectorizer.pkl"
   ```

    Change model_filepath to point to svm_linear.pkl, xgboost.pkl, etc., if desired.

3. **Run the Script**
    ```bash
    python run_model.py
    ```

    You will be prompted : 

    ```bash
    Type your input :
    ```

