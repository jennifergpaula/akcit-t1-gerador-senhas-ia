import time
import unittest
from password_generator import generate_password


class PerformanceTests(unittest.TestCase):
    """Testes de performance para o gerador de senhas."""

    def test_generate_many_passwords_performance(self):
        """Testa a geração de 1000 senhas em tempo aceitável."""
        num_passwords = 1000
        password_length = 16

        start_time = time.time()
        passwords = [generate_password(length=password_length) for _ in range(num_passwords)]
        end_time = time.time()

        execution_time = end_time - start_time

        # Verificar que todas as senhas foram geradas
        self.assertEqual(len(passwords), num_passwords)

        # Verificar que todas as senhas têm o tamanho correto
        for password in passwords:
            self.assertEqual(len(password), password_length)

        # Verificar que todas as senhas são únicas
        unique_passwords = set(passwords)
        self.assertEqual(len(unique_passwords), num_passwords)

        # Verificar tempo de execução (deve ser menor que 1 segundo para 1000 senhas)
        self.assertLess(execution_time, 1.0, f"Geração de {num_passwords} senhas demorou {execution_time:.2f}s")

        print(f"✅ Performance test passed: {num_passwords} passwords generated in {execution_time:.4f} seconds")

    def test_generate_large_passwords_performance(self):
        """Testa a geração de senhas muito grandes."""
        large_lengths = [100, 500, 1000]

        for length in large_lengths:
            with self.subTest(length=length):
                start_time = time.time()
                password = generate_password(length=length)
                end_time = time.time()

                execution_time = end_time - start_time

                # Verificar tamanho
                self.assertEqual(len(password), length)

                # Verificar que contém todos os tipos de caracteres
                has_upper = any(c.isupper() for c in password)
                has_lower = any(c.islower() for c in password)
                has_digit = any(c.isdigit() for c in password)
                has_symbol = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password)

                self.assertTrue(has_upper, f"Senha de {length} caracteres não contém maiúscula")
                self.assertTrue(has_lower, f"Senha de {length} caracteres não contém minúscula")
                self.assertTrue(has_digit, f"Senha de {length} caracteres não contém dígito")
                self.assertTrue(has_symbol, f"Senha de {length} caracteres não contém símbolo")

                # Tempo aceitável (menos de 0.1s para senhas grandes)
                self.assertLess(execution_time, 0.1, f"Senha de {length} caracteres demorou {execution_time:.4f}s")

                print(f"✅ Large password test passed: {length} chars generated in {execution_time:.6f} seconds")


if __name__ == "__main__":
    unittest.main()