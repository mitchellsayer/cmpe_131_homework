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
		dict_items =  list(words.items())
		top_five = []
		i = 0

		while len(top_five) < 5 and i < len(dict_items):
			cur_item = dict_items[i]
			i += 1

			if len(top_five) == 0:
				top_five.append(cur_item)
				continue
			last_item = top_five[-1]

			if cur_item[1] == last_item[1]:
				if cur_item[0] < last_item[0]:
					top_five[-1] = cur_item
			else:
				top_five.append(cur_item)

		for item in top_five:
			print(f'{item[0]}: {item[1]}')

if __name__ == "__main__":
	main()
