import csv
import uuid
import random 
import csv
from typing import TextIO

globalContentBlockDict = {} #Key: ContentBlock ID. Value: ContentBlock object
globalFlashcardIDList = []
lastUsedIndexPos = 0


class ContentBlock:
	def __init__(self, prompt: str):
		self.id = str(uuid.uuid4())
		self.prompt = prompt

class Flashcard(ContentBlock):
	def __init__(self, prompt: str, answer: str):
		super().__init__(prompt)
		self.answer = answer

class ChooseCorrectOption(ContentBlock):
	def __init__(self, prompt: str, options: list):
		super().__init__(prompt)
		random.shuffle(options)
		self.answer = options


def extract_info_from_CSV(file: str):
	with open(file, 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			word, desc = row
			make_flashcard(word, desc)
		

def write_to_CSV(file: str, newWord: str, newDesc: str):
	with open(file, 'a', newline='') as write_file:
		csv.writer(write_file).writerow((newWord, newDesc))



def make_flashcard(prompt: str, desc: str) -> None:
	global globalContentBlockDict
	global globalFlashcardIDList
	newlyAdded = Flashcard(prompt, desc)
	globalContentBlockDict[newlyAdded.id] = newlyAdded
	globalFlashcardIDList.append(newlyAdded.id)
	print(f"ID: {newlyAdded.id} | prompt: {newlyAdded.prompt} | answer: {newlyAdded.answer}")

def get_random_flashcard() -> Flashcard:
	global lastUsedIndexPos
	[print(globalContentBlockDict[f].prompt) for f in globalFlashcardIDList]
	if lastUsedIndexPos == len(globalFlashcardIDList):
		return "ALL FLASHCARDS VISITED"
	contentBlockID = globalFlashcardIDList[lastUsedIndexPos]
	lastUsedIndexPos += 1
	return globalContentBlockDict[contentBlockID]

def start_learn():
	global lastUsedIndexPos
	lastUsedIndexPos = 0
	random.shuffle(globalFlashcardIDList)

def start_test():
	pass

# TODO: reset_learn, build out methods for learn -> make, get, reset
	

def validate_user_response(flashcardID: str, userResponse: str) -> bool:
	try:
		return globalContentBlockDict[flashcardID].answer == userResponse
	except KeyError:
		return False



if __name__ == '__main__':
	extract_info_from_CSV('read.csv')
	start_learn()