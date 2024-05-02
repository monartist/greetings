from greet import greetings
from translate import Translator

translator = Translator(to_lang='fa')
for g in greetings:
    print(translator.translate(g).title())