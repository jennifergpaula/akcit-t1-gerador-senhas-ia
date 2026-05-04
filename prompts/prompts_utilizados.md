# Prompts Utilizados

Este arquivo registra os prompts usados durante o desenvolvimento do projeto.

## Prompt original do usuário

- Criar um gerador de senhas seguras com base em critérios definidos pelo usuário (tamanho, caracteres especiais, números, letras maiúsculas/minúsculas).
- Implementação em Python ou JavaScript, com CLI ou web simples.
- Aplicar IA generativa no desenvolvimento: lógica de geração, testes, interface CLI/HTML.

## Prompts de Desenvolvimento

### Implementação Inicial
- Criar a lógica de geração de senhas em `password_generator.py`
- Implementar função `generate_password` com parâmetros configuráveis
- Usar `secrets` para geração criptograficamente segura
- Criar função de validação `validate_password`

### Interface CLI
- Criar `cli.py` com `argparse` para processar argumentos
- Implementar opções: `--length`, `--count`, `--no-upper`, `--no-lower`, `--no-digits`, `--no-symbols`
- Adicionar validação de entrada e tratamento de erros

### Testes
- Criar `tests/test_password_generator.py` com casos de teste
- Testar geração padrão, comprimento personalizado, critérios específicos
- Verificar tratamento de configurações inválidas
- Testar aleatoriedade entre múltiplas gerações

### Documentação
- Criar pasta `docs/` com `documentacao.md`
- Documentar estrutura do projeto, uso, funcionamento e extensões futuras
- Atualizar `README.md` com informações da documentação

### Controle de Versão
- Fazer commit explicando implementação inicial
- Fazer novo commit incluindo documentação
- Salvar mudanças no Git

### Qualidade e Testes
- Executar testes automatizados como analista de qualidade
- Salvar resultado dos testes em `tests/documento_test/resultado_testes.md`
- Verificar cobertura de testes e funcionamento correto

### Melhorias Visuais
- Atualizar README com informações da documentação
- Deixar README atrativo visualmente com badges, emojis, tabelas
- Adicionar diagramas, exemplos organizados e seções bem estruturadas

### Registro de Prompts
- Criar pasta `prompts/` com `prompts_utilizados.md`
- Registrar todos os prompts utilizados durante o desenvolvimento

## Observações

A pasta `prompts/` foi criada para manter esses registros organizados e permitir referência futura às instruções de desenvolvimento. Este documento serve como histórico completo das interações e decisões tomadas durante o desenvolvimento do projeto de gerador de senhas seguras.