"""
У нас росла липа. Липа стала стара. Липа стала суха. Липа упала. Пришли папа и паша. У папы пила. У паши топорик. Они распилили липу.
"""

from textblob import TextBlob

space = ' '
syllable = 0
Text = 'У нас росла липа. Липа стала стара. Липа стала суха. Липа упала. Пришли папа и паша. У папы пила. У паши топорик. Они распилили липу.'

Dots = Text.count('.')
Questions = Text.count('?')
Exclamation = Text.count('!')

sentences = Dots + Questions + Exclamation

Words = len(Text.split())

Text = Text.lower()

for i in Text:
    if i == 'а' or i == 'е' or i == 'ё' or i == 'и' or i == 'о' or i == 'у' or i == 'э' or i == 'ы' or i == 'я' or i == 'ю':
        syllable += 1

length_of_sentence = Words/sentences

length_of_syllable = syllable/Words

PRE_rus = 206.835 - 1.3*(Words/sentences) - 60.1*(syllable/Words)
PRE_eng = 206.835 - 1.015*(Words/sentences) - 84.6*(syllable/Words)
print(sentences, Words, syllable, length_of_sentence, length_of_syllable, PRE_rus)

