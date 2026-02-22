import ast
import sys
import pathlib
from loguru import logger

def verify_ast(file_path: pathlib.Path) -> bool:
    """Verifica el AST del archivo en busca de funciones peligrosas."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ["eval", "exec"]:
                        logger.error(f"Fallo de seguridad: Uso de {node.func.id} detectado en {file_path}")
                        return False
        return True
    except Exception as e:
        logger.error(f"Error parseando {file_path}: {e}")
        return False

if __name__ == "__main__":
    logger.add(sys.stderr, level="DEBUG")
    success = True
    for p in pathlib.Path("src").rglob("*.py"):
        if not verify_ast(p):
            success = False
    sys.exit(0 if success else 1)
