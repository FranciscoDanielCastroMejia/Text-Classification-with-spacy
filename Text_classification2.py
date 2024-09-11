import os
import spacy 



#Part of the speech

nlp = spacy.load("en_core_web_sm")

 # load en_core_web_sm of English for vocabluary, syntax & entities
def text_classification(Text):

    
    #crearemos un diccionario con los elementos qeu necesitamos

    #diccionario Part of speech
    POS = {
        "ADJ": [],
        "NOUN" : [],
        "VERB" : [],
        "ADV" : [],
        "PROPN" : []
    }

    docs = nlp(Text) #Se hace la clasificacion del texto qeu ingresamos
   
    for word in docs:
        if word.pos_ == "ADJ":
            #se verificará si la palabra ya fue agregada, para evitar que se repita
            if(word.text not in POS["ADJ"]): #si la palabra no está se agrega
                POS["ADJ"].append(word.text)
            else:#si la palabra ya estaba, no se hace nada
                continue
 
        elif word.pos_ == "NOUN":
            if(word.text not in POS["NOUN"]): #si la palabra no está se agrega
                POS["NOUN"].append(word.text)
                #verificamos si la palabra esta en plural, si lo esta
                #la pasamos a su forma base y al agregamos al diccionario
                if word.tag_[-1] == "S": #esto indica que si la palabra esta en plura entra
                    aux = word.lemma_ #aqui buscamos la palabra en su forma base
                    POS["NOUN"].append(aux)#guardamos la palabra en su forma base
                else:
                    continue
            else:#si la palabra ya estaba, no se hace nada
                continue
        
        elif word.pos_ == "VERB":
            if(word.text not in POS["VERB"]): #si la palabra no está se agrega
                POS["VERB"].append(word.text)
            else:#si la palabra ya estaba, no se hace nada
                continue

        elif word.pos_ == "ADV":
            if(word.text not in POS["ADV"]): #si la palabra no está se agrega
                POS["ADV"].append(word.text)
            else:#si la palabra ya estaba, no se hace nada
                continue
        
        elif word.pos_ == "PROPN":
            if(word.text not in POS["PROPN"]): #si la palabra no está se agrega
                POS["PROPN"].append(word.text)
                if word.tag_[-1] == "S":
                    aux = word.lemma_
                    POS["PROPN"].append(aux)
                else:
                    continue
            else:#si la palabra ya estaba, no se hace nada
                continue
                 
    return(POS)

if __name__=='__main__':
    
    text = "Natural Language Processing (NLP) is a branch of AI that enables computers to understand, interpret, and generate human language. It's used in applications like chatbots, translation, and sentiment analysis to make machines interact with language more naturally."
    Part_of_the_speech = text_classification(text)
    print(Part_of_the_speech)