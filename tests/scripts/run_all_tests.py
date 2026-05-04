#!/usr/bin/env python3
"""
Script de execução completa dos testes de qualidade.
Executa todos os testes do gerador de senhas: funcionais, performance e distribuição.
"""

import sys
import os
import time
import unittest

# Adicionar o diretório raiz ao path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tests.test_password_generator import PasswordGeneratorTests
from tests.test_performance import PerformanceTests
from tests.test_distribution import DistributionTests

def run_all_quality_tests():
    """Executa todos os testes de qualidade."""
    print("🧪 Executando Suite Completa de Testes de Qualidade")
    print("=" * 60)

    start_time = time.time()

    # Criar suite completa
    suite = unittest.TestSuite()

    # Adicionar todos os casos de teste
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PasswordGeneratorTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PerformanceTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(DistributionTests))

    # Executar testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    end_time = time.time()
    execution_time = end_time - start_time

    # Resumo final
    print("\n" + "=" * 60)
    print(f"⏱️  Tempo total de execução: {execution_time:.2f} segundos")

    if result.wasSuccessful():
        print("✅ Todos os testes de qualidade passaram!")
        print(f"📊 Total de testes executados: {result.testsRun}")
        return 0
    else:
        print(f"❌ {len(result.failures)} falhas, {len(result.errors)} erros")
        print(f"📊 Total de testes executados: {result.testsRun}")
        return 1

def run_specific_test_suite(suite_name):
    """Executa uma suite específica de testes."""
    suites = {
        'functional': (PasswordGeneratorTests, "Testes Funcionais"),
        'performance': (PerformanceTests, "Testes de Performance"),
        'distribution': (DistributionTests, "Testes de Distribuição")
    }

    if suite_name not in suites:
        print(f"❌ Suite '{suite_name}' não encontrada. Opções: functional, performance, distribution")
        return 1

    test_class, description = suites[suite_name]
    print(f"🎯 Executando {description}")
    print("=" * 40)

    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print(f"✅ {description} passaram!")
        return 0
    else:
        print(f"❌ {description} falharam")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        suite_name = sys.argv[1]
        exit_code = run_specific_test_suite(suite_name)
    else:
        exit_code = run_all_quality_tests()

    sys.exit(exit_code)