import csv,random
from datetime import datetime

def create_new_quiz(qName):
	f=open("{}.csv".format(qName),'w')
	f.close()
	__main__()



def add_new_questions(qName):
	f=open("{}.csv".format(qName),'a')
	while(1):
		question=input("Please enter a question or key term, or exit to quit: ")
		answer=input("Please enter an answer: ")
		if(question=='exit'):
			f.close()
			__main__()
		else:
			string=question+","+answer+"\n"
			f.write(string)


def test(qName):
	with open("{}.csv".format(qName),'r') as testcsv:
		f=csv.reader(testcsv)
		i=random.choice(list(f))
		print(i[0])
		usersAns=input("> ")
		if usersAns==i[1]:
			print("Correct! Well done")
		else:
			print("Wrong. The correct answer is: ",i[1])



def __main__():
	choice=input("Would you like to create a new quiz, add questions to an existing quiz, or test yourself. (1/2/3/4 to quit)")

	if choice == '1':
		quizName=input("Please enter a name for the quiz: ")
		create_new_quiz(quizName)
		add_new_questions(quizName)

	elif choice == '2':
		quizName=input("Please enter a name for the quiz you would like to add to: ")
		add_new_questions(quizName)


	elif choice == '3':
		quizName=input("Please enter a name for the quiz you would like to test")
		while(1):
			choice = input("Would you like a new question? y/n > ")
			if choice == 'y':
				random.seed(datetime.now())
				test(quizName)
			else:
				break

	else:
		print("Error Please try again")


if __name__ == '__main__':
	__main__()
