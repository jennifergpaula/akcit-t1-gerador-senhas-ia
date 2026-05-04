# Documentação do Projeto: Gerador de Senhas Seguras

## Visão Geral

Este projeto implementa um gerador de senhas seguras em Python com interface de linha de comando (CLI). A aplicação permite gerar senhas aleatórias com critérios configuráveis pelo usuário, incluindo comprimento e inclusão/exclusão de letras maiúsculas, minúsculas, dígitos e símbolos especiais.

## Estrutura do Projeto

- `password_generator.py`
  - Contém a lógica principal de geração de senhas.
  - Utiliza `secrets` para gerar caracteres de forma criptograficamente segura.
  - Garante ao menos um caractere de cada categoria habilitada.

- `cli.py`
  - Interface de linha de comando construída com `argparse`.
  - Expõe opções para personalizar a senha gerada.

- `tests/test_password_generator.py`
  - Casos de teste com `unittest`.
  - Verifica tamanho, critérios de composição, configuração inválida e aleatoriedade básica.

- `README.md`
  - Documentação principal do projeto.
  - Instruções de uso e execução de testes.

## Como Usar

### Executar a CLI

```bash
python cli.py --length 20 --count 3
```

Opções disponíveis:

- `-l`, `--length`: especifica o tamanho da senha. Valor padrão: `16`.
- `-c`, `--count`: quantas senhas gerar. Valor padrão: `1`.
- `--no-upper`: não inclui letras maiúsculas.
- `--no-lower`: não inclui letras minúsculas.
- `--no-digits`: não inclui dígitos.
- `--no-symbols`: não inclui símbolos especiais.

### Exemplo completo

```bash
python cli.py -l 18 --no-symbols
```

Isto gera uma senha de 18 caracteres usando apenas letras e dígitos.

## Como Funciona a Geração de Senhas

1. O usuário define os critérios pela CLI.
2. A função `generate_password` monta os conjuntos de caracteres habilitados.
3. Um caractere de cada conjunto habilitado é incluído para garantir conformidade.
4. Os caracteres restantes são escolhidos aleatoriamente a partir de todos os conjuntos.
5. A lista final é embaralhada e convertida em string.

## Testes

Para rodar os testes:

```bash
python -m unittest discover
```

Os testes cobrem:

- geração de senhas com comprimento padrão e personalizado
- geração com apenas dígitos
- exclusão de símbolos
- tratamento de configuração inválida
- verificação de que múltiplas chamadas produzem senhas diferentes

## Considerações de Segurança

- Uso de `secrets.choice` para garantir geração segura de números aleatórios.
- Símbolos especiais definidos explicitamente para evitar caracteres problemáticos em alguns shells.
- Validação para impedir geração sem nenhum tipo de caractere habilitado.

## Possíveis Extensões Futuras

- Adicionar suporte a caracteres ambíguos removíveis (`O`, `0`, `l`, `1`).
- Criar uma interface web simples em HTML/CSS/JS.
- Adicionar opções de memorabilidade ou frases de senha.
- Exportar senhas geradas para arquivo seguro.
