import sqlite3
from flask_bcrypt import Bcrypt

# Configuración inicial
bcrypt = Bcrypt()

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            username TEXT NOT NULL,
            is_verified INTEGER NOT NULL DEFAULT 0
        )
    ''')

    # Crear tabla de minutas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS minutes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    """Genera un hash seguro para la contraseña."""
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hash_password, password):
    """Verifica la contraseña."""
    return bcrypt.check_password_hash(hash_password, password)

if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada.")
