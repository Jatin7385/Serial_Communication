void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=1;i<100;i++)
  {
    String prefix = "1000,23:52:01,";
    String suffix = ",C,F,R,N,422,25.6,8.8,23:52:01,37.2314,80.4264,422.6,7,RELEASE_1,73,0,CX-ON";
    Serial.println(prefix + String(i) + suffix);
    delay(1000);
  }
}
