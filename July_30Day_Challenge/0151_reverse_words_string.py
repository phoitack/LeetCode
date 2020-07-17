# Given an input string, reverse the string word by word.


def reverseWords(s:str):

	s = s.strip().split()

	s = ' '.join(reversed(s))

	return(s)



word = 'a good   example'
word = 'hello world!'

reverseWords(word)