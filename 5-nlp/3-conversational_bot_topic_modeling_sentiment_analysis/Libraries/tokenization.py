import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

nlp = spacy.load('es_core_news_sm')

def tokenize(_frase, language='spanish'):
    """
    Tokeniza una frase en palabras individuales, eliminando cualquier carácter no alfabético y convirtiendo
    todas las palabras a minúsculas.

    Args:
    _frase (str): La frase que se quiere tokenizar.

    Returns:
    list: Una lista de tokens alfabéticos en minúsculas.
    """

    tokens = word_tokenize(_frase, language)
    tokens = [word.lower() for word in tokens if word.isalpha()]

    return tokens



def clean_sw(_tokens, language='spanish'):
    """
    Removes stopwords from a list of tokens based on the specified language.

    Args:
    _tokens (list of str): List of tokens (words) from which the stopwords will be removed.
    language (str, optional): The language of the stopwords. Defaults to 'spanish'.

    Returns:
    list of str: A list of tokens with the stopwords removed.

    Note:
    The function uses the NLTK library's list of stopwords for the removal. Ensure that
    the 'stopwords' dataset from NLTK is downloaded before using this function.
    """
    clean_tokens = _tokens[:]

    for token in _tokens:
        if token in stopwords.words(language):
            clean_tokens.remove(token)

    return clean_tokens



def lematize(_tokens):
    lem_tokens = []

    separator = ' '

    for token in nlp(separator.join(_tokens)):
        lem_tokens.append(token.lemma_)

    return lem_tokens



def my_stopwords(_tokensIn):
    """
    Cleans a list of tokens by removing specific unwanted tokens.

    This function iterates through a list of tokens and removes any that are found 
    in the predefined `_toDelete` list.

    Args:
    _tokensIn (list of str): The input list of tokens to be cleaned.

    Returns:
    list of str: A cleaned list of tokens with specific words removed.
    """
    
    _toDelete = ['tigre', 'buenos', 'aires', 'victoria', 'josé', 'dellagiovanna', 'zona', 'norte']

    _tokens = _tokensIn[:]
    for token in _tokensIn:
        if token in _toDelete:
            _tokens.remove(token)

    return _tokens