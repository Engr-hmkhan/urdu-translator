from translate import Translator

word = input("Enter words or sentence to translate: ")
translator = Translator(to_lang='ur')

print(translator.translate(word).title())

#done