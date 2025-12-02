"""Word Frequency Finder
Counts word frequency in a paragraph, with punctuation removal and optional CSV export.
"""
import string
import csv

def word_frequencies(text: str):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

if __name__ == '__main__':
    text = input('Enter a paragraph:\n\n')
    freq = word_frequencies(text)
    print('\nWord Frequency:\n')
    for word, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word} : {count}")
    save = input('\nSave results to CSV? (yes/no): ').strip().lower()
    if save in ('yes','y'):
        fname = input('Filename (e.g. freq.csv): ').strip() or 'freq.csv'
        with open(fname, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['word','count'])
            for w,c in sorted(freq.items(), key=lambda x:(-x[1], x[0])):
                writer.writerow([w,c])
        print('Saved to', fname)
