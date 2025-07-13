# Inflabot 🛒📈

**Inflabot** es una herramienta que genera métricas de inflación a partir de datos obtenidos mediante **scraping de supermercados online**.  
El objetivo es construir reportes periódicos que reflejen la evolución de precios, su distribución y la variación por categorías de productos.

---

## 🚀 Características principales

- Obtención de datos de precios desde supermercados online.
- Generación de métricas y reportes de inflación:
- Distribución de precios por categorías.
- Variación semanal de precios por tipo de artículos.
- Creación automática de páginas HTML con resultados.
- Actualización del **índice (`index.html`)** para navegar los reportes generados.
- Arquitectura modular y extensible:
- **Dominio** → entidades e interfaces de casos de uso.  
- **Aplicación** → implementación de casos de uso (métricas, reportes).  
- **Infraestructura** → conexión con PostgreSQL y repositorios.  

---

## 📂 Estructura del proyecto

```
inflabot/
├── application/              # Casos de uso (métricas y generación de reportes)
├── domain/                   # Entidades e interfaces del dominio
├── infraestructure/          # Repositorios y modelos de base de datos
├── config.py                 # Configuración general (paths, logging, etc.)
├── main.py                   # Punto de entrada principal
└── README.md                 # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.10+  
- PostgreSQL en ejecución con los datos de posteos cargados  
- Dependencias instaladas (ver `requirements.txt` si está disponible)

Ejemplo de instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

El script principal es `main.py`.  
Cuenta con un **CLI** que permite crear páginas para un posteo y actualizar el índice.

### Crear la página de un posteo específico
```bash
python main.py crear_pagina -i <UUID_DEL_POSTEO>
```

Esto:
1. Obtiene el posteo desde la base de datos PostgreSQL.  
2. Genera la página HTML con las métricas correspondientes.  
3. Guarda el archivo en la carpeta de salida (`OUTPUT_DIR/posts/`).  
4. Actualiza el `index.html` con el nuevo posteo.  

Ejemplo:
```bash
python main.py crear_pagina -i 123e4567-e89b-12d3-a456-426614174000
```

---

## 🛠️ Configuración

La configuración se define en `config.py`. Algunos parámetros importantes:

- `OUTPUT_DIR`: Carpeta donde se guardan los reportes (`/posts/` e `index.html`).
- `TITLE`: Nombre de la aplicación para logs.
- `LOG_LEVEL`: Nivel de logging (`INFO`, `DEBUG`, etc.).

---

## 📊 Ejemplo de salida

- Página HTML con métricas de distribución de precios por categorías.
- Página HTML con variación semanal de precios por artículos.
- Índice HTML navegable con todos los reportes generados.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Podés proponer nuevas métricas, optimizar el scraping o mejorar la visualización de reportes.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
Consultá el archivo `LICENSE` para más detalles.
