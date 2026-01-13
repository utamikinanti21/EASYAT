#fungsi untuk menambah histori berat badan
import pandas as pd
from datetime import datetime

history_file = "history_berat.csv"

def add_history(username, berat_badan):
    tanggal = datetime.now().strftime("%d-%m-%Y")

    data = {
        "Username": [username],
        "Tanggal" : [tanggal],
        "BeratBadan" : [berat_badan]
    }

    df = pd.DataFrame(data)

    try:
        df.to_csv(history_file, mode="a", index=False, header=False)
    except FileNotFoundError:
        df.to_csv(history_file, index=False)


#fungsi untuk melihat histori dan total naik/turun

def history_berat(username):
    try:
        df = pd.read_csv(history_file)
    except FileNotFoundError:
        print("Belum ada histori berat badan.")
        return
    
    user_history = df[df["Username"] == username]

    if user_history.empty:
        print("Belum ada histori berat badan untuk user ini.")
        return
    
    print("\n======= History Berat Badan =======")
    for _, row in user_history.iterrows():
        print(f"{row["Tanggal"]} | {row["BeratBadan"]} kg")
    
    berat_awal = user_history.iloc[0]["BeratBadan"]
    berat_akhir = user_history.iloc[-1]["BeratBadan"]
    perubahan = berat_akhir - berat_awal

    print("\n======= Ringkasan =======")
    print(f"Berat awal : {berat_awal} kg")
    print(f"Berat terakhir: {berat_akhir} kg")

    if perubahan < 0:
        print(f"Total perubahan: {perubahan} kg (Turun, yey)")
    elif perubahan > 0:
        print(f"Total perubahan: +{perubahan} kg (Naik, yaahh)")
    else:
        print("Total perubahan: 0 kg (Stabil)")

    print("=======================================\n")