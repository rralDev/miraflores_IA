# 🏆 Presupuesto Participativo Miraflores 2027 - Plataforma Inteligente

Una plataforma web interactiva y moderna diseñada para modernizar y democratizar el proceso del **Presupuesto Participativo** en la Municipalidad de Miraflores. Integra inteligencia artificial para asistir a los vecinos en la formulación de proyectos técnicos oficiales.

## 🚀 Características Principales

La aplicación se divide en 4 módulos clave:

1. **🗺️ Radar del Desarrollo (Mapa Interactivo)**
   - Visualización geoespacial de la problemática del distrito usando `Leaflet` y mapas base de OpenStreetMap / CartoDB.
   - Los vecinos pueden reportar incidencias o proponer mejoras colocando un pin directamente en su zona.

2. **📝 Inscripción de Agentes Participantes**
   - Interfaz de registro para organizaciones civiles y juntas vecinales.
   - Validación de datos (DNI, Acta de Constitución) para acreditar a los agentes oficiales con voz y voto.

3. **🤖 Crea tu Proyecto con IA (Generador Automático)**
   - **Paso 1:** Validación de identidad usando un DNI registrado (ej. `44556677`).
   - **Paso 2:** El vecino redacta su idea de mejora en lenguaje coloquial.
   - **Paso 3:** Un motor de **Procesamiento de Lenguaje Natural (NLP)** simulado en JavaScript analiza las palabras clave y traduce la idea en un proyecto técnico estructurado.
   - **Paso 4:** Se alinea automáticamente el proyecto con los Objetivos Estratégicos de Desarrollo (OED) de Miraflores.
   - **Paso 5:** Generación y descarga automática del **Anexo N° 05 Oficial en formato PDF**, listo para ser firmado e ingresado a mesa de partes.

4. **🎖️ Muro de Honor**
   - Sección de gamificación y transparencia.
   - Ranking de las organizaciones vecinales con más proyectos priorizados.
   - Presentación del Comité de Vigilancia elegido democráticamente.

## 🛠️ Tecnologías Utilizadas

Este prototipo fue construido pensando en la agilidad y el despliegue inmediato. Es un proyecto **100% Frontend** (no requiere servidor de base de datos pesado para las demostraciones):

* **Estructura y Estilos:** HTML5, CSS3, Bootstrap 5.
* **Lógica e Inteligencia Artificial:** JavaScript (Vanilla JS). El motor de IA opera en el cliente usando expresiones regulares complejas y diccionarios de datos estructurados.
* **Mapas:** Leaflet.js con tiles de OpenStreetMap y CartoDB Voyager.
* **Generación de Documentos:** `jsPDF` y `html2canvas` para renderizar el PDF en tiempo real.
* **Iconografía y Avatares:** FontAwesome, ui-avatars y randomuser.me.

## ⚙️ Cómo Ejecutar el Proyecto (Local)

Al ser una aplicación estática, la ejecución es sumamente sencilla:

1. Clona o descarga este repositorio.
2. Abre el archivo `index.html` en cualquier navegador web moderno (Chrome, Edge, Firefox, Safari).
3. ¡Listo! La plataforma funcionará completamente sin configuraciones adicionales.

## 🌐 Despliegue en Vivo

El proyecto está preparado para ser desplegado instantáneamente en servicios estáticos como **GitHub Pages**, **Netlify** o **Vercel**. 
Simplemente enlaza la rama `master` o `main` a la plataforma de hosting de tu preferencia y la aplicación estará en vivo.

---
*Desarrollado para la Hackatón de Innovación Tecnológica.*
