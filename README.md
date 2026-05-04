# akcit-t1-gerador-senhas-ia

Um gerador de senhas seguras em Python com interface de linha de comando.

## Tecnologias

- Python 3
- Biblioteca padrão: `argparse`, `secrets`, `string`
- Testes com `unittest`

## Uso

Executar a CLI:

```bash
python cli.py --length 20 --count 3
```

Opções principais:

- `-l`, `--length`: tamanho da senha (padrão: 16)
- `-c`, `--count`: quantas senhas gerar (padrão: 1)
- `--no-upper`: remove letras maiúsculas
- `--no-lower`: remove letras minúsculas
- `--no-digits`: remove dígitos
- `--no-symbols`: remove símbolos especiais

Exemplo:

```bash
python cli.py -l 18 --no-symbols
```

## Testes

Executar todos os testes:

```bash
python -m unittest discover
```
