import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

################## Pré-processamento ###################
# Coleta e Integração
iris = load_iris()

caracteristicas = iris.data

################### Mineração #####################
grupos = KMeans(n_clusters=3)
grupos.fit(X=caracteristicas)
labels = grupos.labels_  # indice do grupo ao qual cada amostra pertence

################ Pós-processamento ####################
fig = plt.figure(1)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1],
           caracteristicas[:, 2], c=grupos.labels_, edgecolor='k')

target = iris.target
fig = plt.figure(2)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1],
           caracteristicas[:, 2], c=target, edgecolor='k')

plt.show()
