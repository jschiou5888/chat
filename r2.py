
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	jack1_word = 0
	jack1_sticker = 0
	jack1_image = 0
	jack2_word = 0
	jack2_sticker = 0
	jack2_image = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '邱俊雄':
			if s[2] == '貼圖':
				jack1_sticker += 1
			elif s[2] == '圖片':
				jack1_image += 1
			else:	
				for m in (s[2:]):
					jack1_word += len(m)
		elif name == '邱俊哲':
			if s[2] == '貼圖':
				jack2_sticker += 1
			elif s[2] == '圖片':
				jack2_image += 1	
			else:
				for m in (s[2:]):
					jack2_word += len(m)
	print('邱俊雄說了', jack1_word, '個字')
	print('邱俊雄傳了', jack1_sticker, '個貼圖')
	print('邱俊雄傳了', jack1_image, '張圖片')

	print('邱俊哲說了', jack2_word, '個字')
	print('邱俊哲傳了', jack2_sticker, '個貼圖')
	print('邱俊哲傳了', jack2_image, '張圖片')

			
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():	
    lines = read_file('[line]邱俊哲.txt')
    lines = convert(lines)
    # print(lines)
    # write_file('output.txt', lines)

main()			
