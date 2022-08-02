import xml.etree.ElementTree as ET
import shutil
import glob
import xmlschema
import time

# loading the xsd schema
xsd = xmlschema.XMLSchema('schema.xsd')

index = 0
# infinite loop
while True:

	# descriptive terminal message
	print("Iteration: " + str(index) + " initiated.")

	# iterating over all xml files
	for file in glob.glob("*.xml"):

		# parsing file
		tree = ET.parse(file)

		# xsd.validate(tree)
		# validating file against schema
		if xsd.is_valid(tree):

			# finding the root of the xml data
			root = tree.getroot()

			# valid parameters boolean, we assume validity until we find an error
			valid_params = True

			# iterating over all elements labeled 'entry' and comparing value fields
			for book in root.findall('entry'):
				if( isinstance(book.find("sender").text, str) ):
					if( len(book.find("sender").text) > 50 or len(book.find("sender").text) < 10 ):
						valid_params = False

				if( isinstance(book.find("recipient").text, str) ):
					if( len(book.find("recipient").text) > 50 or len(book.find("recipient").text) < 10 ):
						valid_params = False

				if( isinstance(book.find("message").text, str) ):
					if( len(book.find("message").text) > 8 or len(book.find("message").text) < 3 ):
						valid_params = False

				if( isinstance(book.find("time").text, str) ):
					if( len(book.find("time").text) != 4 ):
						valid_params = False

			# after iteration of elements, parameter validity is checked to determine which directory the file belongs in
			if valid_params == True:
				shutil.move( file, "valid/" + file )
			elif valid_params == False:
				shutil.move( file, "invalid-params/" + file )
			else:
				shutil.move( file, "error/" + file )

		# if schema validation fails, move to invalid-schema directory
		else:
			shutil.move( file, "invalid-schema/" + file )

	# descriptive terminal message
	print("Iteration: " + str(index) + " completed.")
	index = index + 1

	# wait ten seconds
	time.sleep(10)