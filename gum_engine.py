import numpy as np

def calculate_combined_uncertainty(uncertainties):
    """
    Calculates the combined standard uncertainty for independent variables
    based on the GUM (Guide to the Expression of Uncertainty in Measurement).
    """
    return np.sqrt(np.sum(np.square(uncertainties)))

def calculate_expanded_uncertainty(combined_u, k=2):
    """
    Calculates the expanded uncertainty for a specific coverage factor (default k=2 for ~95%).
    """
    return combined_u * k

if __name__ == "__main__":
    print("--- Metrology GUM Tool: Uncertainty Calculator ---")
    
    # Example: Uncertainties from calibration, repeatability, and resolution
    # Data in units (e.g., mg or mL)
    u_calibration = 0.05
    u_repeatability = 0.02
    u_resolution = 0.01
    
    u_list = [u_calibration, u_repeatability, u_resolution]
    
    uc = calculate_combined_uncertainty(u_list)
    u_expanded = calculate_expanded_uncertainty(uc)
    
    print(f"Combined Uncertainty (uc): {uc:.4f}")
    print(f"Expanded Uncertainty (U) [k=2]: {u_expanded:.4f}")

