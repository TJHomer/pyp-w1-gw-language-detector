# -*- coding: utf-8 -*-

from .languages import LANGUAGES

def detect_language(text, languages):
    available_languages = {'English': 0, 'Spanish': 0, 'German': 0}

    for word in text.split(' '):
        for language in languages:
            if word in language['common_words']:
                available_languages[language['name']] += 1
                
    return max(available_languages, key=available_languages.get)
    
