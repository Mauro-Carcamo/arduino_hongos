import serial

# Configuración del puerto serial (asegúrate de usar el puerto correcto)
ser = serial.Serial('COM4', 9600)  # Reemplaza 'COM3' con el nombre de tu puerto serial

try:
    while True:
        # Leer la línea de datos enviada por Arduino
        data = ser.readline().decode().strip()
        
        # Imprimir el valor del potenciómetro
        print("Valor del potenciómetro:", data)
        
except KeyboardInterrupt:
    ser.close()  # Cerrar el puerto serial al finalizar
    print("Comunicación serial cerrada.")