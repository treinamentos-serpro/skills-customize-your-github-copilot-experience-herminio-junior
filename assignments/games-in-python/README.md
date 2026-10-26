
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo da Forca em Python para praticar manipulação de strings, seleção aleatória, condicionais, loops e entrada de dados do usuário.

## 📝 Tarefas

### 🛠️ Implementar a mecânica do jogo

#### Descrição
Use uma lista predefinida de palavras para iniciar uma partida. O jogador deve tentar descobrir a palavra secreta informando letras.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista
- Exibir cada letra ainda não descoberta como um espaço em branco, por exemplo, `_ _ _`
- Aceitar palpites de letras e revelar no progresso todas as posições correspondentes
- Registrar os palpites incorretos e mostrar quantas tentativas restam

### 🛠️ Encerrar a partida com o resultado

#### Descrição
Mantenha a partida ativa enquanto a palavra não for descoberta e ainda houver tentativas disponíveis. Ao final, informe o resultado ao jogador.

#### Requisitos
O programa concluído deve:

- Encerrar quando o jogador descobrir a palavra ou esgotar as tentativas
- Exibir uma mensagem de vitória quando a palavra for descoberta
- Exibir uma mensagem de derrota e revelar a palavra secreta quando as tentativas acabarem