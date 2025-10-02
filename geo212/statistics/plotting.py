import matplotlib.pyplot as plt
from .statistics import correlation_matrix

def plot_correlation_matrix(dados, cmap='gray'):
    matriz = correlation_matrix(dados)
    keys = list(dados.keys())
    plt.figure(figsize=(20,10))
    plt.title('Correlation Matrix')
    plt.imshow(matriz, cmap=cmap, vmin=-1, vmax=1)
    gca = plt.gca()
    # gca.invert_yaxis()
    labels = gca.get_xticklabels()
    labels[0].get_text()
    # labels_mod = []
    for l in labels:
        try:
            idx = int(l.get_text())
            if idx >= 0 and idx < len(keys):
                l.set_text(keys[idx])
        except:
            pass
    gca.xaxis.tick_top()
    # plt.xticks(rotation=90)
    gca.set_xticklabels(labels)
    gca.set_yticklabels(labels)
    plt.colorbar()
