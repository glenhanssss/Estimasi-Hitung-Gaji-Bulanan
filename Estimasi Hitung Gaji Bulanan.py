# Membuat fungsi pengubah tipe data float menjadi format Rupah (Rp)
def transform_to_rupiah_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return "Rp " + temp_result + "," + before_decimal

# # # #

# BASIC SALARY
basic = float(input("Masukkan gaji Pokok = "))
print(f"*Besar Gaji Pokok = {transform_to_rupiah_format(basic)}")

# COMMUNICATION ALLOWANCE (Optional, if you have)
comm = float(input("Masukkan communication allowance (jika tidak ada isi 0) = "))
print(f"*Besar Communication Allowance = {transform_to_rupiah_format(comm)}")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\n")

# PPH 21
# source: https://www.talenta.co/blog/apa-itu-spt-pph-21-juga-tarif-pph-pasal-21-adalah-berapa-persen/
# source : https://www.talenta.co/blog/jenis-potongan-gaji-karyawan/
# Penghasilan Kena Pajak (PKP) = Penghasilan Neto Setahun - Penghasilan Tidak Kena Pajak (PTKP)

print("Menghitung penghasilan kena pajak (PKP)")
penghasilan_neto_setahun = basic*12
ptkp = float(54000000)
print(f"penghasilan tidak kena pajak (PTKP) yang berlaku bagi pekerja tidak kawin dengan 0 tanggungan anak adalah {transform_to_rupiah_format(ptkp)} (54 juta) ")
print(f"penghasilan kena pajak (PKP) = ( {transform_to_rupiah_format(basic)} * 12 ) - {transform_to_rupiah_format(ptkp)}")
pkp = penghasilan_neto_setahun - ptkp
print("penghasilan kena pajak (PKP) = ", transform_to_rupiah_format(pkp))

print("besar tarif pajak sebesar 5% jika pkp <= 60 juta")
print(f"karena PKP sebesar {transform_to_rupiah_format(pkp)}, maka rumus tarif pph21 setahun menjadi 5% x {transform_to_rupiah_format(float(60000000))}")
tarif_pajak_setahun = ((5/100)*60000000)
tarif_pajak_sebulan = tarif_pajak_setahun/12
print("tarif pph21 setahun = ", transform_to_rupiah_format(tarif_pajak_setahun))
print("tarif pph21 sebulan = ", transform_to_rupiah_format(tarif_pajak_sebulan))
print("\n")

# POTONGAN BPJS
print("Rincian BPJS:")
print("- BPJS Kesehatan 1%")
print("- BPJS Ketenagakerjaan : Jaminan Hari Tua 2%")
print("- BPJS Ketenagakerjaan : Jaminan Pensiun 1%")
print("- BPJS Ketenagakerjaan : Jaminan Kecelakaan Kerja 0,24% dan Jaminan Kematian 0,3%")

b1 = 1/100
b2 = 2/100
b3 = 1/100
b4 = 0.24/100
b5 = 0.3/100

persen_bpjs = (b1 + b2 + b3 + b4 + b5)
print("Persentase total untuk membayar BPJS = ", persen_bpjs)
print(f"Total Pembayaran BPJS Kesehatan dan Ketenagakerjaan = {persen_bpjs} * {transform_to_rupiah_format(basic)}")
bpjs_tot = persen_bpjs*basic
print("Total Pembayaran BPJS Kesehatan dan Ketenagakerjaan = ", transform_to_rupiah_format(bpjs_tot))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\n")

# rumus hitung gaji kotor
print("Gaji kotor sebulan = Basic Salary - (Tarif Pajak Sebulan + Total Pembayaran BPJS) + Communication Allowance")
print(f"Gaji kotor sebulan = {transform_to_rupiah_format(basic)} - ({transform_to_rupiah_format(tarif_pajak_sebulan)} + {transform_to_rupiah_format(bpjs_tot)}) + {transform_to_rupiah_format(comm)}")
gaji_kotor = basic - (tarif_pajak_sebulan + bpjs_tot) + comm
print("Gaji kotor sebulan -+ sekitar ", transform_to_rupiah_format(gaji_kotor))

# transport
transport = float(input("Masukkan uang transport per hari: "))
transport = transport*22
print("uang 35transport per bulan = ", transform_to_rupiah_format(transport))

# makan
makan = float(input("Masukkan uang makan per hari: "))
makan = makan*22
print("uang makan per bulan = ", transform_to_rupiah_format(makan))

# rumus hitung gaji bersih
print("Gaji Bersih sebulan = Gaji Kotor - ( Uang Transport sebulan + Uang Makan sebulan )")
print(f"Gaji Bersih sebulan = {transform_to_rupiah_format(gaji_kotor)} - ( {transform_to_rupiah_format(transport)} + {transform_to_rupiah_format(makan)} )")
gaji_bersih = gaji_kotor - (transport + makan)
print("Gaji bersih sebulan -+ sekitar ", transform_to_rupiah_format(gaji_bersih))