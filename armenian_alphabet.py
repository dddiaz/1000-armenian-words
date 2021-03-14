# Download raw alphabet from here: http://mylanguages.org/armenian_alphabet.php
# darn looks like its uppercase which is a problem as python lower and upper dont handle it right
raw_alphabet = """ա	ɑ	ɑ	Like the 'ah' in 'father'
բ	b	pʰ	like the 'b' in 'boat'
գ	ɡ	kʰ	like the 'k' in 'key' or 'g' in 'goat'
դ	d	tʰ	like the 'd' in 'dog'
ե	(j)ɛ	(j)ɛ	like the 'ye' in 'yet' or 'eh' in 'bet'
զ	z	z	like the 'z' in 'zebra'
է	ɛ	ɛ	Like the 'e' in 'end'
ը	ə	ə	Like the 'u' in 'but'
թ	tʰ	tʰ	Like the 't' in 'tomorrow'
ժ	ʒ	ʒ	Like the 's' in 'measure'
ի	i	i	Like the 'ee' in 'meet'
լ	l	l	Like the 'l' in 'lily'
խ	χ	χ	Like guttural 'ch' in 'Bach'
ծ	ts	dz	Like the 'tz' in 'Mitzi'
կ	k	ɡ	Like the 'ck' in 'Micky'
հ	h	h	Like the 'h' in 'hello'
ձ	dz	tsʰ	Like the 'ds' in 'kids'
ղ	ʁ	ʁ	Like a guttural French 'r'
ճ	tʃ	dʒ	Like a hard, clipped 'j' 
մ	m	m	Like the 'm' in 'mom'
յ	j	j	Like the 'y' in 'year' or 'y' in 'buy'
ն	n	n	Like the 'n' in 'number'
շ	ʃ	ʃ	Like the 'sh' in 'shower'
ո	(v)o	(v)o	Like the 'vo' in 'vocal' (beginning) or 'o' in 'low' (within a word)
չ	tʃʰ	tʃʰ	Like the 'ch' in 'church'
պ	p	b	Like the 'p' in 'pizza'
ջ	dʒ	tʃʰ	Like the 'j' in 'jeans'
ռ	r	r/ɾ	Like the rolled Spanish 'r'
ս	s	s	Like the 's' in 'sand'
վ	v	v	Like the 'v' in 'Victor'
տ	t	d	Like a hard 't' in 'but'
ր	ɾ	ɾ	Like the 'r' in 'red' or 'rh' in 'bother' (word endings)
ց	tsʰ	tsʰ	Like the 'ts' in 'bits'
ւ	v	v	like the 'oo' in 'cool'
փ	pʰ	pʰ	like the 'p' in 'pear'
ք	kʰ	kʰ	like the 'k' in 'kite'
օ	o	o	like the 'o' in 'bone'
ֆ	f	f	like the 'f' in 'life'
ու	u	u	like the 'oo' in 'cool'
և	(j)ɛv	(j)ɛv	Combination of sounds 'ye' and 'v'
 :	 :	 :	Full stop or period."""


def get_armenian_alphabet_map():
    armenian_alphabet_map = {}
    for line in raw_alphabet.splitlines():
        line_chunks = line.split()
        # I think these are uppercase?
        armenian_letter = line_chunks[0]
        english_sound = line_chunks[1]
        pronunciation_example = line_chunks[2]
        english_sound_description = line_chunks[3:]
        # print(f"Armernian Letter: {armenian_letter} english sound: {english_sound} pronunciation_example: {pronunciation_example} english_sound_description: {' '.join(english_sound_description)}")
        armenian_alphabet_map[armenian_letter] = (english_sound, pronunciation_example, ' '.join(english_sound_description))
    return armenian_alphabet_map


if __name__ == '__main__':
    armenian_map = get_armenian_alphabet_map()
    for k,v in armenian_map.items():
        print(f"Armernian Letter: {k} english sound: {v[0]} pronunciation_example: {v[1]} english_sound_description: {v[2]}")