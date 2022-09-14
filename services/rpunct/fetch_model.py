from punctuate import RestorePuncts

def cache_model():
    model = RestorePuncts()
    model.model.convert_to_onnx('/app/model')


cache_model()    