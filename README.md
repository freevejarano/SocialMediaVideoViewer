# 🎥 Visualizador de Videos de Redes Sociales para AWS re/Start

Este repositorio contiene el código fuente para una aplicación de Streamlit que permite visualizar videos de Instagram y TikTok. Este proyecto es un ejemplo de referencia desarrollado como parte del material didáctico para el curso de AWS re/Start.

## 📋 Descripción

La aplicación desarrollada utiliza Streamlit para crear una interfaz de usuario sencilla que permite a los usuarios ingresar URLs de videos de Instagram y TikTok y visualizarlos directamente en la página. Este ejemplo utiliza HTML y scripts incrustados para cargar los videos, similar a cómo se harían en un sitio web estándar.

## 🚀 Uso

Para ejecutar esta aplicación, sigue los pasos a continuación:

1. Clona este repositorio en tu máquina local:

```
git clone https://github.com/freevejarano/SocialMediaVideoViewer.git
```

```
cd SocialMediaVideoViewer
```

2. Asegúrate de tener Python y Streamlit instalados. Si no, puedes instalar Streamlit y agregar los requerimientos necesarios usando:

```
pip install -r requirements.txt
```

3. Navega al directorio del proyecto y ejecuta la aplicación:

```
streamlit run app.py
```

## 🛠️ Configuración

En el código, puedes ajustar las URLs incrustadas para los videos de Instagram y TikTok modificando las variables `instagram_html` y `tiktok_html` en el archivo `app.py`.

## 📖 Referencia

Este proyecto es solo un ejemplo para fines educativos en el curso de AWS re/Start y no debe considerarse como una solución de producción. Se recomienda revisar y ajustar el código según las necesidades específicas del proyecto y las políticas de seguridad pertinentes.


# Desafío de Programación: Creación de una Aplicación Web para Visualización de Videos de Redes Sociales

## 🎓 Curso: AWS re/Start

## 📈 Contexto del Problema
Los estudiantes del curso AWS re/Start suelen compartir entre sí videos de TikTok e Instagram como una forma de entretenimiento. Sin embargo, actualmente necesitan abrir cada enlace individualmente para poder ver los videos, lo que puede ser tedioso y poco eficiente. Para resolver esta situación y mejorar la experiencia de usuario, se ha planteado el desarrollo de una solución más integrada y accesible.

## 🛠️ Herramienta de Desarrollo
Se utilizará Python con Streamlit para desarrollar una aplicación web. Streamlit es una herramienta poderosa que permite construir rápidamente aplicaciones web interactivas y atractivas para visualizar datos y contenido multimedia.

## 📌 Descripción de la Tarea
El objetivo es desarrollar una aplicación que permita a los usuarios:
- Subir enlaces de videos de Instagram y TikTok.
- Visualizar estos videos directamente dentro de la aplicación sin necesidad de abrir cada enlace por separado.

## 🚀 Instrucciones
1. **Diseño del Boceto**: Antes de comenzar a programar, desarrollen un boceto de la interfaz de usuario utilizando herramientas como Figma o Canva. Esto les ayudará a visualizar la disposición de los elementos en la aplicación y garantizar una experiencia de usuario coherente y atractiva.
2. **Reflexión sobre la Estructura**: Reflexionen sobre cómo estructurarían la aplicación para manejar las URLs y la visualización de videos. Consideren la lógica necesaria para extraer y gestionar los enlaces de manera eficiente.
3. **Desarrollo de la Interfaz**: Consideren qué elementos de interfaz son necesarios para una experiencia de usuario fluida y atractiva. Incluyan funcionalidades que mejoren la interacción del usuario con la aplicación.
4. **Prototipo Inicial y Pruebas**: Desarrollen un prototipo inicial que puedan mejorar iterativamente. Realicen pruebas para asegurarse de que la aplicación funciona correctamente y es intuitiva de usar.

## 📓 [Documentación de Streamlit](https://docs.streamlit.io/)

Este ejercicio es una oportunidad para innovar y crear una herramienta que no solo resuelva un problema, sino que también sea fácil de usar y visualmente atractiva. ¡Buena suerte!
