# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:27:27 2021

@author: https://learning.oreilly.com/library/view/effective-python-90/9780134854717/ch05.xhtml#item37
"""

class SimpleGradebook:
  def __init__(self):
        self._grades = {}

  def add_student(self, name):
      self._grades[name] = []

  def report_grade(self, name, score):
      self._grades[name].append(score)

  def average_grade(self, name):
      grades = self._grades[name]
      return sum(grades) / len(grades)
  
book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)

print(book.average_grade('Isaac Newton'))


#%%
from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}                     # Outer dict
    def add_student(self, name):
       self._grades[name] = defaultdict(list) # Inner dict
       
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count
    
book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))    
