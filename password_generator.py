import secrets
import string


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure password based on user-selected criteria."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not pools:
        raise ValueError("At least one character type must be enabled.")

    # Guarantee inclusion of at least one character from each enabled pool.
    password_chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)

    remaining = length - len(password_chars)
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def validate_password(
    password: str,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> bool:
    """Check that password matches the requested category requirements."""
    if use_upper and not any(c.isupper() for c in password):
        return False
    if use_lower and not any(c.islower() for c in password):
        return False
    if use_digits and not any(c.isdigit() for c in password):
        return False
    if use_symbols and not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password):
        return False

    return True
