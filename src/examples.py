from grammar import LSystemGrammar

def algae_growth_example():
	alphabet=['A', 'B']
	constants=[]
	rules={'A':'AB', 'B':'A'}

	grammar=LSystemGrammar(alphabet, constants, rules)

	axiom='A'
	steps=7

	string=grammar.generate(axiom, steps)
	print('ALGAE GROWTH EXAMPLE\n\tAxiom: '+str(axiom)+'\n\tIterations: '+str(steps)+'\n\tOutput: '+string+'\n')

def fractal_tree_example():
	alphabet=['0', '1']
	constants=['[', ']']
	rules={'1':'11', '0':'1[0]0'}

	grammar=LSystemGrammar(alphabet, constants, rules)

	axiom='0'
	steps=3

	string=grammar.generate(axiom, steps)
	print('FRACTAL TREE EXAMPLE\n\tAxiom: '+str(axiom)+'\n\tIterations: '+str(steps)+'\n\tOutput: '+string+'\n')

if __name__=="__main__":
	algae_growth_example()
	fractal_tree_example()