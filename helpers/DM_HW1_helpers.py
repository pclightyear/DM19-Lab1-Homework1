import pandas as pd
import matplotlib.pyplot as plt

def plot_term_matrix(matrix, precision):
    plt.subplots(figsize=(20, 25))
    plt.spy(matrix, precision=precision, markersize=1)

def convert_file_to_dataframe(file):
    with open(file, 'r', encoding='utf8') as reader:
        lines = reader.readlines()
        sentence = []
        label = []
        for l in lines:
            split = l.split('\t')
            sentence.append(split[0])
            label.append(split[1].rstrip())

        df = pd.DataFrame({'sentence': sentence, 'label': label})

    return df