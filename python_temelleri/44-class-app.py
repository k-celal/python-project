class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def check_answer(self,answer):
        return self.answer==answer
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+1} : {question.text}')
        for q in question.choices:
            print("-" + q)
        answer=input("Cevap : ")
        self.guess(answer)
        self.loadQuestion()
    def guess(self, answer):
        question = self.getQuestion()

        if question.check_answer(answer):
            self.score += 1
        self.questionIndex += 1
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            print("Quiz bitti")
            self.showScore()
        else:         
            self.displayProgress()  
            self.displayQuestion()
    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))        
        
        
        
question1=Question("En iyi takım hangisi",["Fenerbahçe","Trabzonspor","Galatasaray","Niğdespor"],"Niğdespor")
question2=Question("En iyi programlama dili",["Python","C","Go","Java"],"Python")
question3=Question("En güzel ülke",["Türkiye","Alamanya","Fransa","İspanya"],"Türkiye")
question4=Question("En çok kazandıran dil",["Python","C","Go","Java"],"Java")

questions=[question1,question2,question3,question4]

quiz=Quiz(questions)
quiz.loadQuestion()


        