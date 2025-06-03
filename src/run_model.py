import os
import pickle
import warnings
import logging
from config import model_filepath, vectorizer_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings('ignore')

labels_map = {
    0 : 'Negative',
    1 : 'Neutral',
    2 : 'Positive'
}

def load_models():
    with open(vectorizer_path, 'rb') as vf:
        vectorizer = pickle.load(vf)

    with open(model_filepath, 'rb') as mf:
        model = pickle.load(mf)

    return vectorizer, model


vectorizer, model = load_models()
logging.info('Loading the models...')

def predict(text: str, return_label : bool=False):
    X = vectorizer.transform([text])       # transform to the same TF-IDF format
    pred_num = model.predict(X)[0]

    if return_label:
        return labels_map.get(pred_num, str(pred_num))
    return pred_num

logging.info('Starting the prediction...')

# sample_text = "I absolutely loved the product and it works like a charm!"

sample_text = input('Type your input :')
logging.info('Processing your input...')
num_label = predict(sample_text)
human_label = predict(sample_text, return_label=True)

print(f"Numeric prediction: {num_label}")
print(f"Readable prediction: {human_label}")
