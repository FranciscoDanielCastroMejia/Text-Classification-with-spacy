# Text-Classification-with-spacy
In this program you will be able to separate the text in the part of the speech that you want. The program is made in the way that you call the function and enter the text that you want to divide, and the the prgram return a diccionary with your part of the speech.
---
## Requirements 

I recomend to install the following libraries in the following order:
- python = 3.9
- conda install spacy-model-en_core_web_sm

---
## Code
### Importing libraries 
```python
import spacy
```
### Load the model 
Load a pre-trained natural language processing (NLP) model using the spaCy library in Python.
```python
nlp = spacy.load("en_core_web_sm")
```
"en_core_web_sm": This is the name of the specific pre-trained model. You can use different models like "es_core_news_sm" to work with spanish, "fr_core_news_sm" to french, etc. 

### Principal function
```python
def text_classification(Text):

    
    #Creating the dictionary that will return the function
    POS = {
        "ADJ": [],
        "NOUN" : [],
        "VERB" : [],
        "ADV" : [],
        "PROPN" : []
    }

    docs = nlp(Text) #Here we make the text clasification

    #Here we fill the dictionary with the part of the speech we want
    for word in docs:
        if word.pos_ == "ADJ":
            #It will be checked if the word has already been added, to avoid it being repeated.
            if(word.text not in POS["ADJ"]): #If the word is not added, we add the word to teh dictionary
                POS["ADJ"].append(word.text)
            else:#If the word was already there, nothing is done
                continue
    #If the word is a Noun or proper Noun and we find that is in plural we add to the dictionary its base form an its plural form
        elif word.pos_ == "NOUN":
            if(word.text not in POS["NOUN"]): 
                POS["NOUN"].append(word.text)
                #We check if the word is plural, if it is
                #we convert it to its base form and add it to the dictionary.
                if word.tag_[-1] == "S": #This indicates that if the word is plural it approves the condition.
                    aux = word.lemma_ #transform the word to its base form
                    POS["NOUN"].append(aux)#we save the word in its base form
                else:
                    continue
            else:
                continue
        
        elif word.pos_ == "VERB":
            if(word.text not in POS["VERB"]): 
                POS["VERB"].append(word.text)
            else:
                continue

        elif word.pos_ == "ADV":
            if(word.text not in POS["ADV"]): 
                POS["ADV"].append(word.text)
            else:
                continue
        
        elif word.pos_ == "PROPN":
            if(word.text not in POS["PROPN"]): 
                POS["PROPN"].append(word.text)
                if word.tag_[-1] == "S":
                    aux = word.lemma_
                    POS["PROPN"].append(aux)
                else:
                    continue
            else:
                continue
                 
    return(POS)
```

### Testing
```python
if __name__=='__main__':
    
    text = "Natural Language Processing (NLP) is a branch of AI that enables computers to understand, interpret, and generate human language. It's used in applications like chatbots, translation, and sentiment analysis to make machines interact with language more naturally."
    Part_of_the_speech = text_classification(text)
    print(Part_of_the_speech)
```
---
### Result
- ADJ: human
- NOUN: branch, computers, computer, language, applications, application, chatbots, chatbot, translation, analysis, machines, machine
- VERB: enables, understand, interpret, generate, used, sentiment, make, interact
- ADV: more, naturally
- PROPN: Natural, Language, Processing, NLP, AI
