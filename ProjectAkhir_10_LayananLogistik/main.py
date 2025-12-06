from acc import users
import acc as acc
import features as ft

def login():
    print("=============== LOGIN ===============")
    email = input("email: ").strip()
    password = input("password: ").strip()

    for username, data in users.items():
        if data["email"] == email and data["password"] == password:
            print(f"\nberhasil login, selamat datang {username}!\n")
            return data["role"], username

    print("\nemail atau password salah.\n")
    return None, None

def menu_admin(user):
    while True:
        print("======== MENU ADMIN ========")
        print("1. tampilkan pengiriman")
        print("2. tambah pengiriman")
        print("3. ubah status")
        print("4. hapus pengiriman")
        print("5. cari data")
        print("6. update data")
        print("7. cetak struk")
        print("8. kelola retur")
        print("9. tambahkan akun admin")
        print("10. lihat daftar akun")
        print("11. logout")

        p = input("pilih: ")

        if p == "1":
            ft.show()
        elif p == "2":
            ft.add(user)
        elif p == "3":
            ft.stats()
        elif p == "4":
            ft.delete()
        elif p == "5":
            ft.cari_data()
        elif p == "6":
            ft.update_data()
        elif p == "7":
            ft.cetak_struk(input("\nmasukkan resi: "))
        elif p == "8":
            ft.kr()
        elif p == "9":
            acc.verify()
        elif p == "10":
            acc.ta()
        elif p == "11":
            l()
        else:
            print("pilihan tidak valid.\n")

def menu_pembeli(user):
    while True:
        print("======== MENU PEMBELI ========")
        print("1. cek paket")
        print("2. lihat struk")
        print("3. ajukan retur")
        print("4. lihat status retur")
        print("5. logout")

        p = input("pilih: ")

        if p == "1":
            ft.cari_data()
        elif p == "2":
            ft.cetak_struk(input("\nmasukkan resi: "))
        elif p == "3":
            ft.ar(user)
        elif p == "4":
            resi = input("\nmasukkan resi: ")
            ft.tr(resi)
        elif p == "5":
            l()
        else:
            print("pilihan tidak valid.\n")

def main():
    while True:
        role, user = login()

        if role == "admin":
            menu_admin(user)
        elif role == "customer":
            menu_pembeli(user)
        else:
            continue

def l():
    while True:
        print("=============== LOGIN ===============")
        print("1. login")
        print("2. belum punya akun? daftar sekarang")
        print("3. exit")
    
        p = input("pilih: ")
    
        if p == "1":
            main()
        elif p == "2":
            acc.tau()
        elif p == "3":
            exit()
        else:
            print("pilihan tidak valid.\n")
            continue

if __name__ == "__main__":
    l() 