# jogo da cobrinha (snake)

![python](https://img.shields.io/badge/python-3.12-blue)
![pygame](https://img.shields.io/badge/pygame-2.x-green)
![repo size](https://img.shields.io/github/repo-size/olucaxx/snake)

https://github.com/olucaxx/snake/blob/main/assets/snake-demo.mp4

## sobre o projeto

primeiro projeto de 2026, desenvolvido principalmente como uma introdução ao **pygame** e à lógica básica de jogos 2d.

a serpente é representada como uma lista de posições, onde a movimentação ocorre removendo a cauda e adicionando uma nova cabeça a cada atualização.

## características principais

- serpente baseada em uma lista
- fila de comandos para suavizar mudanças rápidas de direção
- aumento dinâmico de velocidade conforme o tamanho
- renderização contínua do corpo com conexão entre segmentos
- geração segura de alimento fora do corpo da serpente

## requisitos

- **Python 3.12**
    - versões mais recentes apresentam problemas de compatibilidade com o pygame

## instalação e execução

```bash
git clone https://github.com/olucaxx/snake
cd snake
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python snake-the-game/game.py
```