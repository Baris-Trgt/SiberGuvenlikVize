import nmap #nmap kütüphanesini python'a import ettim

#kullanıcı icin bilgilendirme yaptım
print("\n-----------------------Hangi IP Adresi Hangi Portu Kullandığını ve Portların Durumunu Gösteren Uygulama-----------------------")
print("\nLütfen IP Adreslerinin Arasına , (virgül) Kullanmayınız  . (nokta) Kullanınız !!!! ")
print("Örnek: 192.168.x.x şeklinde IP adreslerini giriniz :")
print("\n***** ÖNEMLİ *****\n")
print("Tek IP Adresi Taratmak Icin 192.168.x.x Seklinde Deger Giriniz !!!!!!")
print("Birden Fazla IP Adresi Aralıgı Taratmak Icin  192.168.x.x/25   192.168.x.x-25   192.168.x.x/255   192.168.x.x-255 Seklinde Deger Giriniz !!!!!!")


ip_gir = input("\nLütfen taramak istediğiniz ip adresini veya ip adresi aralığını giriniz: ") #nmap den aranacak olan  IP değerlerini girdirdim
print("Bu Islem Biraz Zaman Alacaktır Lütfen Bekleyiniz...")
tara = nmap.PortScanner() #PortScanner() ı tara değişkenine atadım ve nmap.PortScanner() kullanarak IP taraması yaptım
tara.scan(hosts=ip_gir) #IP leri kullanıcıdan girdirdim



for ip in tara.all_hosts(): #bir döngü oluşturdum ve tüm host bilgilerini topladım
    print('\nTaranan IP Adresi : %s ' % (ip)) #taranan IP adresini yazdırdım

    for proto in tara[ip].all_protocols(): #bir döngü daha oluşturdum ve taradıgım ip adreslerinin kullandıgı tüm protokolleri topladım
        print('----------')
        listele_port = tara[ip][proto].keys() #keys() ile belirtilen değerlerin görüntülenmesini sağladım
        #bu işlem hangi IP lerin hangi portları kullandığını gösteriyor
        for port in listele_port: 
            print('Port : %s\t Durumu : %s' % (port, tara[ip][proto][port]['state']))
            #bu işlemde hangi IP adresinin hangi portları kullandığını ve bu portların açık mı kapalı mı olduğunu gösterir

breakpoint()
#uygulamayı exe yapınca hemen kapanmasın diye kullandım

