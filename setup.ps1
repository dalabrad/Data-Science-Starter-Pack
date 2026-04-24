Write-Host "🚀🚀🚀 Setting up Data Science template..." -ForegroundColor Cyan

# Crear entorno virtual (solo si no existe)
if (!(Test-Path "venv")) {
    python -m venv venv
}

# Activar entorno
.\venv\Scripts\Activate.ps1

# Actualizar pip
python -m pip install --upgrade pip

# Instalar base de data science
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# Guardar dependencias
pip freeze > requirements.txt

Write-Host "✅✅✅ Template ready to use! ✅✅✅" -ForegroundColor Green