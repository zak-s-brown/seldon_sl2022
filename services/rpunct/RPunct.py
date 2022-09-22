import logging
from punctuate import RestorePuncts

logger = logging.getLogger(__name__)

class RPunct():
    
    def __init__(self): 
        
        logger.warning('Initializing')

    def load(self):
        logger.warning("Loading Model")
        self.model = RestorePuncts(model_name='/app/model')
        logger.warning("Model Loaded")

    
    
    def predict(self, ndarray, names=[], meta=[]):
        logger.warning(ndarray)
        logger.warning(meta)
        logger.warning(names)
        text = str(ndarray[0])
        
        try:
            punctuated = self.model.punctuate(text)

        except Exception as e:
            punctuated = text

        return [punctuated]
        
