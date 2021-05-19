corpus =  """
Doubt thou the stars are fire
Doubt that the sun doth move
Doubt truth to be a liar
But never doubt I love.
"""
print(corpus)
subtext = input("Please enter the subtext to learn frequency of it in the text given: ")
#taking the subtext from the user
corpus = corpus.lower() 
subtext = subtext.lower()
#we need to convert the text and the subtext to lower case to prevent problems with the user's input with upper case

frequency = corpus.count(subtext)
#finding the occureance of subtext by count method and keep them in a variable as frequency
print(f"{subtext} occurs in the text {frequency} times.")
