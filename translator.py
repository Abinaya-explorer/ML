# pip install googletrans==4.0.0-rc1
from googletrans import Translator
translator = Translator()
sentence = "Hello, how are you?"
# Change the language code in this line
translate_text = translator.translate(sentence, dest='ta') # ta for tamil
print(translate_text.text)
