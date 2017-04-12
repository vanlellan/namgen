# Markov Chain Name Generator
# Randall Evan McClellan
# 2017-04-09

#TO DO
#DONE	implement command line argument handler
#DONE	implement choice of markov depth
#DONE	implement loop, options to quit, save, or next after each name
#DONE	write arbitrary depth function

import random
from optparse import OptionParser


parser = OptionParser('Usage: %prog [options]')
parser.add_option('-d', '--depth', type = 'int', dest = 'depth', help = 'Markov Chain depth [default=%default]', default = 2)
parser.add_option('-i', '--infile', type = 'string', dest = 'infilename', help = 'Input file with list of names', default = '')
parser.add_option('-o', '--outfile', type = 'string', dest = 'outfilename', help = 'Output file for saving names', default = '')

(options, args) = parser.parse_args()

if options.infilename == '':
	print "Must specify input file!"
	parser.parse_args(["--help"])


prevname = ''
keepOnKeepingOn = True
print "Enter for another name, s+Enter to save previous name, q+Enter to quit..."
while keepOnKeepingOn:		#MAIN LOOP

	command = raw_input()

	if command == 'q':
		keepOnKeepingOn = False

	if command == 's':
		try:
			with open(options.outfilename, 'a') as outfile:
				outfile.write(prevname+'\n')
			print "Saved \'"+prevname+"\' to "+options.outfilename
		except:
			print "Can't save to outfile: \'"+options.outfilename+"\'"



	#arbitrary depth generator	
	if command == '':
		maxdepth = options.depth
		cors = ['']+[{} for k in range(maxdepth)]

		#Read in Library of names
		with open(options.infilename, 'r') as infile:
			for line in infile:
				if line[0] != '#':
					line = '^'+line.rstrip()+'$'
					for i,let in enumerate(line):
						if i>0:
							 cors[0] += let
						for j,dic in enumerate(cors):
							if i>=j and j>0:
								try:
									dic[line[i-j:i]] += let
								except KeyError:
									dic[line[i-j:i]] = let
		#Generate name
		name = '^'
		while name[-1] != '$':
			leng = len(name)
			if maxdepth == 0:
				name = name + random.choice(cors[0])
			elif leng >= maxdepth:
				name = name + random.choice(cors[-1][name[-maxdepth:]])
			else:
				name = name + random.choice(cors[leng][name[-leng:]])
		
		#print name
		print name[1:-1]
		prevname = name[1:-1]

