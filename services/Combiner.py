import logging
import numpy as np

class Combiner(object):

    def aggregate(self, X, features_names=[]):
        logging.info("Input: " + str(X))
        output = {
            "Model0": X[0].tolist(),
            "Model1": X[1].tolist(),
        }
        logging.info("Output: " + str(output))
        return output
