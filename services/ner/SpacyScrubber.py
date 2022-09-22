import spacy
import logging

logger = logging.getLogger(__name__)

class SpacyScrubber():
    
    def __init__(self, 
                 classes=['PERSON', 'ORG']
                ): 
        
        self.classes = set(classes)

    def load(self):
        logger.warning("loading model")
        self.nlp = spacy.load('en_core_web_md')
        
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
        scrubbed = text
        ents = self.identify(text)
        
        if ents:
            scrubbed = self.scrub(text, ents)

        
        return {
            "scrubbed": scrubbed,
            "ents": ents
        }
        
