# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hm9af_5nCQz7HGoutv5B-0L0cKQ-XqdG
"""

def add(a,b):
  print (a+b)

def sub(a,b):
  print (a-b)

def mul(a,b):
  print (a*b)

def div(a,b):
  print (a/b)

def mod(a,b):
  print(a%b)

a=float(input("enter the first no:"))
b=float(input("enter the second no:"))
op=input("enter the operator:")

if (op=="+"):
  sum (a,b)
elif (op=="-"):
  sub (a,b)
elif (op=="*"):
  mul (a,b)
elif (op=="/"):
  div (a,b)
else:
  print("invalid op")