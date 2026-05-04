# 🔐 Gerador de Senhas Seguras

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> Um gerador de senhas aleatórias e seguras em Python com interface de linha de comando (CLI). Personalize o tamanho, os tipos de caracteres e gere múltiplas senhas com segurança criptográfica.

---

## ✨ Visão Geral

Este projeto implementa um gerador de senhas seguras que permite personalizar completamente os critérios de geração:

- 🎯 **Tamanho configurável** - de 4 a milhões de caracteres
- 🔤 **Tipos de caracteres** - maiúsculas, minúsculas, dígitos e símbolos
- 🔐 **Segurança criptográfica** - utiliza `secrets` para geração segura
- ⚡ **Múltiplas senhas** - gere várias de uma vez
- ✅ **Totalmente testado** - 6 testes de cobertura

---

## 🚀 Começar Rapidamente

```bash
# Gerar uma senha padrão (16 caracteres)
python cli.py

# Gerar senha com 20 caracteres
python cli.py --length 20

# Gerar 5 senhas de 18 caracteres
python cli.py -l 18 -c 5
```

---

## 📦 Tecnologias

| Ferramenta | Descrição |
|-----------|-----------|
| **Python 3** | Linguagem de programação |
| **argparse** | Processamento de argumentos CLI |
| **secrets** | Geração criptograficamente segura |
| **unittest** | Framework de testes |

---

## 📁 Estrutura do Projeto

```
.
├── 🔧 password_generator.py    # Motor de geração de senhas
├── 💻 cli.py                   # Interface de linha de comando
├── 📋 README.md                # Este arquivo
├── tests/
│   ├── test_password_generator.py  # Testes automatizados
│   └── documento_test/             # Relatórios de teste
├── docs/
│   └── documentacao.md         # Documentação técnica completa
└── prompts/
    └── prompts_utilizados.md   # Prompts do desenvolvimento
```

---

## 🎮 Como Usar

### Opções Disponíveis

| Opção | Descrição | Padrão |
|-------|-----------|--------|
| `-l, --length` | Tamanho da senha | 16 |
| `-c, --count` | Quantas senhas gerar | 1 |
| `--no-upper` | Remover maiúsculas | ❌ |
| `--no-lower` | Remover minúsculas | ❌ |
| `--no-digits` | Remover dígitos | ❌ |
| `--no-symbols` | Remover símbolos | ❌ |

### Exemplos de Uso

#### 📌 Exemplo 1: Senha Padrão
```bash
python cli.py
# Resultado: jK9@mP2xL$qR4vW!nT
```

#### 📌 Exemplo 2: Senha Mais Longa
```bash
python cli.py --length 32
# Resultado: aB3#cD5%eF7&gH9*iJ1@kL2!mN4$oP6
```

#### 📌 Exemplo 3: Múltiplas Senhas
```bash
python cli.py -c 3 -l 20
# Resultado: 3 senhas diferentes de 20 caracteres
```

#### 📌 Exemplo 4: Apenas Letras e Números
```bash
python cli.py -l 16 --no-symbols
# Resultado: aB3cDeFgHiJkLmNo
```

#### 📌 Exemplo 5: Números Apenas
```bash
python cli.py --no-upper --no-lower --no-symbols -l 8
# Resultado: 48291647
```

---

## 🔍 Como Funciona

```
┌─────────────────────────────────────────────────────────┐
│ 1️⃣  Usuário define critérios pela CLI                   │
├─────────────────────────────────────────────────────────┤
│ 2️⃣  password_generator monta conjuntos de caracteres    │
├─────────────────────────────────────────────────────────┤
│ 3️⃣  Inclui um caractere de cada tipo habilitado         │
├─────────────────────────────────────────────────────────┤
│ 4️⃣  Preenche o restante aleatoriamente                  │
├─────────────────────────────────────────────────────────┤
│ 5️⃣  Embaralha a lista final                             │
├─────────────────────────────────────────────────────────┤
│ 6️⃣  Retorna a senha segura                              │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ Testes

### Executar os Testes

```bash
python -m unittest tests.test_password_generator
```

### Resultado Esperado

```
......
------
Ran 6 tests in 0.006s
OK
```

### Cobertura de Testes

- ✓ Geração com comprimento padrão (16 caracteres)
- ✓ Geração com comprimento personalizado
- ✓ Geração apenas com dígitos
- ✓ Exclusão de símbolos especiais
- ✓ Tratamento de configurações inválidas
- ✓ Verificação de aleatoriedade entre gerações

---

## 🔒 Segurança

### Por que `secrets` é importante?

```python
# ❌ NÃO USAR - Inseguro
import random
random.choice(caracteres)  # Previsível

# ✅ USAR - Seguro
import secrets
secrets.choice(caracteres)  # Criptograficamente seguro
```

### Práticas de Segurança Implementadas

- 🔐 Uso de `secrets.choice` para geração criptograficamente segura
- 📋 Símbolos especiais definidos explicitamente (sem caracteres problemáticos)
- ✔️ Validação de entrada para evitar configurações inválidas
- 🎲 Embaralhamento adicional com `SystemRandom` para melhor distribuição

---

## 🚀 Possíveis Extensões Futuras

- [ ] 🌐 Interface web em HTML/CSS/JS
- [ ] 📱 Suporte para mobile
- [ ] 🎨 Tema dark/light customizável
- [ ] 💾 Exportar senhas para arquivo seguro
- [ ] 🔤 Remover caracteres ambíguos (O, 0, l, 1)
- [ ] 📝 Gerador de frases de senha
- [ ] 🔌 API REST
- [ ] 🌍 Suporte a múltiplos idiomas

---

## 📚 Documentação

- 📖 [Documentação Técnica Completa](docs/documentacao.md)
- 📋 [Prompts Utilizados](prompts/prompts_utilizados.md)
- 🧪 [Resultados dos Testes](tests/documento_test/resultado_testes.md)

---

## 📝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👤 Autor

Desenvolvido como projeto educacional para aplicação de IA generativa em desenvolvimento Python.

---

<div align="center">

### ⭐ Se este projeto foi útil, considere deixar uma estrela!

**Gerador de Senhas Seguras | Python | CLI | Segurança**

</div>
