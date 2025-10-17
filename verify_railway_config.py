#!/usr/bin/env python
"""
Script para verificar que el backend está listo para Railway.
Ejecuta este script antes de hacer deploy para asegurarte de que todo está configurado.
"""

import os
import sys
from pathlib import Path

# Colores para terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def check_file_exists(filename, required=True):
    """Verifica si un archivo existe."""
    exists = Path(filename).exists()
    status = f"{GREEN}[OK]{RESET}" if exists else f"{RED}[X]{RESET}"
    req_text = "OBLIGATORIO" if required else "RECOMENDADO"
    
    print(f"{status} {filename} - {'Encontrado' if exists else 'NO encontrado'} ({req_text})")
    
    if not exists and required:
        return False
    return True

def check_file_contains(filename, search_text, description):
    """Verifica si un archivo contiene cierto texto."""
    try:
        # Intentar leer con diferentes encodings
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    content = f.read()
                    found = search_text in content
                    status = f"{GREEN}[OK]{RESET}" if found else f"{RED}[X]{RESET}"
                    print(f"{status} {description}")
                    return found
            except UnicodeDecodeError:
                continue
        print(f"{RED}[X]{RESET} {description} - Error de encoding")
        return False
    except FileNotFoundError:
        print(f"{RED}[X]{RESET} {description} - Archivo no encontrado")
        return False

def main():
    print("=" * 60)
    print("VERIFICANDO CONFIGURACION PARA RAILWAY")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # 1. Verificar archivos necesarios
    print("Verificando archivos...")
    all_ok &= check_file_exists("requirements.txt", required=True)
    all_ok &= check_file_exists("Procfile", required=True)
    all_ok &= check_file_exists("railway.json", required=False)
    all_ok &= check_file_exists("runtime.txt", required=False)
    all_ok &= check_file_exists("maps_backend/settings.py", required=True)
    all_ok &= check_file_exists("manage.py", required=True)
    all_ok &= check_file_exists(".gitignore", required=True)
    print()
    
    # 2. Verificar dependencias en requirements.txt
    print("Verificando dependencias...")
    all_ok &= check_file_contains("requirements.txt", "gunicorn", "gunicorn instalado")
    all_ok &= check_file_contains("requirements.txt", "psycopg2", "psycopg2-binary instalado")
    all_ok &= check_file_contains("requirements.txt", "whitenoise", "whitenoise instalado")
    all_ok &= check_file_contains("requirements.txt", "dj-database-url", "dj-database-url instalado")
    all_ok &= check_file_contains("requirements.txt", "Django", "Django instalado")
    all_ok &= check_file_contains("requirements.txt", "djangorestframework", "DRF instalado")
    all_ok &= check_file_contains("requirements.txt", "django-cors-headers", "django-cors-headers instalado")
    print()
    
    # 3. Verificar Procfile
    print("Verificando Procfile...")
    all_ok &= check_file_contains("Procfile", "gunicorn", "Procfile contiene gunicorn")
    all_ok &= check_file_contains("Procfile", "maps_backend.wsgi", "Procfile apunta a maps_backend.wsgi")
    print()
    
    # 4. Verificar settings.py
    print("Verificando settings.py...")
    all_ok &= check_file_contains("maps_backend/settings.py", "import os", "Importa os")
    all_ok &= check_file_contains("maps_backend/settings.py", "import dj_database_url", "Importa dj_database_url")
    all_ok &= check_file_contains("maps_backend/settings.py", "whitenoise", "WhiteNoise configurado")
    all_ok &= check_file_contains("maps_backend/settings.py", "DATABASE_URL", "Usa DATABASE_URL")
    all_ok &= check_file_contains("maps_backend/settings.py", "os.environ.get", "Lee variables de entorno")
    print()
    
    # 5. Verificar .gitignore
    print("Verificando .gitignore...")
    all_ok &= check_file_contains(".gitignore", "venv/", ".gitignore excluye venv/")
    all_ok &= check_file_contains(".gitignore", ".env", ".gitignore excluye .env")
    all_ok &= check_file_contains(".gitignore", "db.sqlite3", ".gitignore excluye db.sqlite3")
    all_ok &= check_file_contains(".gitignore", "__pycache__", ".gitignore excluye __pycache__")
    print()
    
    # 6. Verificar que archivos sensibles NO estén
    print("Verificando que archivos sensibles no existan...")
    venv_not_exists = not Path("venv").exists()
    env_not_exists = not Path(".env").exists()
    db_not_exists = not Path("db.sqlite3").exists()
    
    status_venv = f"{GREEN}[OK]{RESET}" if venv_not_exists else f"{YELLOW}[WARN]{RESET}"
    status_env = f"{GREEN}[OK]{RESET}" if env_not_exists else f"{YELLOW}[WARN]{RESET}"
    status_db = f"{GREEN}[OK]{RESET}" if db_not_exists else f"{YELLOW}[WARN]{RESET}"
    
    print(f"{status_venv} venv/ {'no existe (OK)' if venv_not_exists else 'existe (asegurate de que este en .gitignore)'}")
    print(f"{status_env} .env {'no existe (OK)' if env_not_exists else 'existe (asegurate de que este en .gitignore)'}")
    print(f"{status_db} db.sqlite3 {'no existe (OK)' if db_not_exists else 'existe (asegurate de que este en .gitignore)'}")
    print()
    
    # Resultado final
    print("=" * 60)
    if all_ok:
        print(f"{GREEN}TODO LISTO PARA RAILWAY!{RESET}")
        print()
        print("Proximos pasos:")
        print("1. git add .")
        print("2. git commit -m 'Configuracion para Railway'")
        print("3. git push origin main")
        print("4. Desplegar en Railway siguiendo RAILWAY_QUICKSTART.md")
    else:
        print(f"{RED}HAY ERRORES QUE CORREGIR{RESET}")
        print()
        print("Revisa los archivos marcados con X y corrigelos.")
        print("Consulta RAILWAY_FILES.md para mas informacion.")
    print("=" * 60)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

