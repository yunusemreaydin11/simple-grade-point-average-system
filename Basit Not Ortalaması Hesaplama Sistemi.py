print("Takdir Teşekkür Hesaplama")

m1 = float(input("Matematik Birinci Sınav Notunuzu Giriniz:"))
m2 = float(input("Matematik İkinci Sınav Notunuzu Giriniz:"))
m3 = float(input("Matematik Üçüncü Sınav Notunuzu Giriniz:"))
 
mort = (m1 + m2 + m3) / 3

s1 = float(input("Sosyal Birinci Sınav Notunuzu Giriniz: "))
s2 = float(input("Sosyal İkinci Sınav Notunuzu Giriniz: "))
s3 = float(input("Sosyal Üçüncü Sınav Notunuzu Giriniz: "))

sort = (s1 + s2 + s3) / 3

t1 = float(input("Türkçe Birinci Sınav Notunuzu Giriniz: "))
t2 = float(input("Türkçe İkinci Sınav Notunuzu Giriniz: "))
t3 = float(input("Türkçe Üçüncü Sınav Notunuzu Giriniz: "))

tort = (t1 + t2 + t3) / 3

f1 = float(input("Fen Birinci Sınav Notunuzu Giriniz: "))
f2 = float(input("Fen İkinci Sınav Notunuzu Giriniz: "))
f3 = float(input("Fen Üçüncü Sınav Notunuzu Giriniz: "))

fort = (f1 + f2 + f3) / 3

dönemort = (mort + sort + fort) / 3

print("Dönem Ortalamanız:",round(dönemort, 3))

if (dönemort >= 85 ):
    print("Tebrikler Takdir Belgesi Kazandınız!")
elif ( 70 <= dönemort < 85):
    print("Tebrikler Teşekkür Belgesi Kazandınız!")
else:
    print("Belge Kazanamadınız.")
          
