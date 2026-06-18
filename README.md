# TPPE_2026.1 - Trabalhos Práticos 1 e 2 - Curadoria de Dados e Refatoração

## Sobre o Projeto

Este projeto consiste no desenvolvimento de uma aplicação orientada a objetos para a curadoria e deduplicação de registros de autores em repositórios de informações científicas. O desenvolvimento foi inteiramente guiado por testes, segundo a logica "Test-Driven Development" (TDD), garantindo a confiabilidade na identificação e unificação de registros de publicações.

A aplicação resolve problemas comuns de duplicidade na integração de diferentes bases de dados indexadoras, contemplando os seguintes casos de padronização:
1. **Diferenças tipográficas e de grafia** (acentuação, cedilha, apóstrofos).
2. **Sobrenome + Iniciais dos nomes** vs. Nome Completo.
3. **Omissão de partículas "de"** e uso de ponto em abreviações.
4. **Iniciais agrupadas + sobrenome** vs. Nome Completo.
5. **Resolução de IDs conflitantes** (mapeamento para o ID de menor valor).

## Integrantes

| Matrícula | Nome do Integrante |
| :---: | :--- |
| João Pedro Costa | 190030801 |
| Julia Gabriela Cunha Paulino | 221029230 |
| Leonardo Sobrinho de Aguiar | 200022199 |

## Metodologia

Como foi solicitado adotar a metodologia de Test-Driven Development (TDD), a nossa dinâmica de desenvolvimento seguiu um fluxo reverso ao tradicional: antes de escrevermos a lógica principal de qualquer um dos cinco problemas, nós elaboramos primeiro os testes. O objetivo era mapear rigorosamente todas as condições, entradas e saídas esperadas para cada problema, assim como foi visto em sala de aula. Apenas após a criação desses testes, iniciamos a etapa de elaboração dos programas em si. Desenvolvemos o código de cada aplicação de forma direcionada, com o propósito de satisfazer as condições estabelecidas e fazer com que todos os testes elaborados anteriormente passassem com sucesso. Essa abordagem garantiu que os desafios propostos fossem cumpridos sem maiores dificuldades.

## Tecnologias Utilizadas

* **Linguagem Orientada a Objetos:** Python
* **Framework de Testes Unitários:** Pytest (versão 7.4.4)

O framework escolhido possui suporte completo aos recursos exigidos pela disciplina:
- Suítes de testes
- Categorias de testes
- Testes parametrizados
- Testes de exceção

## Refatoração (Trabalho Prático 2)

Dando continuidade ao projeto, na Etapa 2 aplicamos técnicas de refatoração para melhorar a estrutura e legibilidade do código, garantindo que os testes continuem passando (barra verde). Como integrantes do **Grupo 2**, realizamos as seguintes operações exigidas:

* **Extrair Método:** Extraímos partes da lógica do método `CuradorDeDados::corresponde_caso2()` para novos métodos privados (`_nomes_invalidos_para_caso2`, `_obter_iniciais_abreviadas_caso2`, `_extrair_iniciais_nome_completo`), aumentando a coesão.
* **Substituir Método por Objeto Método:** A lógica complexa do método `DeduplicadorNomes::deduplicar_caso4()` foi substituída pela instanciação e execução da nova classe `DeduplicacaoCaso4`.
* **Extrair Classe:** A lógica de manipulação e padronização de strings foi extraída da classe `CuradorDeDados` para a nova classe `NormalizadorNomes`.

## Como executar os testes

Siga os passos abaixo para clonar o repositório e executar a suíte de testes:

**1. Na pasta escolhida clone o repositório:**

```bash
git clone https://github.com/JuliaGabP/TPPE_2026.1.git
```

**2. Instale as dependências:**

```bash
pip install pytest
```

**3. Execute os testes**
### na pasta "tests" por caso, onde X é o numero do "caso_X":

```bash
pytest test_caso_X.py -v
```
### na pasta "TPPE_2026.1" todos de uma vez:

```bash
pytest tests/ -v
```

## Testes cobertos

- Caso 1: Diferenças de grafia (tipográficas);
- Caso 2: Sobrenome + Iniciais dos nomes;
- Caso 3: Partículas de e uso de ponto nas abreviações opcionais;
- Caso 4: Iniciais dos nomes agrupadas + sobrenome;
- Caso 5: IDs diferentes para o mesmo autor.
  
## Critérios

* [ ] Aplicação desenvolvida em Linguagem Orientada a Objetos.
* [ ] Framework de testes com suporte a suítes, categorias, testes parametrizados e de exceção.
* [ ] Mínimo de 1 teste para cada um dos 5 casos de deduplicação.
* [ ] Mínimo de 2 conjuntos de dados de teste (cenários) para cada caso.
* [ ] Todos os testes passando (Barra Verde) de forma independente (sem condições de corrida).
* [ ] Nenhuma unidade construída de forma *hard-coded* (falsificada).
