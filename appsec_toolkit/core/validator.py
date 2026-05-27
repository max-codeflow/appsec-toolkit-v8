import importlib


REQUIRED_MODULES = [
    "appsec_toolkit.modules.headers",
    "appsec_toolkit.modules.jwt",
    "appsec_toolkit.modules.secrets",
    "appsec_toolkit.modules.xss",
    "appsec_toolkit.modules.sqli",
]


def validate_modules():
    print("[*] Validating modules...")

    valid = []
    invalid = []

    for module_path in REQUIRED_MODULES:
        try:
            module = importlib.import_module(module_path)

            # derive expected function name
            func_name = "check_" + module_path.split(".")[-1]

            if not hasattr(module, func_name):
                raise Exception(f"Missing {func_name}")

            valid.append(module_path)
            print(f"[OK] {module_path}")

        except Exception as e:
            invalid.append((module_path, str(e)))
            print(f"[WARN] {module_path} -> {e}")

    return valid, invalid
