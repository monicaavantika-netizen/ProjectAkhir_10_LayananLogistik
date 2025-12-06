import acc as acc

all = {}

def add(user):
    while True:
        resi = input("\nbuat resi dengan panjang 5 angka: ")
        if not resi.isdigit():
            print("resi harus berupa angka! coba lagi.\n")
            continue 
        elif len(resi) != 5:
            print("resi harus 5 angka! coba lagi.\n")
            continue
        if resi in all:
            print("resi sudah terdaftar! buat resi lain.\n")
            continue
        break

    pengirim = input("\nmasukkan nama pengirim: ")
    penerima = input("masukkan nama penerima: ")
    alamat = input("masukkan alamat tujuan: ")
    nb = input("masukkan nama barang: ")
    berat = int(input("masukkan berat barang (kg): "))

    hpkg = 5000
    biaya = berat * hpkg

    if berat >= 10:
        diskon = 0.20
    elif berat >= 5:
        diskon = 0.10
    else:
        diskon = 0

    diskon_rp = biaya * diskon
    total = biaya - diskon_rp

    all[resi] = {
        "pengirim": pengirim,
        "penerima": penerima,
        "alamat": alamat,
        "nb": nb,
        "berat": berat,
        "biaya": biaya,
        "diskon": diskon_rp,
        "total": total,
        "status": "dikemas",
        "retur": None
    }

    print("pengiriman berhasil ditambahkan.\n")

def stats():
    resi = input("masukkan nomor resi untuk ubah status: ")
    if resi not in all:
        print("resi tidak ditemukan.\n")
        return

    print("\npilih status baru:")
    print("1. dikemas")
    print("2. dalam perjalanan")
    print("3. sudah diterima")

    pilih = input("Pilih (1/2/3): ")

    if pilih == "1":
        all[resi]["status"] = "dikemas"
    elif pilih == "2":
        all[resi]["status"] = "dalam perjalanan"
    elif pilih == "3":
        all[resi]["status"] = "sudah diterima"
    else:
        print("pilihan tidak valid.\n")
        return

    print(f"Status resi {resi} berhasil diubah menjadi '{all[resi]['status']}'.\n")

def show():
    if not all:
        print("Tidak ada data yang tersimpan.\n")
        return

    print("="*45)
    print("Daftar Pengiriman:")
    print("="*45)

    for resi, data in all.items():
        print(f"Resi: {resi}")
        print(f"  nama Pengirim   : {data['pengirim']}")
        print(f"  nama Penerima   : {data['penerima']}")
        print(f"  alamat Tujuan   : {data['alamat']}")
        print(f"  nama Barang     : {data['nb']}")
        print(f"  berat Barang    : {data['berat']} KG")
        print(f"  diskon barang   : Rp. {data['diskon']}")
        print(f"  total biaya     : Rp. {data['total']}")
        print(f"  status          : {data['status']}")
        print("="*45)
    print()

def delete():
    resi = input("masukkan Nomor Resi Barang yang akan dihapus: ")
    if resi in all:
        del all[resi]
        print(f"data pengiriman dengan resi {resi} berhasil dihapus.\n")
    else:
        print(f"tidak ditemukan data pengiriman dengan resi {resi}.\n")


def cari_data():
    resi = input("masukkan resi yang ingin dicari: ")

    if resi not in all:
        print("resi tidak ditemukan.\n")
        return
    
    d = all[resi]

    print("\n===== DATA PENGIRIMAN =====")
    print(f"resi      : {resi}")
    print(f"pengirim  : {d['pengirim']}")
    print(f"penerima  : {d['penerima']}")
    print(f"alamat    : {d['alamat']}")
    print(f"barang    : {d['nb']}")
    print(f"berat     : {d['berat']} KG")
    print(f"total     : Rp. {d['total']}")
    print(f"status    : {d['status']}\n")

def update_data():
    resi = input("masukkan resi untuk update data: ")
    if resi not in all:
        print("resi tidak ditemukan.\n")
        return
    
    print("\nkosongkan jika tidak ingin mengubah")
    pengirim = input("pengirim baru: ")
    penerima = input("penerima baru: ")
    alamat = input("alamat tujuan baru: ")
    nb = input("nama barang baru: ")

    if pengirim != "":
        all[resi]["pengirim"] = pengirim
    if penerima != "":
        all[resi]["penerima"] = penerima
    if alamat != "":
        all[resi]["alamat"] = alamat
    if nb != "":
        all[resi]["nb"] = nb

    print("data berhasil diperbarui.\n")


def cetak_struk(resi):
    if resi not in all:
        print("resi tidak ditemukan.\n")
        return
    
    d = all[resi]

    print("\n========== STRUK PENGIRIMAN ==========")
    print(f"resi        : {resi}")
    print(f"pengirim    : {d['pengirim']}")
    print(f"penerima    : {d['penerima']}")
    print(f"alamat      : {d['alamat']}")
    print(f"nama barang : {d['nb']}")
    print(f"berat       : {d['berat']} KG")
    print(f"total biaya : Rp. {d['total']}")
    print(f"status      : {d['status']}")
    print("=======================================\n")
    
def ar(user): #ar = ajukan retur
    resi = input("masukkan resi yang ingin diretur: ")

    if resi not in all:
        print("resi tidak ditemukan.\n")
        return

    if all[resi].get("retur") is not None:
        print("retur sudah diajukan sebelumnya.\n")
        return

    alasan = input("masukkan alasan retur: ")

    if alasan.strip() == "":
        print("alasan tidak boleh kosong.\n")
        return

    all[resi]["retur"] = {
        "oleh": user,
        "alasan": alasan,
        "status": "menunggu persetujuan"
    }

    print("\npengajuan retur berhasil dikirim. Menunggu persetujuan admin.\n")

def kr(): #kr = kelola retur
    print("\n====== DAFTAR RETUR YANG DIAJUKAN ======")

    ada = False
    for resi, data in all.items():
        if data.get("retur") and data["retur"]["status"] == "menunggu persetujuan":
            ada = True
            print(f"Resi : {resi}")
            print(f"Alasan: {data['retur']['alasan']}")
            print("----------------------------")

    if not ada:
        print("tidak ada retur untuk diproses.\n")
        return

    resi = input("\nmasukkan resi yang ingin diproses: ")

    if resi not in all or all[resi].get("retur") is None:
        print("resi tidak valid atau tidak ada pengajuan retur.\n")
        return

    print("\n1. setujui retur")
    print("2. tolak retur")
    pilih = input("pilih: ")

    if pilih == "1":
        all[resi]["retur"]["status"] = "disetujui"
        print("\nRetur disetujui.\n")

    elif pilih == "2":
        all[resi]["retur"]["status"] = "ditolak"
        print("\nRetur ditolak.\n")

    else:
        print("pilihan tidak valid.\n")
        
def tr(resi): #tr = tampilkan retur
    if resi not in all:
        print("\nresi tidak ditemukan!\n")
        return

    data = all[resi]["retur"]

    print("\n============== STATUS RETUR ==============")

    if data is None:
        print("status retur : belum ada pengajuan retur")

    else:
        print(f"Diajukan Oleh    : {data['oleh']}")
        print(f"Alasan           : {data['alasan']}")
        print(f"Status Pengajuan : {data['status']}")

    print("==========================================\n")