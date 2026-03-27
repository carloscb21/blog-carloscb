---
name: flujo-git
description: Estandariza la creación de ramas, commits (Conventional Commits) y genera descripciones detalladas y estructuradas para las Pull Requests. Skill global para todos los agentes del equipo.
---

# Skill: Flujo de Trabajo en Git y GitHub

## Contexto
Eres el encargado de gestionar el control de versiones del proyecto "blog-carloscb". Siempre que el usuario te pida subir cambios o generar una PR, debes seguir estrictamente estas reglas.

## Reglas para Ramas
Antes de hacer cualquier commit, crea una rama con este formato:
`feature/<tipo>-<descripcion-corta>`
Ejemplo: `feature/feat-setup-inicial-django`

## Reglas para Commits (Conventional Commits)
Usa siempre español y sigue este formato: `<tipo>: <descripción corta>`

Tipos permitidos:
- `feat:` (Nueva funcionalidad)
- `fix:` (Corrección de un error)
- `docs:` (Cambios solo en documentación)
- `refactor:` (Mejoras de código sin nueva funcionalidad)
- `chore:` (Tareas de mantenimiento, dependencias, configuración)
- `test:` (Añadir o corregir pruebas)

*Ejemplo válido:* `feat: setup inicial del proyecto Django`
*Ejemplo inválido:* `he creado el proyecto`

## Identificación del agente
Antes de hacer el commit, configura siempre el autor como el agente que ejecuta la tarea:
```
git config user.name "gemini_{nombre_agente}"
```

## Verificación de seguridad
Antes de ejecutar `git add .`, verificar que `.env` no está incluido.
Si se detecta, parar inmediatamente y avisar al autor.

## Reglas para Pull Requests
Cuando crees una PR hacia main, el cuerpo debe tener siempre esta estructura:

### ¿Qué hace este PR?
[Explica brevemente los cambios técnicos introducidos]

### ¿Por qué es necesario?
[Explica el motivo técnico o funcional]

### Archivos principales modificados
- [Archivo 1]
- [Archivo 2]

## Reglas generales
- Nunca hacer push directamente a main.
- Nunca incluir `.env` en el commit.
- Si hay dudas sobre el tipo de commit, usar `feat` por defecto.