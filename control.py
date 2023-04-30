import flashcards as flashcards
import random

def startQuiz(answer: str, correct: str, score: int):
    #take in user selected answer, and correct answer
    #return true or false based on answer
    choices = []
    playerChoice = -1
    
def startLearn():
    #generate a word with definition and show to the user
    flashcard = flashcards.get_random_flashcard()
    showCard = flashcard.prompt
    

    
def resetVariables(choices: list[str], playerChoice: int):
    choices = []
    playerChoice = -1
    
def newCard(flashcard: Flashcard):
    #Get a random flashcard and return the tuple (prompt, answer)
    return (flashcard.prompt, flashcard.answer)
    
def newQuestion():
    #Return 2 element list with first index as (question, correct answer) and second element as list of 4 options
    flashcard = flashcards.get_random_flashcard()
    questions = [(flashcard.prompt, flashcard.answer), [flashcard.answer]]

    used_indexes = []
    for x in range(1,4):
        rand = random.randint(0,len(flashcards.globalFlashcardIDList))
        while(rand in used_indexes):
            rand = random.randint(0,len(flashcards.globalFlashcardIDList))
        used_indexes.append(rand)
        id = flashcards.globalFlashcardIDList[rand]
        newFlash = flashcards.globalContentBlockDict[id]
        questions[1].append(newFlash.answer)
    random.shuffle(questions[1])
    return questions
    