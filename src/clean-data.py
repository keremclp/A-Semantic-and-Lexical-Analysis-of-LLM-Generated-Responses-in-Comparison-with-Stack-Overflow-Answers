import pandas as pd
import re

# ==========================================
# CLEAN AND PREPARE DATASET
# ==========================================

def clean_text(text):
    """Remove excessive whitespace and HTML entities"""
    if pd.isna(text):
        return ""
    
    text = str(text)
    # Decode HTML entities
    text = text.replace('&quot;', '"').replace('&amp;', '&')
    text = text.replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&#39;', "'")
    
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    return text.strip()

print("📂 Veri seti okunuyor...")

try:
    # CRITICAL: Use proper CSV reading with quote handling
    df = pd.read_csv(
        'stackoverflow_with_gpt_answers.csv',
        encoding='utf-8-sig',
        quotechar='"',
        escapechar='\\',
        on_bad_lines='warn'  # Python 3.9+, shows warnings for bad lines
    )
    
    print(f"✅ {len(df)} satır yüklendi")
    
except Exception as e:
    print(f"❌ Hata: {e}")
    print("\nAlternatif okuma yöntemi deneniyor...")
    
    # Alternative: Use engine='python' for more robust parsing
    df = pd.read_csv(
        'stackoverflow_with_gpt_answers.csv',
        encoding='utf-8-sig',
        engine='python',
        quotechar='"',
        escapechar='\\'
    )
    print(f"✅ {len(df)} satır yüklendi (alternatif yöntem)")

# ==========================================
# DATA CLEANING
# ==========================================

print("\n🧹 Veri temizleniyor...")

# 1. Remove rows with missing critical data
initial_count = len(df)
df = df.dropna(subset=['question_title', 'question_body', 'human_answer', 'gpt_answer'])
print(f"   - Eksik veri olan {initial_count - len(df)} satır kaldırıldı")

# 2. Remove ERROR responses
error_count = df['gpt_answer'].str.contains('ERROR', case=False, na=False).sum()
if error_count > 0:
    df = df[~df['gpt_answer'].str.contains('ERROR', case=False, na=False)]
    print(f"   - ERROR içeren {error_count} satır kaldırıldı")

# 3. Clean text fields
print("   - Metinler temizleniyor...")
df['question_title'] = df['question_title'].apply(clean_text)
df['question_body'] = df['question_body'].apply(clean_text)
df['human_answer'] = df['human_answer'].apply(clean_text)
df['gpt_answer'] = df['gpt_answer'].apply(clean_text)

# 4. Remove duplicates
dup_count = df.duplicated(subset=['question_id']).sum()
if dup_count > 0:
    df = df.drop_duplicates(subset=['question_id'], keep='first')
    print(f"   - {dup_count} duplike satır kaldırıldı")

# 5. Remove empty or too short answers
min_length = 50  # Minimum character count for valid answers
df = df[
    (df['human_answer'].str.len() >= min_length) & 
    (df['gpt_answer'].str.len() >= min_length)
]
print(f"   - Çok kısa cevaplar kaldırıldı (min: {min_length} karakter)")

# 6. Reset index
df = df.reset_index(drop=True)

# ==========================================
# SAVE CLEANED DATA
# ==========================================

output_file = 'stackoverflow_cleaned.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n✅ Temizlenmiş veri seti kaydedildi: {output_file}")
print(f"📊 Toplam temiz satır: {len(df)}")

# ==========================================
# DISPLAY STATISTICS
# ==========================================

print("\n" + "="*60)
print("VERİ SETİ İSTATİSTİKLERİ")
print("="*60)

print(f"Toplam soru sayısı: {len(df)}")
print(f"\nOrtalama karakter uzunlukları:")
print(f"  - Soru başlığı: {df['question_title'].str.len().mean():.0f}")
print(f"  - Soru içeriği: {df['question_body'].str.len().mean():.0f}")
print(f"  - İnsan cevabı: {df['human_answer'].str.len().mean():.0f}")
print(f"  - GPT cevabı: {df['gpt_answer'].str.len().mean():.0f}")

print(f"\nİlk 5 soru:")
for idx, row in df.head(5).iterrows():
    print(f"  {idx+1}. {row['question_title'][:60]}...")

print("\n" + "="*60)