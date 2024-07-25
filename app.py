import streamlit as st
import streamlit.components.v1 as components

# Título de la aplicación
st.title('Visualizador de Videos de Redes Sociales')

# HTML para el video de Instagram
instagram_html = """
<div>
  <h2>Video de Instagram</h2>
  <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/C9bXLzlyrbh/?igsh=b2Qxb291N2Uybzcx" data-instgrm-version="13">
    <a href="https://www.instagram.com/reel/C9bXLzlyrbh/?igsh=b2Qxb291N2Uybzcx">Cargar contenido...</a>
  </blockquote>
  <script async src="//www.instagram.com/embed.js"></script>
</div>
"""

# HTML para el video de TikTok
tiktok_html = """
<div>
  <h2>Video de TikTok</h2>
  <blockquote class="tiktok-embed" data-video-id="7368746578238016773" style="max-width: 605px; min-width: 325px">
    <section>...</section>
  </blockquote>
  <script async src="https://www.tiktok.com/embed.js"></script>
</div>
"""

# Usar components.html para insertar el HTML en Streamlit
components.html(instagram_html, height=800)
components.html(tiktok_html, height=800)
