#!/usr/bin/env python3
"""
Script de execução dos testes de performance.
Executa os testes de performance do gerador de senhas.
"""

import sys
import os
import unittest

# Adicionar o diretório raiz ao path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tests.test_performance import PerformanceTests

def run_performance_tests():
    """Executa todos os testes de performance."""
    print("🚀 Executando Testes de Performance")
    print("=" * 50)

    # Criar suite de testes
    suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceTests)

    # Executar testes com verbose
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Resumo
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ Todos os testes de performance passaram!")
        return 0
    else:
        print(f"❌ {len(result.failures)} falhas, {len(result.errors)} erros")
        return 1

if __name__ == "__main__":
    exit_code = run_performance_tests()
    sys.exit(exit_code)