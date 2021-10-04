#!/usr/bin/python3

'''
Docstring goes here

'''


def text_indentation(text):
    ''' text_indent'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new_str = ''
    i = 0
    while i < len(text):
        new_str += text[i]
        if text[i] in ['.', '?', ':']:
            new_str = new_str.strip()
            print(new_str)
            try:
                if text[i + 1] == ' ':
                    i += 1
            except IndexError:
                pass
            new_str = ''
        i += 1

    if len(new_str) > 0:
        print(new_str, end='')


if __name__ == '__main__':
    text_indentation = __import__('5-text_indentation').text_indentation

    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? 
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: 
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")

    print(f'\n==========')

    text_indentation("Lorem amet? consectetur adipiscing elit. Quonam: modo")
    print(f'\n==========')
    text_indentation("text sans characters")
    print(f'\n==========')
    text_indentation("")
    print(f'\n==========')
    text_indentation("test.com")
    print(f'\n==========')
    text_indentation("test_text.")
    print(f'\n==========')
    text_indentation("Como estas? J'n'pas rien: Schadenfreude")
    print(f'\n==========')
