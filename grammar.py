class LSystemGrammar:
	def __init__(self, alphabet, constants, rules):
		self.alphabet=alphabet
		self.constants=constants
		self.rules=rules

	def generate(self, axiom, steps):
		string=[axiom]
		for i in range(steps):
			new_string=list(string)
			for j in range(len(string)):
				char=string[j]
				if char not in self.alphabet and char not in self.constants:
					raise Exception('Invalid character '+str(char)+'.')
				if char in self.rules:
					char=self.rules[char]
				string[j]=char
			new_string=[]
			for char in string:
				if len(char) > 1:
					for c in char:
						new_string.append(c)
				else:new_string.append(char)
			string=new_string

		output=''
		for char in string:
			output+=char
		return output