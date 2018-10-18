"""
This program generates passages that are generated in mad-lib format
Author: Katherin and Wesley
"""

# The template for the story

STORY = "This morning %s \
woke up feeling %s. \
'It is going to be a %s \
day!' Outside, a bunch of %s \
were protesting to keep %s \
in stores. They began to %s \
to the rhythm of the %s, \
which made all the %s \
very %s. \
Concerned, %s \
texted %s, \
who flew %s \
to %s \
and dropped %s \
in a puddle of frozen %s. \
%s \
woke up in the year %s, \
in a world where %s \
ruled the world."

print("Mad Libs has started. Prepare for hilarity.")

name = raw_input("Enter a name:")

adjective_one = raw_input("Enter an adjective:")
adjective_two = raw_input("Enter another adjective:")
adjective_three = raw_input("Enter one more adjective:")

verb = raw_input("Enter a verb:")

noun_one = raw_input("Enter a plural noun:")
noun_two = raw_input("Enter another plural noun:")

animal = raw_input("Now tell me your favorite animal:")
food = raw_input("Now tell me your least favorite food:")
fruit = raw_input("What about the smelliest fruit:")
superhero = raw_input("And the most perplexing superhero:")
country = raw_input("Name a country you've never been to:")
dessert = raw_input("What's your favorite dessert:")
year = raw_input("What is the first year you remember:")

print STORY % (name, \
	adjective_one, \
	adjective_two, \
	animal, \
	food, \
	verb, \
	noun_one, \
	fruit, \
	adjective_three, \
	name, \
	superhero, \
	name, \
	country, \
	name, \
	dessert, \
	name, \
	year, \
	noun_two)