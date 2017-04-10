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
parser.add_option('-d', '--depth', type = 'int', dest = 'depth', help = 'Markov Chain depth [default=%default]', default = 0)
parser.add_option('-i', '--infile', type = 'string', dest = 'infilename', help = 'Input file with list of names', default = '')



(options, args) = parser.parse_args()





allchars = '^abcdefghijklmnopqrstuvwxyz$'

cor = {}

#Read in Library of names
with open(options.infilename, 'r') as infile:
	for line in infile:
		if line[0] != '#':
			line = '^'+line.rstrip()+'$'
			for i,let in enumerate(line):
				if i!=0:
					try:
						cor[line[i-1]] += let
					except KeyError:
						cor[line[i-1]] = let


#Generate name
name = '^'
while name[-1] != '$':
		randi = random.randint( 0, len(cor[name[-1]])-1 )
		name = name + cor[name[-1]][randi]

#print name
print name[1:-1]


