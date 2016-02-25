#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python inventory2meta.py "path/to/inventory/file.csv"

#
# Libs
#
import codecs
import csv
import sys

#
# Config
#
csv_file = 'meta_documents.csv'
csv_delimiter = ','
csv_quotechar = '"'

#
# Functions
#

def loadCsvFile(file) :
	data = []
	with open(file, 'rb') as f :
		spamreader = csv.reader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
		for s in spamreader :
			data.append(s)
	# Skip the first lines that are useless
	return data[4:]

# Generate the meta_documents data
def generateMetaDocument(input) :
	output = []
	for i in input :
		file_id = i[1]
		# Has to be generated based on the file_id
		file_file = ''
		# tei, pdf, htm, csv, link or ref
		file_mimetype = ''
		# Label written on the website
		file_name = ''
		# prep, col, anal, ese or compl
		file_researchPhase = ''
		# admi, audio, docu, icono, inter, methodo, note, publi, revis or transcr
		file_documentType = ''
		file_article = ''
		file_location_01 = ''
		file_location_02 = ''
		file_locationgeo_01 = ''
		file_locationgeo_02 = ''
		file_date = ''
		output.append([file_id, file_file, file_mimetype, file_name, file_researchPhase, file_documentType, file_article, file_location_01, file_location_02, file_locationgeo_01, file_locationgeo_02, file_date])
	return output

# Write data into a CSV file as result
def writeCsvFile(data) :
	# Add csv headers
	csv_headers = [['id', 'file', 'mimetype', 'name', 'researchPhase', 'documentType', 'article', 'location', 'location', 'locationgeo', 'locationgeo', 'date']]
	data = csv_headers + data
	# Write results into a CSV data file
	with codecs.open(csv_file, 'wb', 'utf8') as f :
		spamwriter = csv.writer(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
		spamwriter.writerows(data)
	f.close()

#
# Main
#
if __name__ == '__main__' :
	# Check that the inventory file is here and that's a csv file
	if len(sys.argv) == 2 and sys.argv[1].split('.')[-1].lower() == 'csv' :
		# Load inventory file
		input = loadCsvFile(sys.argv[1])
		# Generate meta_document
		output = generateMetaDocument(input)
		print output
		# Write meta_document
		writeCsvFile(output)
	else :
		print ''
		print 'Argument error'
		print 'Execution example : python inventory2meta.py "path/to/inventory/file.csv"'