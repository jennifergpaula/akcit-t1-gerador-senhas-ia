import unittest

from password_generator import generate_password, validate_password


class PasswordGeneratorTests(unittest.TestCase):
    def test_generate_default_password(self):
        password = generate_password()
        self.assertEqual(len(password), 16)
        self.assertTrue(validate_password(password))

    def test_generate_custom_length(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)
        self.assertTrue(validate_password(password))

    def test_generate_only_digits(self):
        password = generate_password(use_upper=False, use_lower=False, use_digits=True, use_symbols=False, length=10)
        self.assertEqual(len(password), 10)
        self.assertTrue(password.isdigit())

    def test_generate_no_symbols(self):
        password = generate_password(use_upper=True, use_lower=True, use_digits=True, use_symbols=False, length=12)
        self.assertTrue(validate_password(password, use_symbols=False))
        self.assertFalse(any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password))

    def test_generate_invalid_configuration(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

    def test_randomness_with_multiple_calls(self):
        passwords = {generate_password() for _ in range(10)}
        self.assertEqual(len(passwords), 10)


if __name__ == "__main__":
    unittest.main()
