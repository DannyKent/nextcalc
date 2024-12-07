
# **NextCalc**  
**Versión:** 1.0  
Desarrollado por: **Danny Villarreal (Najash Code)**  

## **Descripción**  
NextCalc es una calculadora moderna y funcional desarrollada en Python con la biblioteca Tkinter. Su interfaz está inspirada en el diseño minimalista y cuenta con funcionalidades básicas y avanzadas, como cálculos matemáticos y un menú interactivo.  

---

## **Estructura del Proyecto**  
```
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
```

---

## **Instalación**  
### **Requisitos Previos:**  
- Python 3.x  
- Tkinter (preinstalado con Python)  

### **Paso 1: Clonar el Repositorio**  
```bash
git clone https://github.com/tuusuario/nextcalc.git
cd nextcalc
```

### **Paso 2: Crear un Entorno Virtual (opcional)**  
```bash
python -m venv venv
source venv/bin/activate  # En Unix/Mac
venv\Scripts\activate     # En Windows
```

### **Paso 3: Instalar Dependencias**  
```bash
pip install -r requirements.txt
```

### **Paso 4: Ejecutar la Calculadora**  
```bash
python main.py
```

---

## **Características**  
- Interfaz inspirada en la funcionalidad y belleza combinada  
- Cálculos básicos (+, -, *, /, %).  
- Interfaz personalizable con menú interactivo.  
- Ventana centrada automáticamente.  

---

## **Contribución**  
¿Tienes ideas para mejorar NextCalc? ¡Cualquier contribución es bienvenida! Haz un fork, crea una nueva rama y envía tu PR.  

---

## **Licencia**  
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.  


---

## **Nuevos Desafios** 
A partir de aqui, se comienzan a desarrollar las ideas, a agregar funcionalidades al programa y a implementarlo en versiones de SO