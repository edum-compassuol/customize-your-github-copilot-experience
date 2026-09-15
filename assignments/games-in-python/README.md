
# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras em Python, praticando manipulação de strings, loops, condicionais e seleção aleatória. Ao final, você terá um jogo da Forca completo e jogável no terminal.

## 📝 Tarefas

### 🛠️ Sorteio da Palavra Secreta

#### Descrição
Escreva o código que escolhe aleatoriamente a palavra que o jogador precisará adivinhar, a partir de uma lista predefinida.

#### Requisitos
O programa concluído deve:

- Definir uma lista com pelo menos 5 palavras possíveis.
- Usar o módulo `random` para selecionar uma palavra da lista.
- Armazenar a palavra sorteada em uma variável, sem exibi-la ao jogador.

### 🛠️ Exibição do Progresso

#### Descrição
Mostre ao jogador o estado atual da palavra, revelando apenas as letras já descobertas.

#### Requisitos
O programa concluído deve:

- Exibir a palavra oculta no formato `_ _ _`, com um traço para cada letra ainda não adivinhada.
- Substituir os traços pelas letras corretas já descobertas.
- Exemplo de saída:

  ```text
  Palavra: p _ t h _ n
  Letras já tentadas: p, t, h, n, x
  ```

### 🛠️ Palpites e Controle de Tentativas

#### Descrição
Crie o loop principal do jogo, que recebe os palpites do jogador e atualiza o estado da partida.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra ao jogador a cada rodada usando `input()`.
- Registrar as letras já tentadas e avisar quando uma letra for repetida.
- Diminuir o número de tentativas restantes a cada palpite incorreto.
- Exibir quantas tentativas incorretas ainda restam.

### 🛠️ Fim de Jogo

#### Descrição
Encerre a partida quando o jogador vencer ou esgotar as tentativas e informe o resultado.

#### Requisitos
O programa concluído deve:

- Encerrar o loop quando todas as letras da palavra forem descobertas.
- Encerrar o loop quando o número de tentativas incorretas atingir o limite.
- Exibir uma mensagem de vitória, como `Parabéns! Você adivinhou a palavra: python`.
- Exibir uma mensagem de derrota revelando a palavra secreta, como `Você perdeu! A palavra era: python`.