# !/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python inventory2meta.py "path/to/inventory/file.csv"
# ToDo : bug to solve : 'ascii' codec can't decode byte 0xc2 in position 129

#
# Libs
#
import codecs
import csv
import sys

# Force default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

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
	with codecs.open(file, mode='rb', encoding='utf-8') as f :
		# spamreader = csv.reader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
		# ToDo : set fieldnames
		fieldnames = []
		spamreader = csv.DictReader(f, fieldnames=fieldnames)
		for s in spamreader :
			data.append(s)
	# Skip the first lines that are useless
	return data[3:]

# Generate the meta_documents data
def generateMetaDocument(input) :
	output = []
	for i in input :
		tmp = {}
		tmp["id"] = i[None][1].encode('utf-8')
		# Has to be generated based on the file_id
		tmp['file'] = i[None][3].decode('ascii') + '/' + i[None][4].decode('ascii') + '/' + i[None][5].decode('ascii') + '/' + i[None][1].decode('ascii')
		# tei, pdf, htm, csv, link or ref
		tmp['mimetype'] = i[None][16].decode('ascii')
		# Label written on the website
		# print i[None][10].decode('ascii')
		tmp['name'] = i[None][10].decode('ascii')
		# prep, col, anal, ese or compl
		tmp['researchPhase'] = i[None][3].decode('ascii')
		# admi, audio, docu, icono, inter, methodo, note, publi, revis or transcr
		tmp['documentType'] = i[None][4].decode('ascii')
		# file_article = ''
		tmp['article'] = ''
		# file_location_01 = ''
		tmp['location'] = ''
		# file_location_02 = ''
		tmp['location'] = ''
		# file_locationgeo_01 = ''
		tmp['locationgeo'] = ''
		# file_locationgeo_02 = ''
		tmp['locationgeo'] = ''
		tmp['date'] = i[None][11].decode('ascii')
		output.append(tmp)
		# print output
	return output

# Write data into a CSV file as result
def writeCsvFile(data) :
	# Add csv headers
	# csv_headers = [['id', 'file', 'mimetype', 'name', 'researchPhase', 'documentType', 'article', 'location', 'location', 'locationgeo', 'locationgeo', 'date']]
	fieldnames = ['id', 'file', 'mimetype', 'name', 'researchPhase', 'documentType', 'article', 'location', 'location', 'locationgeo', 'locationgeo', 'date']
	# data = [{'id' : 'flag_01', 'file' : 'flag_02', 'mimetype' : 'flag_03', 'name' : 'flag_04', 'researchPhase' : 'flag_05', 'documentType' : 'flag_06', 'article' : 'flag_07', 'location' : 'flag_08', 'location' : 'flag_09', 'locationgeo' : 'flag_10', 'locationgeo' : 'flag_11', 'date' : 'flag_12'}]
	# data = csv_headers + data
	# Write results into a CSV data file
	with codecs.open(csv_file, 'wb', 'utf8') as f :
		# spamwriter = csv.writer(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
		csvwriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=csv_delimiter)
		csvwriter.writeheader()
		csvwriter.writerows(data)
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
		# Write meta_document
		writeCsvFile(output)
	else :
		print ''
		print 'Argument error'
		print 'Execution example : python inventory2meta.py "path/to/inventory/file.csv"'