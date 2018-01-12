#! /usr/bin/env python3

#class Dev_IPA_RuleBasedTranscription:
	
def transcribe(string):
	"""Transcribes the Sanskrit devanagari text in the input into IPA, i.e., the
		International Phonetic Alphabet"""
		
	transText = ""
	
	vowelB = 0
	vowelA = 0
	prevChar = 0 # 1 == nasal, 2 == 'halant'
	
	#Syllabify
	#for charIndex in range(len(string)):
	charIndex = 0
	
	
	while False:#True:
	
		try :
			c = string[charIndex]
		except Exception :
			break
	
		if not charInRange(string[charIndex]):
			#raise Exception("Character %s out of range."%str(char))
			pass
			
#	ऊर...्ध्व.म.ू.ल.म.ध.ः...श.ा.खमश.्व.त्थ.ं प.्र.ा.ह.ुरव.्ययम.्.......
#	ऊ.र.्ध्व.म.ू.लमध.ःश..ा.खमश.्व.त.्थ.ं प..्राह..ुरव.्ययम्

		if (string[charIndex] in mapping['VOWELS']) or (charIndex+1 < len(string) and string[charIndex+1] != "्" and not string[charIndex+1] in mapping['VOWELS']) :
			vowelB = vowelA
			vowelA = charIndex
			splitStr = string[vowelB+1:vowelA]
			print(splitStr)
			splitLen = 0
			numHalant = 0
			for counter in range(len(splitStr)) :
				if not splitStr[counter] == '्' :
					splitLen += 1
				else :
					numHalant += 1
			
			if splitLen == 1 :
				print(1)
				string = string[:vowelB+1] + "." + string[vowelB+1:]
			elif splitLen == 2 :
				print(2)
				string = string[:vowelB+2+1] + "." + string[vowelB+2+1:]
			elif splitLen == 3 :
				print(3)
				if string[vowelA-2] in {'र', 'य'} :
					string = string[:vowelB+2+1] + "." + string[vowelB+2+1:]
				elif string[vowelA-4] in stops and string[vowelA-6] in stops :
					string = string[:vowelB+2+1] + "." + string[vowelB+2+1:]
				else :
					string = string[:vowelB+2+2+1] + "." + string[vowelB+2+2+1:]
			elif splitLen :
				print(4)
				if string[vowelA-2] in {'र', 'य'} :
					string = string[:vowelA-2-2] + "." + string[vowelA-2-2:]
				else :
					minSonorous = vowelB + 1
					minSonority = 8
					for i in range(splitLen,2) :
						if sonority.get(string[vowelB+1+i],100) < minSonority  :
							minSonorous = vowelB+1+i
							minSonority = sonority.get(string[minSonorous])
					string = string[:vowelB+minSonorous+1] + "." + string[vowelB+minSonorous+1:]
			if splitLen :
				charIndex += 1
			
		charIndex += 1
		print(string)
	
	
	for charIndex in range(len(string)):
			
		if (string[charIndex] == '्') or (str(string[charIndex]) in mapping['VOWELS']) :
			"""Decision block to delete preceding schwa (ə) if the current char
			is either a vowel modifier or a 'halant' indicator."""
			transText = transText[:len(transText)-1]
			if transText[len(transText)-1] == "ə" :
				transText = transText[:len(transText)-1]

		if prevChar == 1 :
			"""Check to see if the previous character had an 'anuswar',
			and if so, apply the appropriate nasal sound according to next phoneme"""		
			for label in ['VELAR', 'PALATAL', 'RETROFLEX', 'DENTAL', 'LABIAL'] :
				if string[charIndex] in mapping[label] :
					transText = transText[:len(transText)-1]
					transText += str(mapping[label]['NASAL'])
					break
				transText = transText[:len(transText)-1] + "̃"
				
		elif prevChar == 2 :
			"""Decision block to assign stress, if any"""
			if not string[charIndex] in mapping['VOWELS'] :	# implying a consonant cluster
				backTrack = charIndex-1
				while (backTrack > 0 and string[backTrack] != "."):
					backTrack -= 1
				syllableBeginning = backTrack
				while backTrack < charIndex and not string[backTrack] in vowels :
					backTrack += 1
				if string[backTrack] in {'ङ', 'ञ', 'ण', 'न', 'म', 'ं'} or string[backTrack] in longVowels :
					pass
				else :
					syllables = transText.split('.')[:len(transText.split('.'))-1]
					lastSyllable = transText.split('.')[len(transText.split('.'))-1]
					transText = ""
					for syllable in syllables :
						transText += str(syllable) + "."
					transText += "ˈ" + str(lastSyllable)
		
		if not string[charIndex] == '.' :
			if (string[charIndex] == 'ं') :
				"""If the current character is an 'anuswar', raise a flag to indicate
				the need for a nasal sound check during transcription of the next char."""
				prevChar = 1
			elif (string[charIndex] == '्') :
				if prevChar != 2 : prevChar = 2
				else : prevChar = 4
			else : prevChar = 0
				
		transText += str(mapping.get(string[charIndex], '~'))
		print(transText + '\n')
	return transText
	
	
def charInRange(c):
	"""Boolean returning function to check if a character is Devanagari"""
	o = ord(c)
	lower = int('0x900', 16)
	upper = int('0x97f', 16)
	"""Set of Devanagari characters that are not used in Sanskrit-Dev orthography"""
	exclude = {'0x900', '0x904', '0x90e', '0x912', '0x929', '0x931', '0x934', '0x93a', '0x93b', '0x93c', '0x946', '0x94e', '0x94f', '0x94a', '0x951', '0x952', '0x953', '0x954', '0x955', '0x956', '0x957', '0x958', '0x959', '0x95a', '0x95b', '0x95c', '0x95d', '0x95e', '0x95f', '0x973', '0x974', '0x975', '0x976', '0x977', '0x978', '0x979', '0x97a', '0x97b', '0x97c', '0x97f', '0x97d', '0x97e', '0x970', '0x971'}
	return (o >= lower and o <= upper) and not (hex(o) in exclude)
	
	
mapping = {
	'ॐ' : 'oːm',
	'अ' : 'ə',
	'आ' : 'ɑ', 'ा' : 'ɑ',
	'इ' : 'i', 'ि' : 'i',
	'ई' : 'iː', 'ी' : 'iː',
	'उ' : 'u', 'ु' : 'u',
	'ऊ' : 'uː', 'ू' : 'uː',
	'ऋ' : 'ɹ̩', 'ॠ' : 'ɹ̩ː', 'ृ' : 'ɹ̩', 'ॄ' : 'ɹ̩ː',
	'ऌ' : 'l̩', 'ॢ' : 'l̩', 'ॡ' : 'l̩ː',
	'ए' : 'eː', 'े' : 'eː',
	'ऐ' : 'əi', 'ै' : 'əi',
	'ओ' : 'oː', 'ो' : 'oː',
	'अाै' : 'əu', 'ाै' : 'əu',
	'अं' : 'əm', 'ं' : 'əm',
	'अः' : 'əh', 'ः' : 'əh',
	'VOWELS' : {
		'ा' : 'ɑ',
		'ि' : 'i',	'ी' : 'iː',
		'ु' : 'u', 'ू' : 'uː',
		'ृ' : 'ɹ̩', 'ॄ' : 'ɹ̩ː', 'ॢ' : 'l̩',
		'े' : 'eː', 'ै' : 'əi',
		'ो' : 'oː', 'ाै' : 'əu',
		'ः' : 'əh', 'ं' : 'əm',
	},
	'क' : 'kə', 'ख' : 'kʰə', 'ग' : 'gə', 'घ' : 'gʰə', 'ङ' : 'ŋə',
	'VELAR' : {'क' : 'kə', 'ख' : 'kʰə', 'ग' : 'gə', 'घ' : 'gʰə', 'NASAL' : 'ŋə',},
	'च' : 't͡ʃə', 'छ' : 't͡ʃʰə', 'ज' : 'd͡ʒə', 'झ' : 'd͡ʒʱə', 'ञ' : 'ɲə',
	'PALATAL' : {'च' : 't͡ʃə', 'छ' : 't͡ʃʰə', 'ज' : 'd͡ʒə', 'झ' : 'd͡ʒʱə', 'NASAL' : 'ɲə',},
	'ट' : 'ʈə', 'ठ' : 'ʈʰə', 'ड' : 'ɖə', 'ढ' : 'ɖʰə', 'ण' : 'ɳə',
	'RETROFLEX' : {'ट' : 'ʈə', 'ठ' : 'ʈʰə', 'ड' : 'ɖə', 'ढ' : 'ɖʰə', 'NASAL' : 'ɳə',},
	'त' : 't̪ə', 'थ' : 't̪ʰə', 'द' : 'd̪ə', 'ध' : 'd̪ʰə', 'न' : 'nə',
	'DENTAL' : {'त' : 't̪ə', 'थ' : 't̪ʰə', 'द' : 'd̪ə', 'ध' : 'd̪ʰə', 'NASAL' : 'nə',},
	'प' : 'pə', 'फ' : 'pʰə', 'ब' : 'bə', 'भ' : 'bʱə', 'म' : 'mə',
	'LABIAL' : {'प' : 'pə', 'फ' : 'pʰə', 'ब' : 'bə', 'भ' : 'bʱə', 'NASAL' : 'mə',},
	'य' : 'jə', 'र' : 'ɹə', 'ल' : 'lə', 'व' : 'ʋə', 'श' : 'ɕə',
	'ष' : 'ʂə', 'स' : 'sə', 'ह' : 'ɦə', 'ळ' : 'ɭə',
	'क्ष' : 'kʂə', 'ज्ञ' : 'd͡ʒɲə', 'त्र' : 't̪ɹə',
	'्' : '', 'ऽ' : '',#ː',
	#escape
	' ' : ' ', '\n' : '\n', '\t' : '\t', '\r' : '\n', '.' : '.',
}

vowels = {
	'ा' : 'ɑ',
	'ि' : 'i',	'ी' : 'iː',
	'ु' : 'u', 'ू' : 'uː',
	'ृ' : 'ɹ̩', 'ॄ' : 'ɹ̩ː', 'ॢ' : 'l̩',
	'े' : 'eː', 'ै' : 'əi',
	'ो' : 'oː', 'ाै' : 'əu',
	'ः' : 'əh', 'ं' : 'əm',
	'ॐ' : 'oːm',
	'अ' : 'ə',
	'आ' : 'ɑ', 'ा' : 'ɑ',
	'इ' : 'i', 'ि' : 'i',
	'ई' : 'iː', 'ी' : 'iː',
	'उ' : 'u', 'ु' : 'u',
	'ऊ' : 'uː', 'ू' : 'uː',
	'ऋ' : 'ɹ̩', 'ॠ' : 'ɹ̩ː', 'ृ' : 'ɹ̩', 'ॄ' : 'ɹ̩ː',
	'ऌ' : 'l̩', 'ॢ' : 'l̩', 'ॡ' : 'l̩ː',
	'ए' : 'eː', 'े' : 'eː',
	'ऐ' : 'əi', 'ै' : 'əi',
	'ओ' : 'oː', 'ो' : 'oː',
	'अाै' : 'əu', 'ाै' : 'əu',
	'अं' : 'əm', 'ं' : 'əm',
	'अः' : 'əh', 'ः' : 'əh',
}

longVowels = {
	'ा' : 'ɑ', 'ी' : 'iː', 'ू' : 'uː', 'ॄ' : 'ɹ̩ː', 'ॢ' : 'l̩',
	'े' : 'eː', 'ै' : 'əi', 'ो' : 'oː', 'ाै' : 'əu',
	'ः' : 'əh', 'ं' : 'əm',
}

stops = {
	'क' : 'kə', 'ख' : 'kʰə', 'ग' : 'gə', 'घ' : 'gʰə', #'ङ' : 'ŋə',
	'च' : 't͡ʃə', 'छ' : 't͡ʃʰə', 'ज' : 'd͡ʒə', 'झ' : 'd͡ʒʱə', #'ञ' : 'ɲə',
	'ट' : 'ʈə', 'ठ' : 'ʈʰə', 'ड' : 'ɖə', 'ढ' : 'ɖʰə', #'ण' : 'ɳə',
	'त' : 't̪ə', 'थ' : 't̪ʰə', 'द' : 'd̪ə', 'ध' : 'd̪ʰə', #'न' : 'nə',
	'प' : 'pə', 'फ' : 'pʰə', 'ब' : 'bə', 'भ' : 'bʱə', #'म' : 'mə',
}

sonority = {
	'क' : 1, 'च' : 1, 'ट' : 1, 'त' : 1, 'प' : 1,
	'ख' : 2, 'छ' : 2, 'ठ' : 2, 'थ' : 2, 'फ' : 2,
	'ग' : 3, 'ज' : 3, 'ड' : 3, 'द' : 3, 'ब' : 3,
	'घ' : 4, 'झ' : 4, 'ढ' : 4, 'ध' : 4, 'भ' : 4,
	'ङ' : 5, 'ञ' : 5, 'ण' : 5, 'न' : 5, 'म' : 5,
	'श' : 6, 'ष' : 6, 'स' : 6, 'ह' : 6, 'ळ' : 6,
	'य' : 7, 'र' : 7, 'ल' : 7, 'व' : 7,
	# vowels : 8,
	
}
