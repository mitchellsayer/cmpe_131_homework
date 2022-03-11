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
		top_five = dict(sorted(top_five, key = lambda item: item[0]))
		print_count = 0

		for item in top_five.items():
			print(f'{item[0]}: {item[1]}')
			print_count += 1

		print(top_five)

if __name__ == "__main__":
	main()
