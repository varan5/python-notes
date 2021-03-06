#Study of File Handling

def fileRead(fileName):
	#open the file in text mode for reading
	#file must exist otherwise FileError gets raised.
	#On success a file handle is returned that
	#must be used for all file operations ahead.
	fh = open(fileName,'r')

	#fetch the file content
	#use chunking if file is too big
	text = fh.read()
	print(text)

	#close the file
	fh.close()

def fileReadLineByLine_1(fileName):
	fh = open(fileName, 'r')
	while True:
		#chunk : a line
		x = fh.readline()
		if x:
			print(x, end='')
		else:
			break
	fh.close()

def fileReadLineByLine_2(fileName):
	fh = open(fileName, 'r')
	for x in fh:
		print('*', x, end='')

	fh.close()


def fileCopy(src, trgt):
	#open the source file for reading in binary mode
	#file must exist
	fh_src = open(src, 'rb')

	# open the target file for writing in binary mode
	#file will be created or overwritten
	fh_trgt = open(trgt, 'wb')
	chunkSize = 2048

	while True:
		x = fh_src.read(chunkSize)
		if x:
			fh_trgt.write(x)
		else:
			break
	print('File Copied')

	fh_trgt.close()
	fh_src.close()



myFile = 'd:/a.txt'
src = 'd:/q.png'
trgt = 'd:/qqqq.png'

#fileRead(myFile)
#fileReadLineByLine_1(myFile)
#fileReadLineByLine_2(myFile)
fileCopy(src, trgt )