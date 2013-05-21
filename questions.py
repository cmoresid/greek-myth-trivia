import json
import random

class QuestionSet(object):
	def __init__(self, qs_size, jsonfile):
		# Number of questions in QuestionSet
		self.qs_size = qs_size
		# Load Question JSON file
		self.jsonfile = jsonfile
		self.js_questions = self.get_json_questions()
		# Convert from JSON to Question representation
		self.questions = self.question_from_json()
		# Current question index
		self.index = -1
	
	def question_from_json(self):
		question_list = []
		
		for js_question in self.js_questions:
			question = Question()
			question.id = js_question["id"]
			question.question_str = js_question["question_str"]
			question.responses = js_question["responses"]
			question.score = js_question["score"]
			question.correct_response = js_question["correct_response"]
			question.description = js_question["description"]
			# shuffle responses
			random.shuffle(question.responses)
			
			question_list.append(question)
			
		return question_list
	
	def get_json_questions(self):
		f = open(self.jsonfile)
		js = json.load(f)
		js_questions_list = js["questions"]
		random.shuffle(js_questions_list)
		js_questions_list = js_questions_list[:self.qs_size]
		
		return js_questions_list
		
	def next_question(self):
		self.index = self.index + 1
		
		if (self.index == len(self.questions)):
			return None
		else:
			return self.questions[self.index]
		
		
class Question(object):
	def __init__(self):
		self.id = 0
		self.score = 0
		self.question_str = []
		self.responses = {}
		self.correct_response = ""
		self.description = []
		