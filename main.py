import xml.etree.ElementTree as ET
import shutil
import glob

for file in glob.glob("*.xml"):

	tree = ET.parse(file)

	root = tree.getroot()

	# Simple boolean var for determining pass/fail status of file
	# We assume it is valid until we find an error
	valid_xml = True

	for book in root.findall('entry'):
		if( len(book.find("sender").text) > 50 or len(book.find("sender").text) < 10 ):
			valid_xml = False

		if( len(book.find("recipient").text) > 50 or len(book.find("recipient").text) < 10 ):
			valid_xml = False

		if( len(book.find("distance").text) > 8 or len(book.find("distance").text) < 3 ):
			valid_xml = False

		if( len(book.find("time").text) != 4 ):
			valid_xml = False

	if valid_xml == True:
		shutil.move( file, "passed/" + file )
	elif valid_xml == False:
		shutil.move( file, "failed/" + file )
	else:
		shutil.move( file, "error/" + file )

