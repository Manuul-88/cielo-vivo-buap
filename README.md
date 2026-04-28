Cielo Vivo BUAP

Simulación interactiva del cielo nocturno basada en datos reales + creación de planetas personalizados en un universo colectivo.

Descripción

Cielo Vivo BUAP es una experiencia interactiva desarrollada para la Noche de las Estrellas en la BUAP.

El sistema permite:

Visualizar el cielo nocturno desde Puebla en una fecha específica
Explorar constelaciones y planetas visibles
Crear planetas personalizados
Agregar esos planetas a un universo colectivo en tiempo real
Visualizar planetas en modo holograma
Al final del evento, el sistema muestra un universo lleno de planetas creados por los asistentes.

Concepto

Ciencia (cielo real)
Interacción (creación de planetas)
Experiencia (universo colectivo)
Impacto visual (holograma)
Funcionalidades principales
Cielo real (constelaciones y planetas)
Creador de planetas personalizados
Universo colectivo en tiempo real
Modo holograma (visualización física)

Estructura del proyecto
cielo-vivo-buap/
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   ├── modules/
│   │   ├── api.js
│   │   ├── planetCreator.js
│   │   ├── collectiveUniverse.js
│   │   ├── hologramMode.js
│   │   └── skyRenderer.js
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routes/
│       └── planets.py
│
└── data/
    ├── stars.json
    ├── constellations.json
    └── event_sky.json
Tecnologías

Frontend:
HTML, CSS, JavaScript
Canvas / Three.js

Backend:
Python
FastAPI

Base de datos:
SQLite (inicial)
Escalable a PostgreSQL / Supabase

Equipo
Manuel → Backend, lógica principal, integración
Geovanni → Base de datos y datos astronómicos
Jovan → Frontend y renderizado visual
Audrey → UI/UX y presentación

Instalación
1. Clonar repositorio
git clone https://github.com/TU-USUARIO/cielo-vivo-buap.git
cd cielo-vivo-buap
2. Abrir en VS Code
code .

Flujo de trabajo
Antes de trabajar:
git pull origin main
Después de trabajar:
git add .
git commit -m "Descripción de cambios"
git push origin main
Cómo funciona el sistema
El usuario abre la aplicación
Puede explorar el cielo real
Puede crear un planeta personalizado
El planeta se envía al backend
Se guarda en la base de datos
El universo colectivo obtiene todos los planetas
Se renderizan en pantalla en tiempo real
Opcional: se visualizan en modo holograma

Objetivo del proyecto
Crear una experiencia interactiva que combine ciencia y creatividad, donde cada usuario deje una huella en un universo digital compartido.

Reglas del equipo
Hacer git pull antes de trabajar
No modificar archivos de otros sin avisar
Hacer commits claros
Mantener el código limpio

Estado del proyecto
En desarrollo
