# Extração Semi-Automática de Cruzamentos de Vias em Python
### Objetivo do Projeto
Este repositório contém uma implementação em Python do método de extração semi-automática de cruzamentos de vias urbanas, baseado em imagens de intensidade LiDAR. O algoritmo foi desenvolvido a partir da metodologia proposta no artigo científico de Santos, D. J. et al. (2011).

Este projeto foi criado como trabalho prático para a disciplina de Processamento de Imagens, com o objetivo de aplicar conceitos de limiarização, morfologia matemática (erosão e dilatação) e análise de componentes para resolver um problema real.

### Artigo de Referência
O trabalho implementado se baseia integralmente na seguinte publicação:

Santos, D. J. dos; Santos, D. R. dos; Reiss, M. L. L. EXTRAÇÃO SEMI-AUTOMÁTICA DE CRUZAMENTOS DE VIAS EM ÁREAS URBANAS USANDO IMAGEM DE INTENSIDADE DO PULSO LASER. 

Revista Brasileira de Cartografia, N° 63/03, 2011. ISSN 1808-0936.


### Metodologia Implementada
O algoritmo segue as seis etapas principais descritas no fluxograma da Figura 3 do artigo:


Segmentação da Imagem: A imagem de intensidade é binarizada através de uma limiarização para separar os pixels pertencentes à classe "vias", utilizando um valor de corte de 45.


Separação e Filtro: Após a binarização, um filtro de mediana é aplicado para reduzir ruídos do tipo "sal e pimenta" na imagem.

#### Operadores Morfológicos:


Erosão: Uma operação de erosão com um elemento estruturante de disco (15x15 pixels) é aplicada para eliminar pequenos ruídos externos às vias e preencher falhas internas.


Limpeza e Preenchimento: Um processo de análise de contornos é realizado para remover polígonos de ruído e preencher completamente a malha viária principal.




Esqueletização: A malha viária limpa é afinada para obter seus eixos centrais (esqueleto), que são essenciais para a detecção dos pontos de cruzamento.



Detecção de Hipóteses de Cruzamentos: O esqueleto é analisado com uma máscara 3x3 para identificar pixels que representam junções de três ou mais ramos, gerando uma lista de cruzamentos em potencial.

Seleção de Pontos de Referência: As hipóteses são validadas para remover falsos positivos. Cada ponto é verificado em um buffer (20x20 pixels) para garantir que ele se conecta a pelo menos dois eixos e duas bordas de via.



Extração dos Cruzamentos: Os pontos de referência validados são usados para extrair e destacar as áreas de cruzamento correspondentes na imagem original.

### Tecnologias Utilizadas
