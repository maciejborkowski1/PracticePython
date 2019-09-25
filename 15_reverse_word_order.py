'''
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

def reverseWordOrder(text='This is sample text'):
    text='This is sample text'
    separate = text.split(' ')
    separate.reverse()
    separate = ' '.join(separate)
    return separate

