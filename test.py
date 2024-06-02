import torch

# Verificar la disponibilidad de la GPU
if torch.cuda.is_available():
    print(f"GPU disponible: {torch.cuda.get_device_name(0)}")
else:
    print("GPU no disponible")