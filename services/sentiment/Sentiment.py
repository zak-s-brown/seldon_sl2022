from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import logging
import os
import urllib

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
 
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

logger = logging.getLogger(__name__)

class Sentiment():
    
    def __init__(self): 

        # Tasks:
        # emoji, emotion, hate, irony, offensive, sentiment
        # stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary
        self.task = 'sentiment'
        self.MODEL = os.environ.get('MODEL', 'cardiffnlp/twitter-roberta-base-sentiment')
        self.TOKENIZER = os.environ.get('TOKENIZER', 'cardiffnlp/twitter-roberta-base-sentiment-latest')
        logger.warning(self.MODEL)

        #self.mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{self.task}/mapping.txt"

    def load(self):
        logger.warning("loading model")
        # download label mapping
        #labels=[]
        #with urllib.request.urlopen(self.mapping_link) as f:
        #    html = f.read().decode('utf-8').split("\n")
        #    csvreader = csv.reader(html, delimiter='\t')
        #labels = [row[1] for row in csvreader if len(row) > 1]

        # PT
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL, local_files_only=True)
        #self.model.save_pretrained(self.MODEL)

        self.tokenizer = AutoTokenizer.from_pretrained(self.TOKENIZER, local_files_only=True)
        
    def identify(self, text):
        doc = self.nlp(text)
        
        output = []
        
        if doc.ents:
            output = [
                {
                    'start': e.start_char, 
                    'end': e.end_char, 
                    'class': e.label_, 
                    'text': e.text
                }
                for e in doc.ents if e.label_ in self.classes
            ]

        return output
    
    def scrub(self, text, ents):
        
        i = 0
        res = ''
        for ent in ents:
            res += text[i:ent['start']] + str(f"[{ent['class']}]")
            i = ent['end']
        res += text[ent['end']:]
        return res 
            

    def predict(self, ndarray, names=[], meta=[]):
        logger.warning(ndarray)
        logger.warning(meta)
        logger.warning(names)
        text = str(ndarray[0])
        text = preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores).tolist()
        
        
        return {
            "scores": scores
        }
        
