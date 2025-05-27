import os
import tarfile
import glob

def comprimir_csv_a_targz(carpeta):

    # Verificar si la carpeta existe
    if not os.path.isdir(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return
    
    # Buscar todos los archivos CSV en la carpeta
    archivos_csv = glob.glob(os.path.join(carpeta, "*.csv"))
    
    if not archivos_csv:
        print(f"No se encontraron archivos CSV en '{carpeta}'.")
        return
    
    # Procesar cada archivo CSV
    for csv_path in archivos_csv:
        # Crear el nombre del archivo comprimido (mismo nombre pero con .tar.gz)
        tar_path = f"{csv_path}.tar.gz"
        
        try:
            # Crear el archivo tar.gz
            with tarfile.open(tar_path, "w:gz") as tar:
                tar.add(csv_path, arcname=os.path.basename(csv_path))
            
            # Verificar que el archivo comprimido se creó correctamente
            if os.path.exists(tar_path):
                # Eliminar el CSV original
                os.remove(csv_path)
                print(f"Comprimido: {csv_path} -> {tar_path} (y eliminado original)")
            else:
                print(f"Error: No se pudo crear {tar_path}")
                
        except Exception as e:
            print(f"Error al procesar {csv_path}: {str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Uso: python3 comprimir_csv.py <carpeta_con_csv>")
        sys.exit(1)
    
    carpeta = sys.argv[1]
    comprimir_csv_a_targz(carpeta)