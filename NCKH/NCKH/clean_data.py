import pandas as pd
import numpy as np
import re

def parse_discount(x):
    if pd.isna(x):
        return 0.0
    x = str(x)
    # Tìm con số trong chuỗi (ví dụ "10% off" -> 10.0)
    match = re.search(r"(\d+(\.\d+)?)", x)
    if match:
        return float(match.group(1))
    return 0.0

def clean_currency_to_numeric(series):
    # Chuyển về string, xóa mọi thứ KHÔNG PHẢI là số
    # Ví dụ: "1.200.000đ" -> "1200000"
    cleaned = series.astype(str).str.replace(r'[^\d]', '', regex=True)
    return pd.to_numeric(cleaned, errors='coerce').fillna(0)

def advanced_cleaning(df):
    df.columns = df.columns.str.strip()
    
    # 1. Làm sạch tên sản phẩm
    if 'name' in df.columns:
        df = df[df['name'].apply(lambda x: len(str(x)) > 5)].copy()

    # 2. Xử lý PRICE (Đã sửa lỗi)
    if 'price' in df.columns:
        df['price'] = clean_currency_to_numeric(df['price'])
        
        if 'original_price' in df.columns:
            df['original_price'] = clean_currency_to_numeric(df['original_price'])
            # Nếu giá bán = 0, lấy giá gốc
            df.loc[df['price'] == 0, 'price'] = df['original_price']
        
        # Điền giá trung vị theo Brand (Tránh trường hợp toàn bộ brand đó giá = 0)
        overall_median = df[df['price'] > 0]['price'].median()
        brand_median = df[df['price'] > 0].groupby('brand')['price'].transform('median')
        df.loc[df['price'] == 0, 'price'] = brand_median.fillna(overall_median)

    # 3. Xử lý RATING & REVIEWS
    for col in ['rating', 'review_count']:
        if col in df.columns:
            # Rating đôi khi là "4.5/5", ta chỉ lấy số đầu
            if col == 'rating':
                df[col] = df[col].astype(str).str.extract(r'(\d+\.?\d*)').astype(float).fillna(0)
            else:
                df[col] = clean_currency_to_numeric(df[col])

    # ... (Các phần xử lý discount_value và brand giữ nguyên như cũ)
    # 4. Xử lý Brand (Chuẩn hóa để LabelEncoder không bị rối)
    if 'brand' in df.columns:
        df['brand'] = df['brand'].fillna('no brand').replace(['nan', '0', 'unknown'], 'no brand')
        df['brand'] = df['brand'].str.lower().str.strip()

    # 5. Xử lý Discount Value (Đảm bảo có cột này cho mô hình)
    if 'discount_value' not in df.columns and 'discount' in df.columns:
        df['discount_value'] = df['discount'].apply(parse_discount)
    elif 'discount_value' not in df.columns:
        df['discount_value'] = 0.0
    
    # Giới hạn logic discount
    df.loc[df['discount_value'] > 100, 'discount_value'] = 0
    return df
# Thực hiện chạy script
file_input = 'data_final.csv'
file_output = 'data_final_cleaned.csv'

try:
    print(f"Đang đọc file {file_input}...")
    products = pd.read_csv(file_input)
    cleaned_products = advanced_cleaning(products)
    
    cleaned_products.to_csv(file_output, index=False)
    print(f"--- THÀNH CÔNG ---")
    print(f"Số lượng sản phẩm sau khi làm sạch: {len(cleaned_products)}")
    print(f"File đã lưu tại: {file_output}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")