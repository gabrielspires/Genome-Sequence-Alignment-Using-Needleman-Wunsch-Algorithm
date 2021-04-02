# README

## Como rodar o programa

Para rodar o programa use o comando `python3 main.py <Arquivo de entrada>`, por exemplo, `python3 main.py Sequences/input3`.

Os arquivos de entrada que podem ser lidos seguem o seguinte formato:

```
>dados da sequencia 1
caracteres da sequencia1
>dados da sequencia 2
caracteres da sequencia 2
```

Apenas pares de sequencias poder ser lidos para o alinhamento, arquivos com mais de 2 sequencia irão ler apenas as duas primeiras.

### Exemplo de entrada e saída

Usando como exemplo a entrada 3, temos a saída abaixo que contém a matriz de pontuações e as duas sequências já alinhadas.

##### Entrada

```
>sequence1
DRQTAQAAGTTTIT
>sequence2
DRNTAQLLGTDTT

```

##### Saída

```
    w   D   R   Q   T   A   Q   A   A   G   T   T   T   I   T
v   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
D   0  6\  6_  6_  6_  6_  6_  6_  6_  6_  6_  6_  6_  6_  6_
R   0  6| 11\ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_
N   0  6| 11| 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_ 11_
T   0  6| 11| 11_ 16\ 16_ 16_ 16_ 16_ 16_ 16\ 16\ 16\ 16_ 16\
A   0  6| 11| 11_ 16| 20\ 20_ 20\ 20\ 20_ 20_ 20_ 20_ 20_ 20_
Q   0  6| 11| 16\ 16_ 20| 25\ 25_ 25_ 25_ 25_ 25_ 25_ 25_ 25_
L   0  6| 11| 16| 16_ 20| 25| 25_ 25_ 25_ 25_ 25_ 25_ 27_ 27_
L   0  6| 11| 16| 16_ 20| 25| 25_ 25_ 25_ 25_ 25_ 25_ 27| 27_
G   0  6| 11| 16| 16_ 20| 25| 25_ 25_ 31\ 31_ 31_ 31_ 31_ 31_
T   0  6| 11| 16| 21\ 21_ 25| 25_ 25_ 31| 36\ 36\ 36\ 36_ 36\
D   0  6\ 11| 16| 21| 21_ 25| 25_ 25_ 31| 36| 36_ 36_ 36_ 36_
T   0  6| 11| 16| 21\ 21_ 25| 25_ 25_ 31| 36\ 41\ 41\ 41_ 41\
T   0  6| 11| 16| 21\ 21_ 25| 25_ 25_ 31| 36\ 41\ 46\ 46_ 46\
DR-QTAQ--AAGT-TTIT
DRN-TAQLL--GTD-T-T
```



