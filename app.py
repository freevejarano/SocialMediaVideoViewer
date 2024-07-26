import streamlit as st
import streamlit.components.v1 as components
import re
import csv

# Configuración de la página
st.set_page_config(
    page_title="Viernes de Memes",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

def get_instagram_block(url):
    # HTML para el video de Instagram
    instagram_html = f"""
    <style>
    .instagram-block {{
        border: 2px solid #1430d1;
        border-radius: 10px;
        padding: 15px;
        background-color: #F8F8F8;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .instagram-block h2 {{
        font-size: 20px;
        color: #1430d1;
    }}
    </style>
    <div class="instagram-block">
    <center>
    <h2>Video de Instagram</h2>
    <blockquote class="instagram-media" data-instgrm-permalink="{url}" data-instgrm-version="13">
        <a href="{url}">Cargar contenido...</a>
    </blockquote>
    </center>
    <script async src="//www.instagram.com/embed.js"></script>
    </div>
    """
    return instagram_html

def get_tiktok_block(url):
    # Expresión regular para capturar el ID del video
    pattern = r"/video/(\d+)"

    # Buscar el ID del video
    match = re.search(pattern, url)

    if not match:
        print("No se encontró el ID del video")
        return None
    
    video_id = match.group(1)

    # HTML para el video de TikTok
    tiktok_html = f"""
    <style>
    .tiktok-block {{
        border: 2px solid #1430d1;
        border-radius: 10px;
        padding: 15px;
        background-color: #F8F8F8;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .tiktok-block h2 {{
        font-size: 20px;
        color: #1430d1;
    }}
    </style>
    <div class="tiktok-block">
    <center>
    <h2>Video de TikTok</h2>
    <blockquote class="tiktok-embed" data-video-id="{video_id}" style="max-width: 605px; min-width: 325px">
        <section>...</section>
    </blockquote>
    </center>
    <script async src="https://www.tiktok.com/embed.js"></script>
    </div>
    """
    return tiktok_html

# Guardar la url de un video en el csv
def save_video(url, red_social, autor):
    with open('videos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["\n"+url, red_social, autor])


def main():
    # Título de la aplicación
    st.title('Visualizador de Videos de Redes Sociales: Viernes de Memes AWS re/Start Generation 🎥')

    # Ingresa el URL de un video de Instagram
    nuevo = st.text_input('Ingresa el URL de un video de Instagram o TikTok')

    # Ingresa el autor del video
    autor = st.text_input('Ingresa el autor del video')

    # Botón de guardar
    if st.button("Guardar", key='submit', help='Haga clic aquí para guardar'):
        if not nuevo:
            st.warning('Debes ingresar una URL')
        elif not autor:
            st.warning('Debes ingresar el autor del video')
        elif 'instagram' in nuevo:
            save_video(nuevo, 'instagram', autor)
            st.success("Datos guardados correctamente")
        elif 'tiktok' in nuevo:
            save_video(nuevo, 'tiktok', autor)
            st.success("Datos guardados correctamente")
        else:
            st.warning('El URL no es de Instagram o TikTok')

    # Leer archivo de csv con las URLs
    videos = []
    with open('videos.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row:
                videos.append(row)


    # Obtener los bloques de video
    for video in videos:
        if video['red_social'] == 'instagram':
            instagram_html = get_instagram_block(video['url'])
            video['html'] = instagram_html
        elif video['red_social'] == 'tiktok':
            tiktok_html = get_tiktok_block(video['url'])
            video['html'] = tiktok_html


    # Mostar los videos en la aplicación
    for video in videos:
        st.markdown(f"### Video de {video['red_social']} Gracias a {video['autor']}")
        components.html(video['html'], height=800)


# Ejecutar la aplicación
main()