int x_value; 
int y_value;

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void loop() {
  x_value = analogRead(A0);
  y_value = analogRead(A1);
  Serial.print(x_value);
  Serial.print(","); // カンマで区切る
  Serial.println(y_value);
  
}
