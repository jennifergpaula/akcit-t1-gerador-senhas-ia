import argparse

from password_generator import generate_password


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gerador de senhas seguras com opções de tamanho e tipos de caracteres."
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="Tamanho da senha (padrão: 16).",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Quantas senhas gerar (padrão: 1).",
    )
    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Não incluir letras maiúsculas.",
    )
    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Não incluir letras minúsculas.",
    )
    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Não incluir dígitos.",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Não incluir símbolos especiais.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.count < 1:
        raise SystemExit("O número de senhas deve ser ao menos 1.")

    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols

    try:
        for _ in range(args.count):
            print(
                generate_password(
                    length=args.length,
                    use_upper=use_upper,
                    use_lower=use_lower,
                    use_digits=use_digits,
                    use_symbols=use_symbols,
                )
            )
    except ValueError as error:
        raise SystemExit(error)


if __name__ == "__main__":
    main()
