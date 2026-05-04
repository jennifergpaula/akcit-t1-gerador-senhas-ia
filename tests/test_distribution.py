import collections
import unittest
from password_generator import generate_password


class DistributionTests(unittest.TestCase):
    """Testes de distribuição estatística para o gerador de senhas."""

    def test_character_distribution_balance(self):
        """Testa se os caracteres são distribuídos de forma equilibrada."""
        num_samples = 1000
        password_length = 20

        # Coletar estatísticas de caracteres
        all_chars = []
        passwords = []

        for _ in range(num_samples):
            password = generate_password(length=password_length)
            passwords.append(password)
            all_chars.extend(password)

        # Contar frequência de cada tipo de caractere
        upper_count = sum(1 for c in all_chars if c.isupper())
        lower_count = sum(1 for c in all_chars if c.islower())
        digit_count = sum(1 for c in all_chars if c.isdigit())
        symbol_count = sum(1 for c in all_chars if c in "!@#$%^&*()-_=+[]{}|;:,.<>?/")

        total_chars = len(all_chars)

        # Verificar que cada tipo aparece pelo menos 15% das vezes (mais realista)
        min_percentage = 0.15

        upper_pct = upper_count / total_chars
        lower_pct = lower_count / total_chars
        digit_pct = digit_count / total_chars
        symbol_pct = symbol_count / total_chars

        self.assertGreater(upper_pct, min_percentage,
                          f"Maiúsculas insuficientes: {upper_pct:.1%}")
        self.assertGreater(lower_pct, min_percentage,
                          f"Minúsculas insuficientes: {lower_pct:.1%}")
        self.assertGreater(digit_pct, min_percentage,
                          f"Dígitos insuficientes: {digit_pct:.1%}")
        self.assertGreater(symbol_pct, min_percentage,
                          f"Símbolos insuficientes: {symbol_pct:.1%}")

        # Verificar que nenhum tipo domina excessivamente (máximo 35%)
        max_percentage = 0.35

        self.assertLess(upper_pct, max_percentage,
                       f"Maiúsculas excessivas: {upper_pct:.1%}")
        self.assertLess(lower_pct, max_percentage,
                       f"Minúsculas excessivas: {lower_pct:.1%}")
        self.assertLess(digit_pct, max_percentage,
                       f"Dígitos excessivos: {digit_pct:.1%}")
        self.assertLess(symbol_pct, max_percentage,
                       f"Símbolos excessivos: {symbol_pct:.1%}")

        print(f"✅ Distribution test passed:")
        print(f"   Upper: {upper_count} ({upper_pct:.1%})")
        print(f"   Lower: {lower_count} ({lower_pct:.1%})")
        print(f"   Digits: {digit_count} ({digit_pct:.1%})")
        print(f"   Symbols: {symbol_count} ({symbol_pct:.1%})")

    def test_entropy_calculation(self):
        """Testa o cálculo de entropia das senhas geradas."""
        import math

        password = generate_password(length=16)

        # Calcular entropia baseada nos tipos de caracteres
        char_sets = [
            set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # 26 maiúsculas
            set("abcdefghijklmnopqrstuvwxyz"),  # 26 minúsculas
            set("0123456789"),                  # 10 dígitos
            set("!@#$%^&*()-_=+[]{}|;:,.<>?/") # 27 símbolos
        ]

        # Contar quantos conjuntos estão sendo usados
        used_sets = 0
        total_possible_chars = 0

        for char_set in char_sets:
            if any(c in char_set for c in password):
                used_sets += 1
                total_possible_chars += len(char_set)

        # Calcular entropia teórica
        if total_possible_chars > 0:
            entropy_bits = len(password) * math.log2(total_possible_chars)
        else:
            entropy_bits = 0

        # Verificar que a entropia é adequada (> 80 bits para senha de 16 chars)
        self.assertGreater(entropy_bits, 80,
                          f"Entropia insuficiente: {entropy_bits:.1f} bits")

        # Verificar que pelo menos 3 tipos de caracteres são usados
        self.assertGreaterEqual(used_sets, 3,
                               f"Caracter types insuficientes: {used_sets}/4")

        print(f"✅ Entropy test passed: {entropy_bits:.1f} bits, {used_sets} character types")

    def test_no_repeating_patterns(self):
        """Testa que não há padrões repetitivos óbvios nas senhas."""
        num_samples = 100
        password_length = 20

        passwords = [generate_password(length=password_length) for _ in range(num_samples)]

        # Verificar que não há senhas idênticas
        unique_passwords = set(passwords)
        self.assertEqual(len(unique_passwords), len(passwords),
                        "Encontradas senhas duplicadas")

        # Verificar distribuição de caracteres individuais
        for password in passwords:
            char_counts = collections.Counter(password)

            # Nenhum caractere deve aparecer mais de 40% da senha
            max_count = max(char_counts.values())
            max_percentage = max_count / len(password) * 100

            self.assertLessEqual(max_percentage, 40,
                               f"Caractere repetido excessivamente: {max_percentage:.1f}%")

        print(f"✅ Pattern test passed: {len(unique_passwords)} unique passwords, no excessive repetition")


if __name__ == "__main__":
    unittest.main()