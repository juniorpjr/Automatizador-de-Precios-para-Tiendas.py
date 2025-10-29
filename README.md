🏪 Actualizador de Precios - Venezuela
Solución automatizada para la actualización de precios en bolívares según la tasa del dólar oficial

🌟 Descripción
Este sistema resuelve el problema común en Venezuela de tener que actualizar constantemente los precios de productos debido a la fluctuación del dólar. Combina modo automático (obteniendo la tasa oficial en tiempo real) con modo manual para máxima flexibilidad.

🔥 El Problema
En Venezuela, los comerciantes enfrentan:

📈 Fluctuación constante de la tasa del dólar

⏰ Actualizaciones del BCV a diferentes horas del día

📊 Dificultad para mantener precios actualizados en bolívares

🧮 Cálculos manuales propensos a errores

💡 La Solución
Una herramienta en Python que:

🤖 Obtiene automáticamente la tasa del dólar oficial mediante web scraping

🔧 Permite modo manual para porcentajes personalizados

📁 Genera reportes en Excel listos para usar

📊 Mantiene historial de todos los cambios realizados

🛠 Tecnologías Utilizadas
Python 3 - Lenguaje principal

Selenium - Web scraping para obtener tasa oficial

Pandas - Procesamiento de datos y Excel

Openpyxl - Generación de archivos Excel

📁 Estructura del Proyecto
text
actualizador-precios-venezuela/
├── 📄 actualizador_precios.py     # Programa principal
├── 📄 scraper_dolar.py           # Scraping de tasa oficial
├── 📄 config.json               # Configuraciones
├── 📄 requirements.txt          # Dependencias
├── 📁 datos/
│   ├── 📄 productos_base.csv    # Base de productos (precios en $)
│   └── 📄 historial_cambios.csv # Historial automático
├── 📁 resultados/               # Reportes generados
└── 📁 drivers/                  # ChromeDriver (opcional)
🚀 Instrucciones de Uso
Prerrequisitos
bash
pip install -r requirements.txt
Configuración Inicial
Coloque su archivo productos_base.csv en la carpeta datos/

Asegúrese de tener Chrome instalado

Ejecute: python actualizador_precios.py

Archivo de Productos Base
datos/productos_base.csv

csv
Producto,Precio,Categoria
Arroz,2.50,Alimentos
Harina Pan,1.80,Alimentos
Leche,3.20,Lacteos
Queso,4.50,Lacteos
Pollo,5.00,Carnes
Modos de Operación
1. 🔄 Modo Manual
Aplica un porcentaje fijo a todos los productos

Ideal para ajustes rápidos sin cambiar la tasa

2. 🤖 Modo Automático
Obtiene la tasa oficial automáticamente de la página web

Convierte precios de dólares a bolívares

Opción de agregar porcentaje extra

3. ⚡ Modo Mixto
Elige entre tasa automática o manual

Combina con porcentaje personalizado

Máxima flexibilidad

📊 Resultados Generados
El sistema genera reportes en Excel con:

✅ Precios anteriores y nuevos

✅ Tasa de cambio aplicada

✅ Porcentaje de aumento

✅ Fecha y hora de actualización

✅ Método utilizado

🎯 Beneficios para Negocios
⏰ Ahorra 90% del tiempo en actualizaciones de precios

💰 Evita errores costosos en cálculos manuales

📈 Máxima precisión con tasas en tiempo real

🔄 Flexibilidad total con múltiples modos

📊 Trazabilidad completa con historial de cambios

🔧 Personalización
Puede adaptarse para:

🏪 Diferentes tipos de negocios (abarrotes, ferreterías, etc.)

💸 Múltiples tasas de cambio (parallel, oficial, etc.)

📦 Gestión de inventario avanzada

🌐 Conexión con APIs de proveedores

⚠️ Notas Importantes
Se requiere conexión a internet para el modo automático

El archivo de productos base debe tener precios en dólares

Los resultados se guardan automáticamente en la carpeta resultados/

El historial se mantiene para auditoría y control

👥 Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes ideas para mejorar el sistema, no dudes en crear un "Issue" o "Pull Request".

📄 Licencia
Este proyecto es de código abierto y está disponible bajo la licencia MIT.

¿Problemas o preguntas? Revisa la documentación o crea un issue en el repositorio de GitHub.

¡Optimiza la gestión de precios de tu negocio en Venezuela! 🚀
