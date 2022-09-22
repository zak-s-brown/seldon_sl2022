from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import logging
import os
import urllib

logger = logging.getLogger(__name__)

class Sentiment():
    
    def __init__(self): 

        self.task = 'sentiment'
        self.MODEL = os.environ.get('MODEL', 'cardiffnlp/twitter-roberta-base-sentiment')
        self.TOKENIZER = os.environ.get('TOKENIZER', 'cardiffnlp/twitter-roberta-base-sentiment-latest')
        logger.warning(self.MODEL)

    def load(self):
        logger.warning("loading model and tokenizer")

        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL, local_files_only=True)

        self.tokenizer = AutoTokenizer.from_pretrained(self.TOKENIZER, local_files_only=True)
            
    def predict(self, ndarray, names=[], meta=[]):
        logger.warning(ndarray)
        logger.warning(meta)
        logger.warning(names)
        text = str(ndarray[0])
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores).tolist()
        
        
        return {
            "scores": scores
        }
        
