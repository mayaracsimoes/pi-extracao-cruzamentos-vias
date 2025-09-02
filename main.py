import cv2
import numpy as np
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt


# --- FUNÇÃO AUXILIAR PARA VISUALIZAÇÃO ---
def exibir_etapas(imagens, titulos):
    """Função para exibir múltiplas imagens lado a lado."""
    fig, axes = plt.subplots(1, len(imagens), figsize=(15, 5))
    for i, (img, titulo) in enumerate(zip(imagens, titulos)):
        if len(img.shape) == 2:
            axes[i].imshow(img, cmap='gray')
        else:
            axes[i].imshow(img)
        axes[i].set_title(titulo)
        axes[i].axis('off')
    plt.tight_layout()
    plt.show()


# --- CARREGAR IMAGEM INICIAL ---
# Carrega a imagem em escala de cinza
imagem_original = cv2.imread('imagem_intensidade.png', cv2.IMREAD_GRAYSCALE)

# --------------------------------------------------------------------------
# ETAPA (a) e (b): Segmentação e Separação da Classe Vias
# --------------------------------------------------------------------------
# O artigo propõe separar pixels com valor de tons de cinza menor ou igual a 45.
# Isso é uma operação de limiarização (thresholding).
_, imagem_limiarizada = cv2.threshold(imagem_original, 45, 255, cv2.THRESH_BINARY_INV)

# Em seguida, é aplicado um filtro de mediana para reduzir ruídos.
# O tamanho do kernel não é especificado, usaremos 3x3 que é um valor comum.
imagem_mediana = cv2.medianBlur(imagem_limiarizada, 3)

exibir_etapas(
    [imagem_original, imagem_limiarizada, imagem_mediana],
    ["Original (Figura 4)", "Etapa (a): Limiarização (<=45)", "Etapa (b): Filtro de Mediana"]
)
