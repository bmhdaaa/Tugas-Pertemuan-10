
import tkinter as tk
from tkinter import ttk, messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("550x600")
root.resizable(False, False)

# Konfigurasi warna
warna_bg = "#EAF2F8"
warna_header = "#154360"
warna_tombol = "#2874A6"
warna_teks = "#1B2631"

root.configure(bg=warna_bg)

# Judul aplikasi
judul = tk.Label(
    root,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 16, "bold"),
    bg=warna_header,
    fg="white",
    pady=15
)
judul.pack(fill="x")

# Frame utama
form = tk.Frame(root, bg=warna_bg, padx=25, pady=20)
form.pack(fill="both", expand=True)

# Style label
def buat_label(teks, baris):
    tk.Label(
        form,
        text=teks,
        font=("Arial", 11),
        bg=warna_bg,
        fg=warna_teks
    ).grid(row=baris, column=0, sticky="w", pady=10)

# Input Nama
buat_label("Nama Lengkap", 0)

nama = tk.Entry(
    form,
    width=35,
    font=("Arial", 11)
)
nama.grid(row=0, column=1, pady=10, padx=10)

# Input NIM
buat_label("NIM", 1)

nim = tk.Entry(
    form,
    width=35,
    font=("Arial", 11)
)
nim.grid(row=1, column=1, pady=10, padx=10)

# Pilihan Program Studi
buat_label("Program Studi", 2)

prodi = ttk.Combobox(
    form,
    values=[
        "Informatika",
        "Manajemen",
        "Akuntansi",
        "Teknik Sipil",
        "Sistem Informasi"
    ],
    state="readonly",
    width=32,
    font=("Arial", 10)
)
prodi.grid(row=2, column=1, pady=10, padx=10)

# Input Alamat menggunakan Text
buat_label("Alamat", 3)

alamat = tk.Text(
    form,
    width=26,
    height=4,
    font=("Arial", 11),
    relief="solid",
    bd=1
)
alamat.grid(row=3, column=1, pady=10, padx=10)

# Label hasil
hasil_judul = tk.Label(
    form,
    text="HASIL IDENTITAS MAHASISWA",
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_header
)
hasil_judul.grid(
    row=4, column=0, columnspan=2, pady=(20, 5)
)

hasil = tk.Label(
    form,
    text="Data mahasiswa akan ditampilkan di sini.",
    font=("Arial", 10),
    bg="white",
    fg=warna_teks,
    justify="left",
    anchor="w",
    width=55,
    height=7,
    relief="groove",
    padx=10,
    pady=10
)
hasil.grid(row=5, column=0, columnspan=2, pady=5)

# Fungsi Simpan
def simpan():
    data_nama = nama.get().strip()
    data_nim = nim.get().strip()
    data_prodi = prodi.get()
    data_alamat = alamat.get("1.0", tk.END).strip()

    # Validasi nama dan NIM
    if data_nama == "":
        messagebox.showwarning(
            "Peringatan",
            "Nama tidak boleh kosong!"
        )
        nama.focus()
        return

    if data_nim == "":
        messagebox.showwarning(
            "Peringatan",
            "NIM tidak boleh kosong!"
        )
        nim.focus()
        return

    if data_prodi == "":
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih Program Studi!"
        )
        prodi.focus()
        return

    # Menampilkan hasil
    hasil.config(
        text=(
            f"Nama           : {data_nama}\n"
            f"NIM              : {data_nim}\n"
            f"Program Studi : {data_prodi}\n"
            f"Alamat          : {data_alamat or '-'}"
        ),
        bg="#D5F5E3"
    )

    messagebox.showinfo(
        "Berhasil",
        "Data mahasiswa berhasil disimpan!"
    )

# Fungsi Reset
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)

    hasil.config(
        text="Data mahasiswa akan ditampilkan di sini.",
        bg="white"
    )

# Fungsi Keluar
def keluar():
    konfirmasi = messagebox.askyesno(
        "Konfirmasi Keluar",
        "Apakah Anda yakin ingin keluar?"
    )

    if konfirmasi:
        root.destroy()

# Frame tombol
frame_tombol = tk.Frame(form, bg=warna_bg)
frame_tombol.grid(
    row=6, column=0, columnspan=2, pady=20
)

# Tombol Simpan
tk.Button(
    frame_tombol,
    text="SIMPAN",
    command=simpan,
    bg="#2874A6",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=5)

# Tombol Reset
tk.Button(
    frame_tombol,
    text="RESET",
    command=reset,
    bg="#D68910",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=5)

# Tombol Keluar
tk.Button(
    frame_tombol,
    text="KELUAR",
    command=keluar,
    bg="#C0392B",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=5)

# Menjalankan aplikasi
root.mainloop()
