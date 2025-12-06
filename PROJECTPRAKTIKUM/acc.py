users = {
    "asd": {"password": "123", "email": "asd@gmail.com", "role": "admin"},
    "qwe": {"password": "123", "email": "qwe@gmail.com", "role": "customer"}
}

def tau():
    from main import l
    print("======= BUAT AKUN BARU =======")

    allowed_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

    while True:
        email = input("email: ").strip()
        username = input("username: ").strip()
        password = input("password: ").strip()

        errors = []

        if "@" not in email:
            errors.append("email tidak valid!")
        else:
            nama, domain = email.split("@", 1)

            if domain not in allowed_domains:
                errors.append(
                    "domain email tidak dikenali! gunakan salah satu: " +
                    ", ".join(allowed_domains)
                )

            for u in users.values():
                if u["email"] == email:
                    errors.append("email sudah digunakan!")
                    break

        if username in users:
            errors.append("username sudah dipakai!")

        if errors:
            print("\n".join(errors))
            print("Coba lagi!\n")
            continue

        users[username] = {
            "password": password,
            "email": email,
            "role": "customer"
        }

        print("akun berhasil dibuat!\n")
        break
    
    l()
    
def taa():
    from main import menu_admin
    print("======= BUAT AKUN BARU =======")

    allowed_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

    while True:
        email = input("email: ").strip()
        username = input("username: ").strip()
        password = input("password: ").strip()

        errors = []

        if "@" not in email:
            errors.append("email tidak valid!")
        else:
            nama, domain = email.split("@", 1)

            if domain not in allowed_domains:
                errors.append(
                    "domain email tidak dikenali! gunakan salah satu: " +
                    ", ".join(allowed_domains)
                )
        
            for u in users.values():
                if u["email"] == email:
                    errors.append("email sudah digunakan!")
                    break
                
        if username in users:
            errors.append("username sudah dipakai!")

        if errors:
            print("\n".join(errors))
            print("Coba lagi!\n")
            continue

        users[username] = {
            "password": password,
            "email": email,
            "role": "admin"
        }

        print("akun berhasil dibuat!\n")
        break
    
    menu_admin(users)
    
def verify():
    from main import menu_admin
    while True:
        nx = "qw3"
        print("="*40)
        print("masukkan password untuk melanjutkan!\n")
        print("ketik back untuk kembali!")
        print("="*40)
        pw = input("password: ")
        
        if pw == nx:
            break
        if pw.lower() == "back":
            menu_admin(users)
        else:
            print("password salah!")
            continue
        
    taa()

def ta():
    print("====== DAFTAR SEMUA AKUN ======")

    if not users:
        print("belum ada akun.\n")
        return

    data_sorted = sorted(
        enumerate(users.items()),
        key=lambda x: (x[1][1]["role"], x[0])
    )

    admin = []
    customer = []

    for index, (username, data) in data_sorted:
        if data["role"] == "admin":
            admin.append((username, data))
        else:
            customer.append((username, data))

    print("============ ADMIN ============")
    if admin:
        for username, data in admin:
            print(f"username : {username}")
            print(f"email    : {data['email']}")
            print(f"role     : {data['role']}")
            print("-" * 30)
    else:
        print("(belum ada admin)\n")

    print("\n========== CUSTOMER ==========")
    if customer:
        for username, data in customer:
            print(f"username : {username}")
            print(f"email    : {data['email']}")
            print(f"role     : {data['role']}")
            print("-" * 30)
    else:
        print("(belum ada customer)\n")

    print()