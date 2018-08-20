import csv, operator

dataset1 = 'data/tweets/lexicon_dataset/bitcointweets_new.tsv'
dataset2 = 'data/tweets/lexicon_dataset/sent140_1_new.tsv'
dataset3 = 'data/tweets/lexicon_dataset/sent140_2_new.tsv'
dataset4 = 'data/tweets/lexicon_dataset/twitter2_new.tsv'
dataset5 = 'data/tweets/lexicon_dataset/twitter4242_new.tsv'

def build_lexion_dataset(path):
    sentWords = dict()
    with open(path, 'r') as csvfile:
        rows = [row for row in csv.reader(csvfile, delimiter='\t')]

        for row in rows:
            content = row[0]
            sent = int(row[1])
            words = content.split(' ')
            for word in words:
                curr_sen = sent
                if word in sentWords:
                    curr_sen += sentWords[word]
                sentWords[word] = curr_sen


    sorted_neg = sorted(sentWords.items(), key=operator.itemgetter(1))
    sorted_pos = sorted(sentWords.items(), key=operator.itemgetter(1), reverse=True)

    # divide_neg = float(abs(sorted_neg[0][1]))
    # divide_pos = float(abs(sorted_pos[0][1]))

    path5 = path.replace('_new.tsv', '_5.tsv')
    path5 = path5.replace('lexicon_dataset', 'lexicons')
    path25 = path.replace('_new.tsv', '_25.tsv')
    path25 = path25.replace('lexicon_dataset', 'lexicons')

    with open(path5, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        for i in range(0, 5):
            word = sorted_pos[i][0]
            writer.writerow([word, 1])
            word = sorted_neg[i][0]
            writer.writerow([word, -1])


    with open(path25, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        for i in range(0, 25):
            word = sorted_pos[i][0]
            writer.writerow([word, 1])
            word = sorted_neg[i][0]
            writer.writerow([word, -1])


build_lexion_dataset(dataset1)
build_lexion_dataset(dataset2)
build_lexion_dataset(dataset3)
build_lexion_dataset(dataset4)
build_lexion_dataset(dataset5)