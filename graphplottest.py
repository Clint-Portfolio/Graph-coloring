import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.rcsetup as rcsetup

if __name__ == '__main__':

        G = nx.petersen_graph()
        plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.subplot(122)
        nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
        plt.show()
