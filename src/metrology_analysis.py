import pandas as pd
import numpy as np

class UncertaintyAnalyzer:
    """Clase para el cálculo de incertidumbre Tipo A según la GUM."""
    
    def __init__(self, file_path):
        # Cargamos los datos crudos
        self.df = pd.read_csv(file_path)
        self.values = self.df['Value']
        
    def calculate_statistics(self):
        """Calcula promedio y desviación estándar muestral."""
        mean = self.values.mean()
        std_dev = self.values.std(ddof=1) 
        n = len(self.values)
        return mean, std_dev, n

    def type_a_uncertainty(self):
        """Calcula la incertidumbre estándar (u)."""
        _, std_dev, n = self.calculate_statistics()
        u_a = std_dev / np.sqrt(n)
        return round(u_a, 6)

if __name__ == "__main__":
    # Ruta relativa al archivo de datos
    analyzer = UncertaintyAnalyzer("raw_weighing_data.csv")
    print(f"Average: {analyzer.calculate_statistics()[0]} g")
    print(f"Type A Uncertainty: {analyzer.type_a_uncertainty()} g")
