acc_510129={
    'ad':"Celal Karahan",
    'acc_no':"510129",
    'balance': 5000,
    'add_acc':2000
}

acc_510130={
    'ad':"Celal Karahan",
    'acc_no':"510130",
    'balance': 3000,
    'add_acc':1000
}
def bakiye_sorgu(hesap):
      print(f"{hesap['acc_no']} nolu hesabınızda {hesap['balance']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['add_acc']} TL bulunmaktadır.")

def para_cek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if(hesap['balance'] >= miktar):
        hesap['balance']-=miktar
        print("Paranızı alabilirsiniz")
        print("Cekim sonrası bakiye : ")
        bakiye_sorgu(hesap)
    else:
        top_mon=hesap['balance']+hesap['add_acc']
        if(top_mon>=miktar):
            add_mon_use=input("bakiye yetersiz ek hesap kullanılsınmı (e/h)")
            if(add_mon_use=="e"):
                hesap['balance']=0
                hesap['add_acc']=top_mon-miktar
                print("Paranızı alabilirsiniz")
                print("Cekim sonrası bakiye : ")
                bakiye_sorgu(hesap)
            elif (add_mon_use=='h'):
                print("ek hesap kullanımı reddedildi cıkış yapılıyor")
            else:
                print("Yanlıs secim")
        else:
            print("Hesabınızın bakiye ile ek hesap bakiyesi toplamı yetersiz")
            bakiye_sorgu(hesap)
para_cek(acc_510129,8000)     
               
            
    
        
    