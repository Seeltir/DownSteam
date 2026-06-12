# 🎮 Steam Services Monitor Bot

<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjc0cXo0eWhiZmY4eTZ2d3pkcWVhYTBpbG5wNWMwNTYyaTZwODd0ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Oj8pUuT5FOpxHH9LIk/giphy.gif" width="400" alt="Steam Status Bot">
</p>

Un bot de Discord automatizado y modular (basado en Cogs) escrito en Python que monitorea el estado en tiempo real de los servicios principales de la API de Valve (Steam). Diseñado para alertar de forma visual e inmediata mediante Embeds enriquecidos con GIFs dinámicos cuando ocurre una caída o inestabilidad global.

---

## 🚀 Características Principales

* **Monitoreo en Segundo Plano:** Tarea asíncrona optimizada (`tasks.loop`) que consulta la API de Valve cada 5 minutos.
* **Control de Estado Inteligente:** Evita el spam en los canales de chat; solo envía notificaciones cuando detecta un cambio real en el estado del servidor (Estable ↔ Caído).
* **Diseño Visual Atractivo:** Alertas estructuradas mediante `discord.Embed` con códigos de colores semánticos (Rojo para caídas, Verde para recuperaciones) y miniaturas animadas (GIFs).
* **Arquitectura Limpia:** Estructura basada en *Cogs* y gestión de variables mediante entornos seguros para producción (`.env`).

---

## 📁 Arquitectura del Proyecto

```text
BOT_STEAM_DOWN/
├── cogs/
│   └── monitor_steam.py   # Lógica interna y monitoreo de la API de Valve
├── .env                   # Variables de entorno y credenciales (Ignorado en Git)
├── main.py                # Punto de entrada principal y carga asíncrona del Bot
├── README.md              # Documentación del sistema
└── run_bot.vbs            # Script de inicialización invisible para Windows
```

---

## 🛠️ Requisitos e Instalación

**1. Clonar y preparar las dependencias**
Instala los paquetes necesarios en tu entorno local utilizando pip:
```bash
pip install discord.py aiohttp python-dotenv
```
**2. Variables de Entorno (.env)**
Crea un archivo llamado exactamente .env en la raíz del proyecto y configura tus credenciales secretas extraídas de los portales de desarrollo de Discord y Steam:
```bash
DISCORD_TOKEN=Tu_Token_Secreto_De_Discord_Aqui
STEAM_API_KEY=Tu_Clave_De_La_API_De_Steam_Aqui
```
**3. ID del Canal de Alertas**
En el archivo cogs/monitor_steam.py, actualiza la constante CANAL_ALERTAS_ID con el ID del canal de texto de tu servidor donde deseas recibir los reportes:
```bash
CANAL_ALERTAS_ID = 123456789012345678  
```

---

## 🖥️ Ejecución en Segundo Plano (Windows)
Para mantener el bot vigilando 24/7 sin lidiar con molestas ventanas de la consola de comandos (cmd.exe) abiertas en tu pantalla mientras juegas o trabajas, el proyecto incluye un script de automatización nativo de Windows.

## El Script: run_bot.vbs
El archivo contiene una directiva en Visual Basic Script que invoca al intérprete de Python de forma silenciosa e invisible en el background del sistema operativo:
```bash
CreateObject("Wscript.Shell").Run "cmd /c python main.py", 0, True
```

## 🏃‍♂️ Cómo Utilizarlo:
Encender el Bot de forma invisible: Simplemente haz doble clic sobre el archivo run_bot.vbs. El bot se conectará a Discord inmediatamente en segundo plano sin levantar ninguna ventana en tu barra de tareas.

Cómo verificar que está corriendo: Verás al bot En línea en tu servidor de Discord y procesando los logs internamente.

**Cómo apagar el Bot:**

-Abre el Administrador de Tareas de Windows (Ctrl + Shift + Esc).
-Busca en la lista de procesos en segundo plano el nombre Python.
-Dale clic derecho y selecciona Finalizar tarea.