from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os

MODEL = os.environ.get('MODEL', 'cardiffnlp/twitter-roberta-base-sentiment')
TOKENIZER = os.environ.get('TOKENIZER', 'cardiffnlp/twitter-roberta-base-sentiment-latest')

AutoModelForSequenceClassification.from_pretrained(MODEL)
AutoTokenizer.from_pretrained(TOKENIZER)
