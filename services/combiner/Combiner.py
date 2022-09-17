import logging
import numpy as np

class Combiner(object):

    def aggregate(self, X, features_names=[], meta=[]):
        logging.info("Input: " + str(X))
        output = {
            "ner": X[0],
            "sentiment": X[1]
        }
        logging.info("Output: " + str(output))
        return output
