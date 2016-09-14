# IPND Stage 2 Final Project

#########################################
#										#
#		Quiz about famous people		#
#		Andreas Landgraf   				#
#########################################

#	Section 1: Provide the text for the fill-in-the-blank quiz
#
#	Write the word where the blank should be like this: []Bach[] (this is called a blankword)

########################################
# The first text is about composers.   #
# Bach | Mozart | Beethoven | Wagner   #
########################################

text_1 = '''
The first quiz is about composers:

Johann Sebastian []Bach[] (31 March 1685 - 28 July 1750) was a German composer of the Baroque period.
Wolfgang Amadeus []Mozart[] was born in Salzburg and a influential composer of the Classical era.
Ludwig van []Beethoven[] (17 December 1770 - 26 March 1827) has composed nine symphonies and five piano concertos.
Richard []Wagner[] (22 May 1813 - 13 February 1883) is known for his operas like The Flying Dutchman or Lohengrin.
'''

# Informations from:
# https://en.wikipedia.org/wiki/Johann_Sebastian_Bach
# https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart
# https://en.wikipedia.org/wiki/Ludwig_van_Beethoven
# https://en.wikipedia.org/wiki/Richard_Wagner


#######################################
# The second text is about artists.   #
# Klimt | Munch | Picasso | Pollock   #
#######################################

text_2 = '''
The second quiz is about artists:

Gustav []Klimt[] (14 July 1862 - 6 February 1918) was an Austrian symbolist painter 
and one of the most prominent members of the Vienna Secession movement.
Edvard []Munch[] (12 December 1863 - 23 January 1944) was a Norwegian painter.
One of his most well-known works is The Scream of 1893. 
Pablo []Picasso[] (25 October 1881 - 8 April 1973) was a Spanish painter. 
He is known for co-founding the Cubist movement. 
Paul Jackson []Pollock[] (28 January 1912 - 11 August 1956) was an influential American painter 
and a major figure in the abstract expressionist movement. 
He is famous for his unique style of drip painting.
'''

 # Informations from:
 # https://en.wikipedia.org/wiki/Gustav_Klimt
 # https://en.wikipedia.org/wiki/Edvard_Munch
 # https://en.wikipedia.org/wiki/Pablo_Picasso
 # https://en.wikipedia.org/wiki/Jackson_Pollock


##########################################################################################
#                         The third text is about emperors.                              #
#  Alexander the Great | Qin Shi Huang | Gaius Julius Caesar | Suleiman the Magnificent  #
##########################################################################################

text_3 = '''
The third quiz is about emperors:

[]Alexander[] the Great, was a King of the Ancient Greek kingdom of Macedon.
By the age of thirty he had created one of the largest empires of the ancient world. 
[]Qin[] Shi Huang was the first emperor of China.
Julius []Caesar[] was a Roman politician and general. 
He is considered by many historians to be one of the greatest military commanders in history. 
[]Suleiman[] the Magnificent was a Great Sultan of the Ottoman Empire.
'''

# Informations from:
# https://en.wikipedia.org/wiki/Alexander_the_Great
# https://en.wikipedia.org/wiki/Qin_Shi_Huang
# https://en.wikipedia.org/wiki/Julius_Caesar
# https://en.wikipedia.org/wiki/Suleiman_the_Magnificent


###############################################
# The fourth text is about philosophers.      #
# Socrates | Plato | Aristotle | John Locke   #
###############################################

text_4 = ''' 
The fourth quiz is about philosophers:

[]Socrates[] was a classical Greek philosopher credited as one of the founders of Western philosophy. 
One of his students was []Plato[]. []Plato[] was the teacher of []Aristotle[]. 
[]Aristotle[] was the teacher of a famous emperor from the last quiz. 
John []Locke[] (29 August 1632 - 28 October 1704) was an English philosopher. 
He is regarded as one of the most influential of Enlightenment thinkers and commonly known as the Father of Liberalism.
'''

# Informations from:
# https://en.wikipedia.org/wiki/Socrates
# https://en.wikipedia.org/wiki/Plato
# https://en.wikipedia.org/wiki/Aristotle
# https://en.wikipedia.org/wiki/John_Locke

text_collection = [text_1.split(), text_2.split(), text_3.split(), text_4.split()]



def set_lives():
	lives = raw_input("How many lives do you like to have? ")
	if lives.isdigit():
		return int(lives)
	else:
		set_lives()


def set_difficulty_level():
	level = []
	user_input = raw_input("What difficulty level would you like to play? Choose easy, medium or hard: ")
	if user_input in ["easy", "medium", "hard"]:
		return user_input
	else:
		return set_difficulty_level()

def is_blankword(word):
	if len(word) > 4:
		if word[-1] not in  [".", "!", "?", ":", ";", ","]:
			if word[0] == word[-2] == "[" and word[1] == word[-1] == "]" :
				return True
	 		else:
	  			return False
	  	else:
	  		if word[0] == word[-3] == "[" and word[1] == word[-2] == "]" :
				return True
	 		else:
	  			return False

def positions(text):
	pos = []
	i = 0
	while i < len(text):
		if is_blankword(text[i]):
			pos.append(i)
		i += 1
	return pos

def solutions(text):
	pos = positions(text)
	sol = []
	for num in pos:
		if text[num][-1] in [".", "!", "?", ":", ";", ","]:
			sol.append(text[num][2:-3])
		else:	
			sol.append(text[num][2:-2])
	return sol

def numbering(text):
	numb = [1]
	pos = positions(text)
	i = 0
	num = 1
	while i < len(pos)-1:
		if text[pos[i+1]] in text[pos[i]] or text[pos[i]] in text[pos[i+1]]:
			numb.append(num)
		else:
			num += 1
			numb.append(num)
		i += 1
	return numb

def blanks(text, difficulty_level):
	pos = positions(text)
	numbs = numbering(text)
	sol = solutions(text)
	blank = []
	index = 0
	if difficulty_level == "hard":
		for place in numbs:
			blank.append("___" + str(place) + "___")
	if difficulty_level == "medium":
		for place in numbs:
			blank.append( sol[index][0] + "__" + str(place) + "___")
			index +=1
	if difficulty_level == "easy":
		for place in numbs:
			blank.append( sol[index][0] + "__" + str(place) + "__" + sol[index][-1])
			index += 1
	return blank

def create_text(text, fillins):
	pos = positions(text)
	sol = solutions(text)
	j = 0
	k = 0
	while j < len(text):
		if j in pos:
			text[j] = text[j].replace("[]" + sol[k] + "[]", fillins[k])
			k += 1
		j += 1

	return " ".join(text)


###########################
# The Code for the Quiz   #
###########################



# print '''
# Welcome to a quiz about famous persons!

# Please fill in the blanks.
# In easy mode you will get the first and last letter of the name.
# In medium mode you will get only the first letter and in hard mode you will get none.  
# '''

# lives = set_lives()

# death = 0

difficulty_level = "hard"

quiz_num = 0

text = text_collection[quiz_num]
fillins = blanks(text, difficulty_level)
sol = solutions(text)


print create_text(text, sol)


print create_text(text, fillins)



