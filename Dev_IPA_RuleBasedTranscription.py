#! /usr/bin/env python3

#class Dev_IPA_RuleBasedTranscription:
	
def transcribe(string):
	"""Transcribes the input Sanskrit devanagari text into IPA"""
	transText = ""
	for char in string:
		pass #pending
	
	
def charInRange(c):
	"""Boolean returning function to check if a character is Devanagari"""
	o = ord(c)
	lower = int('0x900', 16)
	upper = int('0x97f', 16)
	"""List of Devanagari characters that are not used in Sanskrit-Dev orthography"""
	exclude = {'0x900', '0x904', '0x90e', '0x912', '0x929', '0x931', '0x934', '0x93a', '0x93b', '0x93c', '0x946', '0x94e', '0x94f', '0x94a', '0x951', '0x952', '0x953', '0x954', '0x955', '0x956', '0x957', '0x958', '0x959', '0x95a', '0x95b', '0x95c', '0x95d', '0x95e', '0x95f', '0x973', '0x974', '0x975', '0x976', '0x977', '0x978', '0x979', '0x97a', '0x97b', '0x97c', '0x97f', '0x97d', '0x97e', '0x970', '0x971'}
	return (o >= lower and o <= upper) and not (hex(o) in exclude)
	
	
mapping = {
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
	'क' : 'kə', 'ख' : 'kʰə', 'ग' : 'gə', 'घ' : 'gʰə', 'ङ' : 'ŋə',
	'च' : 't͡ʃə', 'छ' : 't͡ʃʰə', 'ज' : 'd͡ʒə', 'झ' : 'd͡ʒʱə', 'ञ' : 'ɲə',
	'ट' : 'ʈə', 'ठ' : 'ʈʰə', 'ड' : 'ɖə', 'ढ' : 'ɖʰə', 'ण' : 'ɳə',
	'त' : 't̪ə', 'थ' : 't̪ʰə', 'द' : 'd̺ə', 'ध' : 'd̺ʰə', 'न' : 'nə',
	'प' : 'pə', 'फ' : 'pʰə', 'ब' : 'bə', 'भ' : 'bʱə', 'म' : 'mə',
	'य' : 'jə', 'र' : 'ɹə', 'ल' : 'lə', 'व' : 'ʋə', 'श' : 'ɕə',
	'ष' : 'ʂə', 'स' : 'sə', 'ह' : 'ɦə', 'ळ' : 'ɭə',
	'क्ष' : 'kʂə', 'ज्ञ' : 'd͡ʒɲə', 'त्र' : 't̪ɹə',
}
