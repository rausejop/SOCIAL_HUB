"""
Módulo de gestión de base de datos SQLite para Social Hub.
Sigue el estándar Google-style docstrings y principios de seguridad CONF23.
"""

import sqlite3
from pathlib import Path
from loguru import logger

# Ruta a la base de datos
DB_PATH = Path(__file__).parent.parent / "social_hub.db"

def init_db():
    """Inicializa la base de datos y crea las tablas necesarias."""
    logger.info(f"Inicializando base de datos en {DB_PATH}")
    
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Tabla de Usuarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    bio TEXT,
                    avatar TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabla de Posts
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Tabla de Likes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS likes (
                    post_id INTEGER,
                    user_id INTEGER,
                    PRIMARY KEY (post_id, user_id),
                    FOREIGN KEY (post_id) REFERENCES posts (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Tabla de Comentarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    post_id INTEGER,
                    user_id INTEGER,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (post_id) REFERENCES posts (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Insertar un usuario de prueba si no existe
            cursor.execute("SELECT id FROM users WHERE username = ?", ("admin",))
            if not cursor.fetchone():
                cursor.execute("INSERT INTO users (username, bio) VALUES (?, ?)", 
                             ("admin", "Administrador de Social Hub"))
            
            conn.commit()
            logger.success("Base de datos inicializada correctamente.")
            
    except sqlite3.Error as e:
        logger.error(f"Error al inicializar la base de datos: {e}")
        raise

if __name__ == "__main__":
    init_db()
