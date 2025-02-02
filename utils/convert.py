import pandas as pd
"""

BURADA EXCELE KAYITLI VERİLERİ CSV DOSYASINA ÇEVİRDİK DAHA RAHAT ÇALIŞABİLMEK ADINA

"""

# Excel dosyasını oku 
df_2010_2011 = pd.read_excel(r"C:\Users\PC\Desktop\Segma\data\raw\online_retail_II.xlsx", sheet_name=0, engine="openpyxl")

# CSV formatına çevir ve kaydet
df_2010_2011.to_csv(r"C:\Users\PC\Desktop\Segma\data\raw\online_retail_2010_2011.csv", index=False)
print("Dönüştürme tamamlandı! Dosya: online_retail_2010_2011.csv")

# Excel dosyasını oku 
df_2009_2010 = pd.read_excel(r"C:\Users\PC\Desktop\Segma\data\raw\online_retail_II.xlsx", sheet_name=0, engine="openpyxl")

# CSV formatına çevir ve kaydet
df_2009_2010.to_csv(r"C:\Users\PC\Desktop\Segma\data\raw\online_retail_2009_2010.csv", index=False)
print("Dönüştürme tamamlandı! Dosya: online_retail_2009_2010.csv")
