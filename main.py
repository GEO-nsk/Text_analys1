"""
Egor Gagol - 60
Evgeny Tarlo  - 55
Nikolay Karpenko - 20
"""

from textblob import TextBlob
from deep_translator import GoogleTranslator


Text = str(input())
space = ' '
syllable = 0

Text_en = GoogleTranslator(source='auto', target='en').translate(Text)

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

if PRE_rus > 80:
    Difficulty_level = 'The text is easy to read (for younger students)'
elif 80 >= PRE_rus > 50:
    Difficulty_level = 'Simple text (for schoolchildren)'
elif 50 >= PRE_rus > 25:
    Difficulty_level = 'The text is a little hard to read (for students)'
else:
    Difficulty_level = 'Hard to read (for university graduates)'

text_pol = TextBlob(Text_en).polarity

if 1 >= text_pol > 0.1:
    text_tone = 'Positive'
elif 0.1 >= text_pol >= -0.1:
    text_tone = 'Neutral'
else:
    text_tone = 'Negative'

print('Sentences:', sentences)
print('Words:', Words)
print('Syllable:', syllable)
print('Length of sentence:', length_of_sentence)
print('Length of syllable:', length_of_syllable)
print('Flash index:', PRE_rus)
print('Difficulty level:', Difficulty_level)
print('Text tone:', text_tone)
print('Subjectivity: ', TextBlob(Text_en).subjectivity * 100, '%', sep='')
