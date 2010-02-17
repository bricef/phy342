##
# Markdown to html script with goodies:
#	- latex support using mimetex as equation: $$...$$ or inline: $...$
#	- auto title and topnav using meta data and PyMeld
#
# Requires: PyMeld, markdown.py, mimetex.cgi, pygments css stylesheet
#
##

import markdown
import sys, os, re
from PyMeld import Meld as meld

MIMETEX_LOC="http://bricefernandes.com/cgi-bin/mimetex.cgi"
TEMPLATE_LOC="../static/template.html"

def usage():
	print"""
usage: python md2html.py <mdfile> <htmlfile> 

	<mdfile> The input markdown file
	<htmlfile> The output html file
"""
def sanitizeLatex(text):
	return re.sub(r"\\",r"%5C", text)
	
def wrapLatexBlock(text):
	return '<img alt="equation" class="block" src="%s?%s"></img>'%(MIMETEX_LOC,text)
	
def wrapLatexInline(text):
	return '<img alt="equation" class="inline" src="%s?%s"></img>'%(MIMETEX_LOC,text)

def prepLatexBlock(matchobj):
	return wrapLatexBlock(sanitizeLatex(matchobj.group()[2:-2]))

def prepLatexInline(matchobj):
	return wrapLatexInline(sanitizeLatex(matchobj.group()[1:-1]))


def convert(text):
	# initialise markdown
	md=markdown.Markdown(['footnotes','tables','toc(title=Table of Contents)','meta','codehilite'])
	raw_md=text

	##
	# deal with embedded latex
	##

	raw_md=re.sub(r'\$\$(.*?)\$\$',prepLatexBlock, raw_md)
	raw_md=re.sub(r'\$(.*?)\$',prepLatexInline, raw_md)

	##
	# once latex is parsed, convert md to html
	##
	main_html=md.convert(raw_md)

	melded_wrapper=meld(open(TEMPLATE_LOC,"r").read())
	melded_wrapper.main=main_html

	##
	# write to file
	##
	return str(melded_wrapper)


if __name__=="__main__":
	try:
		text=sys.argv[1]
		html=sys.argv[2]
	except IndexError:
		usage()
		sys.exit()
	if not os.access(text, os.R_OK):
		print "the input file '%s' could not be read. Exiting."%(text)
		sys.exit()
	open(html,"w").write(convert(open(text,"r").read()))
