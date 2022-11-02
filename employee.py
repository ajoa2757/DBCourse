# -*- coding: utf-8 -*-
"""employee.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jhxav5ukDvErcFdnkZ4XkK6PZ8mlzgdp
"""

class Employee:
  """A sample Employee class"""

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  def fullname(self):
    return'{} {}'.format(self.first, self.last)

  def __repr__(self):
    return "Employee('{}', '{}', {})".format(self.first, self.last, self.play)