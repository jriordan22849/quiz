from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Quiz(models.Model):
	class Meta:
		verbose_name = "quiz"
		verbose_name_plural = "quiz"

	name = models.CharField(
		max_length=100,
		blank=False,
		verbose_name="name"
	)
	
	quixID = models.IntegerField( unique = '1')
	created = models.DateTimeField(
		auto_now_add=True
	)
	modified = models.DateTimeField(
		auto_now=True
	)
	# objects = models.Manager()

	def __str__(self):
		return "Quiz name: {}".format(self.name)
		

class Question(models.Model):
	class Meta:
		verbose_name = "question for quiz"

	quizBelongTo = models.ForeignKey(
		Quiz,
		verbose_name="quizBelongTo",
		on_delete=models.CASCADE
	)
	
	questionNumber = models.IntegerField( default = '1')
	questionText = models.CharField(max_length = 250, default = "question")

	created = models.DateTimeField(
		auto_now_add=True
	)
	modified = models.DateTimeField(
		auto_now=True
	)

	# objects = models.Manager()]
	def __str__(self):
		return "{} Question {}: {} ".format(self.quizBelongTo, self.questionNumber,self.questionText)

class Option(models.Model):
	class Meta:
		verbose_name = "answer"

	option = models.ForeignKey(
		Question,
		verbose_name="optionForQuestion",
		on_delete=models.CASCADE
	)
	
	optionNumber = models.IntegerField( default = '1')
	optionText = models.CharField(max_length = 250, default = "answer")
	rightAnswer = models.BooleanField(default=False)

	created = models.DateTimeField(
		auto_now_add=True
	)
	modified = models.DateTimeField(
		auto_now=True
	)

	def __str__(self):
		return "Question {}: Option: {} Text: {}  Correct: {}".format(self.option, self.optionNumber,self.optionText,self.rightAnswer)
	# objects = models.Manager()