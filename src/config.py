import os

# File paths
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         # gets the root dir of the project

data_dir = os.path.join(root_dir, 'data')                                      # the data directory under the root
alexa_dir = os.path.join(data_dir, 'alexa_reviews')                            # alexa reviews dir under the data directory
models_dir = os.path.join(data_dir, 'models')
tsv_filepath = os.path.join(alexa_dir, 'amazon_alexa.tsv')

# models paths
model_dir = os.path.join(root_dir, 'trained_models')
vectorizer_file = 'vectorizer.pkl'
model_file = 'logistic_regression.pkl'                                          # change the model 

vectorizer_path = os.path.join(model_dir, vectorizer_file)
model_filepath = os.path.join(model_dir, model_file)