from collections import Counter

def sort_by_count_and_alphabetical(sentence: str, n: int) -> list:
	wordslist = sentence.split()
	word_count = Counter(sorted(wordslist))
	return word_count.most_common(n)
