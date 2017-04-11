# Markov Chain Name Generator
# Randall Evan McClellan
# 2017-04-09

#TO DO
#DONE	implement command line argument handler
#0-2	implement choice of markov depth
#	implement loop, options to quit, save, or next after each name
#	write function for depth 1 and up

import random
from optparse import OptionParser


parser = OptionParser('Usage: %prog [options]')
parser.add_option('-d', '--depth', type = 'int', dest = 'depth', help = 'Markov Chain depth (0,1,2) [default=%default]', default = 1)
parser.add_option('-i', '--infile', type = 'string', dest = 'infilename', help = 'Input file with list of names', default = '')
parser.add_option('-o', '--outfile', type = 'string', dest = 'outfilename', help = 'Output file for saving names', default = '')



(options, args) = parser.parse_args()

if options.depth not in (0,1,2):
	parser.parse_args(["--help"])



prevname = ''
keepOnKeepingOn = True
print "Enter for another name, s+Enter to save previous name, q+Enter to quit..."
while keepOnKeepingOn:

	command = raw_input()

	if command == 'q':
		keepOnKeepingOn = False

	if command == 's':
		with open(options.outfilename, 'a') as outfile:
			outfile.write(prevname+'\n')
		print "Saved \'"+prevname+"\' to "+options.outfilename

	allchars = '^abcdefghijklmnopqrstuvwxyz$'
	
	if options.depth == 0 and command == '':
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
	
	
	if options.depth == 1 and command == '':
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
	
	
	if options.depth == 2 and command == '':
		cor2 = {}
		startchar = ''
		#Read in Library of names
		with open(options.infilename, 'r') as infile:
			for line in infile:
				if line[0] != '#':
					line = '^'+line.rstrip()+'$'
					for i,let in enumerate(line):
						if i==1:
							startchar = startchar+let
						if i>=2:
							try:
								cor2[line[i-2:i]] += let
							except KeyError:
								cor2[line[i-2:i]] = let
		#Generate name
		name = '^'+random.choice(startchar)
		while name[-1] != '$':
			name = name + random.choice(cor2[name[-2:]])
		
		#print name
		print name[1:-1]
		prevname = name[1:-1]
	

