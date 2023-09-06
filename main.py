"""
У нас росал липа. Липа стала стара. Липа стала суха. Липа упала. Пришли папа и паша. У папы пила. У паши топорик.
"""



space = ' '
syllable = 0
Text = str(input())

Dots = Text.count('.')
Questions = Text.count('?')
Exclamation = Text.count('!')

sentences = Dots + Questions + Exclamation

Words = len(Text.split())

for i in Text:
    if i == 'а' or i == 'е' or i == 'ё' or i == 'и' or i == 'о' or i == 'у' or i == 'э' or i == 'ы' or i == 'я' or i == 'ю':
        syllable += 1
print(sentences, Words, syllable)
