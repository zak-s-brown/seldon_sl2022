import spacy
import logging

logger = logging.getLogger(__name__)

class RPunct():
    
    def __init__(self): 
        
        logger.warning('Initializing')

    def load(self):
        logger.warning("Loading Model")
    
    
    def predict(self, ndarray, feature_names):
        text = str(ndarray[0])
        punctuated = text
        
        return {
            "punctuated": punctuated
        }
        
