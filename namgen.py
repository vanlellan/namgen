# Markov Chain Name Generator
# Randall Evan McClellan
# 2017-04-09

#TO DO
#DONE	implement command line argument handler
#	implement choice of markov depth
#	implement namgen loop, options to quit, save, or next after each name


import random
from optparse import OptionParser


parser = OptionParser('Usage: %prog [options]')
parser.add_option('-d', '--depth', type = 'int', dest = 'depth', help = 'Markov Chain depth [default=%default]', default = 1)
parser.add_option('-i', '--infile', type = 'string', dest = 'infilename', help = 'Input file with list of names', default = '')



(options, args) = parser.parse_args()





allchars = '^abcdefghijklmnopqrstuvwxyz$'

if options.depth == 0:
	#Read in names
	cor0 = ''
	with open(options.infilename, 'r') as infile:
		for line in infile:
			if line[0] != '#':
				line = line.rstrip()+'$'
				cor0 = cor0 + line
	#Generate name
	name = '^'
	while name[-1] != '$':
		name = name + random.choice(cor0)

	#print name
	print name[1:-1]


if options.depth == 1:
	cor1 = {}
	#Read in Library of names
	with open(options.infilename, 'r') as infile:
		for line in infile:
			if line[0] != '#':
				line = '^'+line.rstrip()+'$'
				for i,let in enumerate(line):
					if i!=0:
						try:
							cor1[line[i-1]] += let
						except KeyError:
							cor1[line[i-1]] = let
	#Generate name
	name = '^'
	while name[-1] != '$':
		name = name + random.choice(cor1[name[-1]])
	
	#print name
	print name[1:-1]


