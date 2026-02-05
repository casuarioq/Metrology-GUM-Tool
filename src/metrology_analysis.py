Iimport pandas as pd
import numpy as np
import os

class UncertaintyAnalyzer:
    """
    Clase para el procesamiento de datos analíticos y cálculo 
    de incertidumbre Tipo A según la guía GUM.
    """
    
    def __init__(self, file_path):
        """Inicializa la clase cargando el archivo CSV."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encontró el archivo en: {file_path}")
            
        self.df = pd.read_csv(file_path)
        self.values = self.df['Value']
        
    def calculate_statistics(self):
        """Calcula el promedio y la desviación estándar muestral."""
        mean = self.values.mean()
        # ddof=1 asegura que sea desviación estándar muestral (n-1)
        std_dev = self.values.std(ddof=1) 
        n = len(self.values)
        return mean, std_dev, n

    def type_a_uncertainty(self):
        """Calcula la incertidumbre estándar Tipo A (u = s / sqrt(n))."""
        _, std_dev, n = self.calculate_statistics()
        u_a = std_dev / np.sqrt(n)
        return round(u_a, 6)

if __name__ == "__main__":
    # Definimos la ruta relativa: 
    # Desde 'src/', subimos un nivel '..' y entramos a 'data/'
    data_path = os.path.join("..", "data", "raw_weighing_data.csv")
    
    try:
        analyzer = UncertaintyAnalyzer(data_path)
        mean, std, n = analyzer.calculate_statistics()
        u_a = analyzer.type_a_uncertainty()
        
        print("-" * 30)
        print("METROLOGY ANALYSIS REPORT")
        print("-" * 30)
        print(f"Sample size (n):  {n}")
        print(f"Mean (x̄):         {mean:.4f} g")
        print(f"Std Dev (s):      {std:.4f} g")
        print(f"Uncertainty (uA): {u_a:.6f} g")
        print("-" * 30)
        
    except Exception as e:
        print(f"Lamentablemente ocurrió un error: {e}")
