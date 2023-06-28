"""
Imports MymemoryTranslator from deep_translator
"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """
    This function to translate english to french
    """
    frenchtext = MyMemoryTranslator(source='english', target='french').translate(englishtext)
    return frenchtext
def frenchtoenglish(frenchtext):
    """
    This function to translate french to english
    """
    englishtext = MyMemoryTranslator(source='french',target='english').translate(frenchtext)
    return englishtext
    