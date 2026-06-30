# Desarrollo de una API REST para gestión de usuarios

La empresa necesita una API REST que gestione la creación, lectura, actualización y eliminación de usuarios. La API debe soportar autenticación JWT y persistir los datos en una base de datos relacional. El dominio es una plataforma de gestión de usuarios para una fintech. Los actores involucrados son el 'administrador de usuarios', el 'motor de autenticación' y la 'base de datos de usuarios'. La operación principal es la gestión de usuarios, con clave 'id de usuario' y modo de falla 'usuario no encontrado'. El umbral numérico del dominio es un throughput de 100 solicitudes por segundo. La razón de negocio es mejorar la eficiencia en la gestión de usuarios.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | api-rest |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de endpoints y modelo de datos

**Objetivo:** Definir los endpoints necesarios para la gestión de usuarios y el modelo de datos correspondiente.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los endpoints necesarios para crear, leer, actualizar y eliminar usuarios.
- Definir el modelo de datos para los usuarios, incluyendo campos como nombre, email, rol y contraseña.
- Asegurar que los endpoints soporten autenticación JWT.

**Entregable:** Documento con la definición de endpoints y modelo de datos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las operaciones CRUD y cómo se mapean a los endpoints.
- Piensa en la estructura de la base de datos y cómo se relaciona con el modelo de datos.

</details>

### Fase 2: Implementación de la autenticación JWT

**Objetivo:** Implementar la autenticación JWT en los endpoints definidos.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar la autenticación JWT en los endpoints.
- Asegurar que los endpoints requieren autenticación para acceder.
- Manejar la generación y verificación de tokens JWT.

**Entregable:** Implementación de la autenticación JWT en los endpoints.

<details>
<summary>Pistas de conocimiento</summary>

- Investiga cómo generar y verificar tokens JWT.
- Considera la seguridad de los tokens y cómo manejarlos.

</details>

### Fase 3: Persistencia de datos en la base de datos

**Objetivo:** Persistir los datos de los usuarios en una base de datos relacional.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar la conexión a la base de datos relacional.
- Implementar las operaciones CRUD en la base de datos.
- Asegurar la consistencia de los datos al persistir y recuperar usuarios.

**Entregable:** Implementación de las operaciones CRUD en la base de datos.

<details>
<summary>Pistas de conocimiento</summary>

- Investiga cómo conectar y realizar operaciones en una base de datos relacional.
- Considera la consistencia de los datos y cómo manejar errores de persistencia.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los endpoints y cómo se relacionan con las operaciones CRUD?
- **paraQueSirve**: ¿Para qué sirve la autenticación JWT en una API REST?
- **comoSeUsa**: ¿Cómo se implementan las operaciones CRUD en una base de datos relacional?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar autenticación JWT y persistencia de datos?

## Criterios de Evaluacion

- Definición correcta de endpoints y modelo de datos.
- Implementación efectiva de la autenticación JWT.
- Persistencia correcta de datos en la base de datos relacional.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
