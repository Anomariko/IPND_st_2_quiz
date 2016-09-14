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

text_collection = [text_1, text_2, text_3, text_4]

#	Section 2: Some usefull function
#
#	

def set_lives():
	lives = raw_input("How many lives do you like to have? ")
	if lives.isdigit():
		return int(lives)
	else:
		set_lives()

# output: array with integers | function: user can decide what difficulty level he like to play
def set_difficulty_level():
	level = []
	user_input = raw_input("What difficulty level would you like to play? Choose easy, medium or hard: ")
	if user_input == "easy":
		level = [1,2]
	else:
		if user_input == "medium":
			level = [1,0]
		else:
			if user_input == "hard":
				level = [0,0]
			else:
				return set_difficulty_level()

	return level

# input: string | output: bool | function: decides if a word is a blankword (line 11)
def is_blankword(word):
	if len(word) > 4:
		if word[0] == word[-2] == "[" and word[1] == word[-1] == "]":
			return True
 		else:
  			return False
  	else:
  		return False
# input: string | output: array with strings | function: finds all blankwords in a text and creates an array with them
def blankwords(text):
	blankwords = []
	text = text.split()
	for word in text:
		if is_blankword(word):
			new_blankword = True
			for blankword in blankwords:
				if blankword == word:
					new_blankword = False
			if new_blankword:
				blankwords.append(word)
	return blankwords

# input: string, array | output: array with strings for the replacement of the blankword
def for_blankword(word, blankwords):
    i = 0
    while i < len(blankwords):
        if blankwords[i] in word:
            return [blankwords[i], "(" + str(i + 1) + ")", "_", blankwords[i][2], blankwords[i][-3]]
     	else:
     		i += 1
    return None

# input: string, array | output: string | function: replaces the blankwords with words without the []...[], creates the solution
def create_solution(text, blankwords):
	solution = []
	text = text.split()
	for word in text:
		replacement = for_blankword(word, blankwords)
		if replacement != None:
			word = word.replace(replacement[0],  replacement[0][2:-2])
			solution.append(word)
		else:
			solution.append(word)
	solution = " ".join(solution)
	return solution

# input: string. array, array | output: string | creates a quiz with ___(1)____ instead of []Bach[]
def create_quiz(text, difficulty_level, blankwords):
	a = difficulty_level[0]
	b = difficulty_level[1]

	quiz = []
	text = text.split()
	for word in text:
		replacement = for_blankword(word, blankwords)
		if replacement != None:
			word = word.replace(replacement[0],  replacement[2+a]+ "_" + replacement[1] + "_" + replacement[2+b])
			quiz.append(word)
		else:
			quiz.append(word)
	quiz = " ".join(quiz)
	return quiz

# input: string. array, array | output: string | asks the player for the answer
def answer(text, difficulty_level, blankwords):
	a = difficulty_level[0]
	b = difficulty_level[1]

	replaced = []
	text = text.split()
	for word in text:
		replacement = for_blankword(word, blankwords)
		if replacement != None:
			user_input = raw_input("Type in  " + replacement[2+a]+ "_" + replacement[1] + "_" + replacement[2+b] + ": ")
			word = word.replace(replacement[0], user_input)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced


###########################
# The Code for the Quiz   #
###########################



print '''
Welcome to a quiz about famous persons!

Please fill in the blanks.
In easy mode you will get the first and last letter of the name.
In medium mode you will get only the first letter and in hard mode you will get none.  
'''

lives = set_lives()

death = 0

difficulty_level = set_difficulty_level()

i = 0
solution_collection = ["","","",""]
quiz_collection = ["","","",""]
answer_collection = ["","","",""]

while i < len(text_collection) and death < lives:
	text = text_collection[i]
	blankwords_liste = blankwords(text)
	solution_collection[i] = create_solution(text, blankwords_liste)
	quiz_collection[i] = create_quiz(text, difficulty_level, blankwords_liste)
	print ""
	print quiz_collection[i]
	print ""
	answer_collection[i] = answer(text, difficulty_level, blankwords_liste)
	if answer_collection[i] == solution_collection[i]:
		i += 1
		print ""
		print "Nice! All answers were right."
		if i == 4:
			print ""
			print "Awesome!! You answered all questions correct." 
	else: 
		death += 1
		print ""
		print "Please try again!"
		print ""

print '''

Thank you for playing!!
Bye, Bye!!
'''


