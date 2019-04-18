from flashtext.keyword import KeywordProcessor
import pickle

# Function that loads in our pickled word processor
# and defines a function for using it. This makes it easy
# to do these steps together when serving our model.
def get_keywords_api_python():
    
    # read in pickled word processor. You could also load in
    # other models as this step.
    keyword_processor_python = pickle.load(open("processor.pkl", "rb"))
    
    # Function to apply our model & extract keywords from a 
    # provided bit of text
    def keywords_api_python(keyword_processor_python, text, span_info=True): 
        keywords_found = keyword_processor_python.extract_keywords(text, span_info=True)      
        return keywords_found
    
    # return the function we just defined
    return keywords_api_python

def get_keywords_api_r():
    
    # read in pickled word processor. You could also load in
    # other models as this step.
    keyword_processor_r = pickle.load(open("r_processor.pkl", "rb"))
    
    # Function to apply our model & extract keywords from a 
    # provided bit of text
    def keywords_api_r(keyword_processor_r, text, span_info=True): 
        keywords_found = keyword_processor_r.extract_keywords(text, span_info=True)      
        return keywords_found
    
    # return the function we just defined
    return keywords_api_r

def useless_function():
    """ 
    A function that returns some text
    """
    return("some text")
