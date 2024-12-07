# nextcalc
## Implementacion de Calculadora para SO

Esta es la version de la calculadora para Sistemas Operativos, Diseñada por Najash y Desarrollada por la comunidad.

# Licencia de Uso
 Esta Calculadora esta bajo la licencia GNU y es abierta al publico desarrollador para mejoras e implementacion.

## Lenguaje de Programacion y Herramientas Utilzadas.
EL Lenguaje usado es Python, usando como editor Visual Studio Code

# Estructura del Proyecto
nextcalc/
│── README.md              # Documentación principal del proyecto
│── requirements.txt       # Dependencias del proyecto
│── main.py                # Archivo principal que ejecuta la calculadora
│── setup.py               # Configuración para empaquetar el proyecto (opcional)
│── .gitignore             # Archivos y carpetas a ignorar por Git
│── assets/                # Archivos estáticos (imágenes, íconos, etc.)
│   └── logo.png
│── nextcalc/              # Módulo principal de la calculadora
│   │── __init__.py        # Marca el directorio como un paquete
│   │── ui.py              # Interfaz de usuario (Tkinter)
│   │── logic.py           # Lógica de la calculadora
│   │── config.py          # Configuración y constantes (colores, tamaños, etc.)
│   └── utils.py           # Funciones auxiliares
└── tests/                 # Pruebas unitarias
    └── test_logic.py      # Pruebas de la lógica de cálculo
