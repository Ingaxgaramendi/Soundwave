def validate_name(name):
    """Valida que el nombre tenga solo letras y sea adecuado."""
    if not name.isalpha():
        print("❌ El nombre o apellido solo puede contener letras.")
        return False
    return True
