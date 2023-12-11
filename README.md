# Crear la imagen
docker build -t ml:linear .

# ejecutar el contenedor
docker run -p 9999:8888 --name machine-learning ml:linear