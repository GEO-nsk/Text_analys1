"""
"""
space = ' '
Text = str(input())

Dots = Text.count('.')
Questions = Text.count('?')
Exclamation = Text.count('!')

sentences = Dots + Questions + Exclamation

for i in range(0,len(Text)):
    if i == space and i+1 == space:
        Text.pop(i+1)
print(Text)
print(sentences)
