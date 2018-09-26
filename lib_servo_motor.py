# HEADER : SERVO MOTOR MODUL
# AUTHOR : Muhammed YILMAZ
# DATE   : 26.09.2018
# E-MAIL : yilmazmu15@itu.edu.tr


# Servo motorun program içerisinde rahatça kullanılabilmesi için oluşturulmuş modüldür.
import RPi.GPIO as GPIO


# Servo motorun pinini  ayarla
# Diğer fonksiyonları kullanmak için pinleri_ayarla() fonksiyonunun dönüş değeri kullanılır (pwn)
def pinleri_ayarla(pin):
    GPIO.setup(pin, GPIO.OUT)
    pwn = GPIO.PWM(pin, 50)
    baslat(pwn)
    return pwn


# Servo motorun güç ayarını başlat
def baslat(pwn):
    pwn.start(0)


# Motor gücünü değiştirerek istenen açıya gelmesini sağlar
def aci_degistir(pwn, aci):
    duty = float(aci) / 10.0 + 2.5
    pwn.ChangeDutyCycle(duty)


# Motoru durdurur
def durdur(pwn):
    pwn.stop()
