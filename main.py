import streamlit as st
import pandas as pd
from loguru import logger
import sys
from pathlib import Path
import sqlite3
from datetime import datetime

# Importar lógica de base de datos
sys.path.append(str(Path(__file__).parent))
from database.db_manager import init_db, DB_PATH

# Configuración de Loguru siguiendo estándar CONF23
logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("social_hub.log", level="INFO", format="{time} {level} {message}", serialize=True)

# Configuración de la página
st.set_page_config(
    page_title="🛡️ Social Hub - Red Social Segura",
    page_icon="🕸️",
    layout="wide",C:\_CONFIANZA23\PRODUCTOS\25 SOCIAL_HUB
    initial_sidebar_state="expanded"
)

# Estilos Premium (Glassmorphism & Dark Mode)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .stButton>button {
        border-radius: 20px;
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .post-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .user-info {
        font-weight: bold;
        color: #00d2ff;
    }
    .timestamp {
        font-size: 0.8rem;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabecera Global
col_logo, col_text = st.columns([1, 5])
with col_logo:
    st.image("assets/logo.jpg", width=80)
with col_text:
    st.title("Social Hub")

# Inicializar DB
if 'db_ready' not in st.session_state:
    init_db()
    st.session_state.db_ready = True

# Lógica de Datos
def get_posts():
    with sqlite3.connect(DB_PATH) as conn:
        query = """
            SELECT p.id, u.username, p.content, p.created_at, 
            (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as likes
            FROM posts p
            JOIN users u ON p.user_id = u.id
            ORDER BY p.created_at DESC
        """
        return pd.read_sql_query(query, conn)

def create_post(user_id, content):
    if len(content) > 280:
        st.error("El post supera los 280 caracteres.")
        return False
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (user_id, content))
            conn.commit()
            logger.success(f"Post creado por usuario {user_id}")
            return True
    except Exception as e:
        logger.error(f"Error al crear post: {e}")
        return False

# UI - Sidebar
with st.sidebar:
    st.title("🛡️ Social Hub")
    st.markdown("---")
    st.write("Bienvenido, **admin**")
    st.image("assets/logo.jpg", width=150)
    
    st.markdown("---")
    menu = st.radio("Navegación", ["Timeline", "Perfil", "Tendencias", "Configuración"])
    
    st.markdown("---")
    st.info("Estatus: Protegido por CONF23-SDLC")

# UI - Main Content
if menu == "Timeline":
    st.title("🚀 Timeline")
    
    # Crear Post
    with st.expander("✨ ¿Qué estás pensando?", expanded=True):
        new_post_content = st.text_area("Máximo 280 caracteres", height=100, max_chars=280)
        if st.button("Publicar 🚀"):
            if new_post_content:
                if create_post(1, new_post_content):
                    st.toast("Publicado con éxito!", icon='✅')
                    st.rerun()
            else:
                st.warning("El post no puede estar vacío.")

    # Mostrar Posts
    posts = get_posts()
    
    if posts.empty:
        st.write("No hay publicaciones todavía. ¡Sé el primero!")
    else:
        for index, row in posts.iterrows():
            st.markdown(f"""
                <div class="post-card">
                    <span class="user-info">@{row['username']}</span> · 
                    <span class="timestamp">{row['created_at']}</span>
                    <p style="font-size: 1.2rem; margin-top: 10px;">{row['content']}</p>
                    <div style="display: flex; gap: 20px; align-items: center;">
                        <span>❤️ {row['likes']} Likes</span>
                        <span>💬 0 Comentarios</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                if st.button(f"❤️##{row['id']}", key=f"like_{row['id']}"):
                    # Lógica de like simplificada
                    with sqlite3.connect(DB_PATH) as conn:
                        cursor = conn.cursor()
                        try:
                            cursor.execute("INSERT OR IGNORE INTO likes (post_id, user_id) VALUES (?, ?)", (row['id'], 1))
                            conn.commit()
                            st.rerun()
                        except: pass

elif menu == "Perfil":
    st.title("👤 Mi Perfil")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/logo.jpg", width=150)
    with col2:
        st.subheader("admin")
        st.write("Bio: Administrador del sistema Social Hub. Apasionado por la seguridad y el código limpio.")
        st.write("📍 Ciudad: Madrid, España")
        st.write("🔗 Web: confi23.tech")

elif menu == "Tendencias":
    st.title("🔥 Tendencias")
    st.write("Lo más hablado en Social Hub...")
    st.info("#Confianza23")
    st.info("#SecureCoding")
    st.info("#SocialHubLaunch")

elif menu == "Configuración":
    st.title("⚙️ Configuración")
    st.write("Ajustes de privacidad y cuenta.")
    st.toggle("Modo Privado")
    st.toggle("Notificaciones de Desktop")
    st.button("Cerrar Sesión")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Social Hub v1.0 | 🛡️ Secure by Design | © 2026 CONFIANZA23</p>", unsafe_allow_html=True)
