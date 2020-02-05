# 1. TASK: print "Hello World"
x="Hello World!"
print( x )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello %s" %(name) )	# with a comma
# fine, here is your silly comma one!
print("Hello", name, "!")
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( x, f"the number you are looking for is {name}" )	# with a comma
print( "the number that you are looking for is ", name )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} not {}!".format(fave_food2, fave_food1) ) # with .format()
print( f"My favorite food is {fave_food2}, not {fave_food1}!" ) # with an f string
