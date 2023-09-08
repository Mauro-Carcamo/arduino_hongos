const int potPin = A0; // Pin analógico donde está conectado el potenciómetro
const int ledPin = 9;  // Pin digital donde está conectado el LED

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int potValue = analogRead(potPin); // Lee el valor del potenciómetro (0-1023)
  int brightness = map(potValue, 0, 1023, 0, 255); // Mapea el valor a un rango de brillo (0-255)
  analogWrite(ledPin, brightness); // Cambia el brillo del LED utilizando PWM
}