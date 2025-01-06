const int sensorPin = 2;  // Sensor connected to digital pin 2

void setup() {
  pinMode(sensorPin, INPUT);  // Set the pin as input
  Serial.begin(9600);        // Start serial communication
}

void loop() {
  int sensorState = digitalRead(sensorPin);  // Read sensor state (HIGH or LOW)
  
  if (sensorState == HIGH) {
    Serial.println("Pulse Detected: HIGH");
    delay(1000);
  }
  
  delay(250);  // Log every 250ms; adjust if necessary
}
