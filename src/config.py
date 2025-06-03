import os

# File paths
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(root_dir, 'data')
alexa_dir = os.path.join(data_dir, 'alexa_reviews')
tsv_filepath = os.path.join(alexa_dir, 'amazon_alexa.tsv')