import  re

def main():
	words = {}
	alphanumeric_re = r'[^a-zA-Z_]+'

	with open('document.txt', 'r') as f:
		for line in f:
			for word in line.split():
				filtered_word = re.sub(alphanumeric_re, '', word)
				if filtered_word in words:
					words[filtered_word] += 1
				else:
					words[filtered_word] = 1

		words = dict(sorted(words.items(), key = lambda item: item[1], reverse=True))
		top_five = list(words.items())[:5]

		for item in top_five:
			print(f'{item[0]}: {item[1]}')

if __name__ == "__main__":
	main()
