# -*- coding: utf-8 -*-

from languages import LANGUAGES

def detect_language(text, languages):
    available_languages = {'English': 0, 'Spanish': 0, 'German': 0}

    for word in text.split(' '):
        for language in languages:
            if word in language['common_words']:
                available_languages[language['name']] += 1
                
   # return max([i for i in available_languages.values()])
    return max(available_languages, key=available_languages.get)
    
text = """
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.
        """
    
    

print(detect_language(text, LANGUAGES))