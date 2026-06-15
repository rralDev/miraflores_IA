# 🏆 Presupuesto Participativo Miraflores 2027 - Plataforma Inteligente

Una plataforma web interactiva y moderna diseñada para modernizar y democratizar el proceso del **Presupuesto Participativo** en la Municipalidad de Miraflores. Integra inteligencia artificial para asistir a los vecinos en la formulación de proyectos técnicos oficiales.

**📺 Mira el Video Tutorial:** [Haz clic aquí para ver cómo funciona el sistema](https://youtu.be/6myr3dVJdIQ)

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

## 📖 Guía de Uso Paso a Paso (Para Demos)

A continuación, se detalla el flujo completo para utilizar la plataforma y demostrar todas sus capacidades:

### 1. Explorar el Radar del Desarrollo
1. Ingresa a la plataforma y dirígete a la pestaña superior **"Radar"**.
2. Observa el mapa interactivo de Miraflores. Puedes hacer clic en las distintas zonas o en los marcadores existentes para ver proyectos previos.
3. Para proponer una idea rápida, haz clic en el botón flotante **"📍 Registrar Idea de Mejora"**. 
4. Aparecerá una ventana modal donde podrás ingresar tu reporte, seleccionar tu zona y detallar el problema. Al guardar, aparecerá un nuevo pin interactivo en el mapa.

### 2. Registrar un Agente Participante (Inscripción)
1. Navega a la pestaña **"Inscripción"**.
2. Llena el formulario simulando ser un representante de una Junta Vecinal o Asociación.
3. Ingresa tu DNI, los datos de la organización y el número de miembros.
4. Sube (o arrastra) archivos simulados para tu "Acta de Constitución" y "DNI".
5. Al enviar, el sistema te mostrará una alerta de éxito simulando que tu organización ha sido acreditada oficialmente.

### 3. Crear un Proyecto con Inteligencia Artificial (Core)
Esta es la función principal de la plataforma. Dirígete a la pestaña **"Crea tu Proyecto"**:

* **Paso 1: Identificación** 
  - Ingresa un DNI de un agente registrado para acceder al sistema. 
  - *Para pruebas, puedes usar el DNI de ejemplo:* `44556677`. Haz clic en **Validar**.
* **Paso 2: Tu Idea** 
  - Escribe en tus propias palabras qué necesita tu cuadra o zona. 
  - *Ejemplo:* "Necesitamos cambiar las tuberías y la matriz de agua y desagüe porque están muy viejas y se filtra el agua." o "Quiero más seguridad, cámaras y serenos contra los robos". Haz clic en **Estructurar con IA**.
* **Paso 3: Formular (Procesamiento)** 
  - El sistema mostrará una animación de carga mientras la "IA" analiza tus palabras clave, detecta el problema y busca la mejor solución técnica.
* **Paso 4: Evidencias** 
  - Haz clic en el mapa interactivo para colocar un pin exactamente donde se necesita la obra.
  - Sube fotos de evidencia (archivos locales) para adjuntarlas al expediente. Haz clic en **Generar Perfil Final**.
* **Paso 5: Resultado y Exportación** 
  - Visualiza en pantalla tu idea transformada en un proyecto técnico con título profesional, alineado a un Objetivo Estratégico (OED), e impactando a una población específica.
  - Haz clic en el botón verde **"📄 Descargar Anexo 05 Oficial"**. El sistema generará instantáneamente un archivo PDF con formato oficial de la Municipalidad, incluyendo el mapa de ubicación, las coordenadas exactas y tus fotos adjuntas.

### 4. Revisar la Transparencia (Muro de Honor)
1. Ve a la pestaña **"Muro de Honor"**.
2. Observa el ranking de organizaciones (con sus medallas).
3. Revisa los avatares de los Héroes de la Transparencia (Comité de Vigilancia).
4. Mira la lista de las asociaciones recientemente inscritas.

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
