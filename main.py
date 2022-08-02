import xml.etree.ElementTree as ET
import shutil
import glob
# import lxml
# from lxml import etree

for file in glob.glob("*.xml"):

	tree = ET.parse(file)

	root = tree.getroot()

	# Simple boolean var for determining pass/fail status of file
	# We assume it is valid until we find an error
	valid_xml = True

	# This portion of code is meant to validate against a schema, but is still under development
		# xml_file = lxml.etree.parse(file)
		# xml_validator = lxml.etree.XMLSchema(file="schema.xsd")

		# is_valid = xml_validator.validate(xml_file)

		# print(is_valid)

	for book in root.findall('entry'):
		if( isinstance(book.find("sender").text, str) ):
			if( len(book.find("sender").text) > 50 or len(book.find("sender").text) < 10 ):
				valid_xml = False

		if( isinstance(book.find("recipient").text, str) ):
			if( len(book.find("recipient").text) > 50 or len(book.find("recipient").text) < 10 ):
				valid_xml = False

		if( isinstance(book.find("message").text, str) ):
			if( len(book.find("message").text) > 8 or len(book.find("message").text) < 3 ):
				valid_xml = False

		# print( book.find("time") )
		if( isinstance(book.find("time").text, str) ):
			if( len(book.find("time").text) != 4 ):
				valid_xml = False

	if valid_xml == True:
		shutil.move( file, "passed/" + file )
	elif valid_xml == False:
		shutil.move( file, "failed/" + file )
	else:
		shutil.move( file, "error/" + file )