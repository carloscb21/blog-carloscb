# GEMINI.md - Contexto del Proyecto blog-carloscb

Este archivo sirve como guía fundamental para los agentes de Gemini CLI que trabajen en este repositorio.

## Descripción del Proyecto
`blog-carloscb` es un experimento técnico de automatización pura. El objetivo es desarrollar un blog completo utilizando **Python y Django** de forma autónoma, donde cada etapa del ciclo de vida (desarrollo, despliegue, mantenimiento) es gestionada por agentes de IA a través de **Gemini CLI**.

## Arquitectura y Tecnologías
- **Framework:** Django + Django REST Framework.
- **Base de Datos:**
  - Local: PostgreSQL corriendo en contenedor Docker.
  - Producción: Neon PostgreSQL (Serverless).
- **Infraestructura y Hosting:** Render.com.
- **Almacenamiento de Imágenes:** Cloudflare R2.
- **Analítica:** Google Analytics 4.
- **Metodología:** Desarrollo basado en especificaciones de agentes (Agent Specs).

## Estado Actual
La estructura base del proyecto Django está creada y validada en local. PostgreSQL Docker conectado y funcionando. Listo para iniciar el desarrollo de modelos y API REST.

## Convenciones de Desarrollo
- **Agentes Especializados:** El desarrollo se guía por roles específicos. Cada agente consulta su propio spec en `.gemini/specs/`.
- **Mariete:** Responsable del backend, infraestructura y GA4. Su especificación está en `.gemini/specs/mariete.md`.
- **Artur:** Responsable del frontend, templates y sistema visual. Su especificación está en `.gemini/specs/artur.md`.
- **Ramitos:** Responsable del contenido y redacción. Su especificación está en `.gemini/specs/ramitos.md`.
- **Estructura de Archivos:**
  - `manage.py`: Punto de entrada de Django.
  - `carloscb/`: Directorio principal (settings divididos en base, development, production).
  - `blog/`, `projects/`, `pages/`, `api/`: Aplicaciones Django modulares.
  - `.gemini/specs/`: System prompts de cada agente.
  - `.gemini/skills/`: Skills reutilizables globales.
  - `.gemini/hooks/`: Hooks de seguridad y automatización.
- **Seguimiento:**
  - `notas.txt`: Registro de dificultades y soluciones técnicas.
  - `notas-tiempos.txt`: Registro del tiempo invertido en el proyecto.

## Guía de Comandos
- **Python:** 3.12.9. Nunca usar versiones anteriores.
- **Entorno Virtual:** Ya existe un `.venv` con Python 3.12.9. No crear uno nuevo.
- **Instalación:** `pip install -r requirements.txt`
- **Ejecución Local:** `python manage.py runserver`
- **Migraciones:** `python manage.py makemigrations` y `python manage.py migrate`
- **Tests:** `python manage.py test`

## Actualización del contexto
Cuando edites este archivo, ejecuta `/memory refresh` para que los agentes recarguen el contexto sin reiniciar la sesión.

## Seguridad y variables de entorno
- El archivo `.env` contiene credenciales sensibles. **Ningún agente debe leer, modificar ni mostrar su contenido nunca.**
- Las variables de entorno se cargan a través de `config/os_system.py`. Usar siempre ese archivo para acceder a configuraciones sensibles.
- El `.env` debe estar siempre en `.gitignore`. Nunca hacer commit de este archivo.
- El `.env.example` contiene las claves necesarias sin valores reales. Es el único archivo de entorno que se puede leer y commitear.
- El hook `.gemini/hooks/seguridad.py` bloquea automáticamente cualquier intento de acceso a archivos sensibles (`.env`, `settings.json`, claves privadas).

## Skills globales
- **`.gemini/skills/flujo_git/SKILL.md`:** Estandariza ramas, commits (Conventional Commits) y PRs. Úsala cuando Carlos diga "sube los cambios y genera la PR".

## Agentes del equipo

| Agente | Rol |
|--------|-----|
| Mariete | Desarrollador — backend, infraestructura y GA4 |
| Artur | Diseñador — frontend, templates y sistema visual |
| Ramitos | Redactor — creación y edición de contenido |
| Copito | Editor Jefe — estrategia editorial |
| Seyan | SEO — metadatos y posicionamiento |
| Champi | Community Manager — redes sociales |
| Javi | Analista — Google Analytics 4 e informes para Copito |

## Instrucciones para los agentes

### Mariete
1. Consulta `.gemini/specs/mariete.md` antes de actuar.
2. Valida la conectividad a BD local (Docker) antes de migraciones.
3. No toques HTML/CSS salvo para integrar scripts técnicos como GA4.
4. Nunca leas ni modifiques `.env` ni `settings.json`.

### Artur
1. Consulta `.gemini/specs/artur.md` antes de actuar.
2. No toques archivos Python ni lógica de negocio.
3. Respeta siempre el sistema de diseño definido en el spec.
4. Nunca uses frameworks CSS externos (Bootstrap, Tailwind, etc.).

### Ramitos
1. Consulta `.gemini/specs/ramitos.md` antes de actuar.
2. Escribe siempre con la voz de Carlos, no con voz propia.
3. Entrega el contenido en Markdown listo para publicar.

### Copito
1. Consulta `.gemini/specs/copito.md` antes de actuar.
2. Basa las decisiones editoriales en los datos que te pase Javi.
3. No generes contenido, solo decide y organiza.

### Seyan
1. Consulta `.gemini/specs/seyan.md` antes de actuar.
2. Actúa siempre tras la publicación de un artículo nuevo.
3. No modifiques el contenido del artículo, solo sus metadatos.

### Champi
1. Consulta `.gemini/specs/champi.md` antes de actuar.
2. Adapta el tono a cada red social, nunca copies el mismo texto.
3. Presenta siempre los posts al autor antes de publicar.

### Javi
1. Consulta `.gemini/specs/javi.md` antes de actuar.
2. Solo lees e interpretas datos, no tomas decisiones editoriales.
3. Tu output siempre va dirigido a Copito.
