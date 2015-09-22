# -*- coding: utf-8 -*-

name  = 'Lars Böhnke'
age = 24 # not a lie
height = 1.80 # meter
weight = 80.0 #kilogramm
eyes = 'green-grey'
teeth = 'white'
hair = 'black'

print "Let's talk about %s." % name
print "He's %s years old." % age
print "He's %s kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are normally %s depending on the coffee." % teeth

#now comes a tricky line!
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)