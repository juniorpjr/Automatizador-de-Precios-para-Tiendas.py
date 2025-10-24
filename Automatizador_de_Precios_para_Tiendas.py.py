import pandas as pd
import os
from pathlib import Path

#El Problema: Los dueños de pequeños negocios pierden horas comparando manualmente precios
#de diferentes proveedores en hojas de cálculo, lo que genera ineficiencias, por Juniorp
# script sencillo para automatizar 
def main():
    print("🔄 Iniciando análisis de precios...")
    
    
    carpeta_datos = Path("datos")
    carpeta_resultados = Path("resultados")
    carpeta_resultados.mkdir(exist_ok=True)
    
    
    todos_datos = []
    
    
    for archivo in carpeta_datos.iterdir():
        if archivo.suffix in ['.csv', '.xlsx']:
            print(f"📖 Leyendo {archivo.name}...")
            
            try:
                if archivo.suffix == '.csv':
                    df = pd.read_csv(archivo)
                else:
                    df = pd.read_excel(archivo)
                
               
                df['Proveedor'] = archivo.stem
                todos_datos.append(df)
                
            except Exception as e:
                print(f"❌ Error leyendo {archivo.name}: {e}")
    
    if not todos_datos:
        print("❌ No se encontraron archivos válidos en la carpeta 'datos'")
        return
    
    
    datos_combinados = pd.concat(todos_datos, ignore_index=True)
    
    
    mejores_precios = datos_combinados.loc[datos_combinados.groupby('Producto')['Precio'].idxmin()]
    
    
    mejores_precios = mejores_precios.sort_values('Producto')
    
    
    archivo_resultado = carpeta_resultados / "mejores_precios.xlsx"
    mejores_precios.to_excel(archivo_resultado, index=False)
    
   
    print(f"\n✅ Análisis completado!")
    print(f"📊 Total de productos analizados: {len(mejores_precios)}")
    print(f"💰 Ahorro potencial identificado: ${calcular_ahorro_potencial(datos_combinados, mejores_precios):.2f}")
    print(f"📁 Resultados guardados en: {archivo_resultado}")

def calcular_ahorro_potencial(datos_originales, mejores_precios):
    """Calcula el ahorro potencial comparando con el precio promedio"""
    precio_promedio = datos_originales.groupby('Producto')['Precio'].mean()
    precio_optimo = mejores_precios.set_index('Producto')['Precio']
    
    ahorro = (precio_promedio - precio_optimo).sum()
    return ahorro

if __name__ == "__main__":
    main()
