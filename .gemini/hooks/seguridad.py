<<<<<<< HEAD
import sys
import json

ARCHIVOS_PROHIBIDOS = [
    ".env",
    "settings.json",
    "GITHUB_PERSONAL_ACCESS_TOKEN",
    ".pem",
    ".key",
]

def main():
    try:
        input_data = sys.stdin.read()
        if not input_data:
            sys.exit(0)

        data = json.loads(input_data)
        args = str(data.get("tool_args", {}))

        for archivo in ARCHIVOS_PROHIBIDOS:
            if archivo in args:
                print(
                    f"ACCESO DENEGADO por el Hook de Seguridad: "
                    f"intento de acceso a '{archivo}' bloqueado.",
                    file=sys.stderr
                )
                sys.exit(2)

        sys.exit(0)

    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()