# L-System Grammar

From the [WikiPedia article](https://en.wikipedia.org/wiki/L-system) on L-systems:

_"An L-system or Lindenmayer system is a parallel rewriting system and a type of formal grammar. An L-system consists of an alphabet of symbols that can be used to make strings, a collection of production rules that expand each symbol into some larger string of symbols, an initial "axiom" string from which to begin construction, and a mechanism for translating the generated strings into geometric structures. L-systems were introduced and developed in 1968 by Aristid Lindenmayer, a Hungarian theoretical biologist and botanist at the University of Utrecht. Lindenmayer used L-systems to describe the behaviour of plant cells and to model the growth processes of plant development. L-systems have also been used to model the morphology of a variety of organisms[1] and can be used to generate self-similar fractals."_

### Examples

The following examples are explained thoroughly in the WikiPedia article if you are interested. 

__1) Algae growth Example__

	alphabet=['A', 'B']
	constants=[]
	rules={'A':'AB', 'B':'A'}

	grammar=LSystemGrammar(alphabet, constants, rules)

	axiom='A'
	steps=7

	string=grammar.generate(axiom, steps)
	print(string)

OUTPUT: ABAABABAABAABABAABABAABAABABAABAAB

__2) Fractal Tree Example__
	
	alphabet=['0', '1']
	constants=['[', ']']
	rules={'1':'11', '0':'1[0]0'}

	grammar=LSystemGrammar(alphabet, constants, rules)

	axiom='0'
	steps=3

	string=grammar.generate(axiom, steps)
	print(string)

OUTPUT: 1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0
