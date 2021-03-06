#Examination System

import random

def prepareData(line):
	#line = 'This is question1;AAAA,BBBB,CCCC;BBBB;1'
	ls = line.split(';')
	#empty dictionary
	unit = {}
	unit['question'] = ls[0]
	unit['options'] = ls[1].split(',')
	unit['correctAnswer'] = ls[2]
	unit['marks'] = ls[3]
	return unit


def loadQuestionSet(fileName):
	fh = open(fileName,'r')
	easy = []
	moderate = []
	difficult = []
	for x in fh:
		unit = prepareData(x.strip())
		if unit['marks'] == '1':
			easy.append(unit)
		elif unit['marks'] == '2':
			moderate.append(unit)
		elif unit['marks'] == '3':
			difficult.append(unit)
	fh.close()
	return [easy, moderate, difficult]

def getQuestionPaper(qSet , count= 5):
	maxQ = len(qSet[0]) + len(qSet[1]) + len(qSet[2])

	if count > maxQ:
		print('Max count can be : ', maxQ )
		return

	qPaper = []
	i = 1
	easy = qSet[0]
	moderate = qSet[1]
	difficult = qSet[2]

	random.shuffle(easy)
	random.shuffle(moderate)
	random.shuffle(difficult)

	while i <= count:
		if i %3 == 1:
			#fetch a random unit from easy
			temp = random.choice(easy)
		elif i % 3 == 2:
			# fetch a random unit from moderate
			temp = random.choice(moderate)
		elif i % 3 == 0:
			# fetch a random unit from difficult
			temp = random.choice(difficult)

		if temp not in qPaper:
			qPaper.append(temp)
			i += 1

	return qPaper

def attemptTest(qPaper):
	print('Welcome to Abstract Tests')
	score = 0
	total = 0
	for unit in qPaper:
		print('Q)', unit['question'])
		for i in range(len(unit['options'])):
			print(i+1, unit['options'][i])

		while True:
			ans = int(input('Enter Answer '))
			if ans >=1 and ans <= len(unit['options']):
				break
			else:
				print('Wrong Choice')

		if unit['correctAnswer'] == unit['options'][ans-1]:
			score += int(unit['marks'])

		total+=int(unit['marks'])

	print('Score : ', score ,'/', total)

qSet = loadQuestionSet('d:/test_questions.txt')
qPaper = getQuestionPaper(qSet, 6)
attemptTest(qPaper)

