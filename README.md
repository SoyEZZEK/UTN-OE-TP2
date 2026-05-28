# TP2 - Gestión Colaborativa, Control de Versiones y Organización Empresarial

## Descripción
Trabajo Práctico 2 de la cátedra Organización Empresarial — UTN TUPaD (2026).

Implementación de un flujo de trabajo colaborativo completo utilizando Git, GitHub y Jira,
aplicado al análisis de datos de ventas de una pequeña empresa (Escenario B).
El proyecto simula una célula ágil de desarrollo con tres roles diferenciados:
líder organizador (Hugo), desarrollador técnico (Paco) y revisor QA (Luis).

## Integrantes (rol, nombre y responsabilidad)

| P1 - Hugo | Lautaro Pérez | Inicialización del repositorio y estructura del proyecto |
| P2 - Paco | Lautaro Pérez | Desarrollo del script de análisis de ventas |
| P3 - Luis | Lautaro Pérez | Revisión de código, documentación y Pull Request |

## Escenario elegido
**Escenario B — Análisis de Ventas de una Pequeña Empresa**

Análisis de un conjunto de datos simulados de ventas comerciales para generar
indicadores básicos que permitan interpretar el desempeño de la empresa.

## Dataset utilizado
- **Nombre:** Sales Dataset (ventas simuladas)
- **Fuente:** https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6
- **Formato:** CSV
- **Columnas principales:** `id`, `sales_date`, `sales_amount`
- **Descripción:** Registros diarios de ventas con fecha y monto de cada transacción.

## Estructura del proyecto
UTN-OE-TP2/
├── datos/
│   └── dataset.csv              <- Dataset de ventas en formato CSV
├── scripts/
│   └── analisis_ventas.py       <- Script Python de análisis
├── resultados/
│   └── grafico_ventas.png       <- Gráfico de evolución temporal generado
├── README.md
└── .gitignore

## Requisitos
- Python 3.x
- Librerías: `pandas`, `matplotlib`

Para instalar las dependencias:
```bash
pip install pandas matplotlib
```

## Instrucciones para ejecutar
1. Abrir Google Colab: https://colab.research.google.com
2. Clonar el repositorio:
```bash
   git clone https://github.com/SoyEZZEK/UTN-OE-TP2.git
```
3. Navegar a la carpeta del proyecto:
```bash
   cd UTN-OE-TP2
```
4. Ejecutar el script de análisis:
```bash
   python scripts/analisis_ventas.py
```
5. El gráfico generado se guardará automáticamente en `/resultados/grafico_ventas.png`.

## Gestión del proyecto
Las tareas fueron organizadas y trazadas mediante **Jira** (ID de proyecto: `TP2OE`).
Cada commit en este repositorio incluye el ID del Issue correspondiente
para garantizar la trazabilidad entre el código y la planificación.

## Tecnologías utilizadas
- **Git** — Control de versiones
- **GitHub** — Repositorio remoto y revisión colaborativa (Pull Requests)
- **Google Colab** — Entorno de ejecución en la nube
- **Jira** — Gestión de tareas y trazabilidad
- **Python** — Lenguaje de análisis de datos
