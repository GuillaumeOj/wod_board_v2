TRUE_VALUES = ["true", "1"]
FALSE_VALUES = ["false", "0"]


def str_to_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in TRUE_VALUES:
        return True

    if value.lower() in FALSE_VALUES:
        return False

    raise ValueError(f"{value} is not a known value")
