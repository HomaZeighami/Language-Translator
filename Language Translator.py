from googletrans import Translator
translator = Translator()
text = "I love Python."
output = translator.translate(text, dest="fr")
print(output) 
