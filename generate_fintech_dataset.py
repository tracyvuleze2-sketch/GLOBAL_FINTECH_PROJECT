"""
generate_fintech_dataset.py
============================
Generates a realistic, messy 100,000-row FinTech Digital Payments dataset
suitable for an end-to-end data analytics project covering:
  - Data Cleaning (Python / Pandas)
  - SQL Analysis
  - EDA (Seaborn / Matplotlib)
  - Power BI Dashboarding
  - Stakeholder Storytelling

Output: fintech_payments_raw.csv

Requirements:
    pip install pandas numpy faker tqdm
"""

import pandas as pd
import numpy as np
from faker import Faker
from tqdm import tqdm
import random
import uuid
import warnings
warnings.filterwarnings("ignore")

fake = Faker()
np.random.seed(42)
random.seed(42)

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
N_ROWS = 100_000
START_DATE = "2022-01-01"
END_DATE   = "2024-12-31"
OUTPUT_FILE = "fintech_payments_raw.csv"

# ──────────────────────────────────────────────
# LOOKUP TABLES  (clean versions — dirt added later)
# ──────────────────────────────────────────────
COUNTRIES = {
    "Kenya":         0.18,
    "Nigeria":       0.16,
    "South Africa":  0.12,
    "Ghana":         0.08,
    "Egypt":         0.07,
    "Tanzania":      0.06,
    "Uganda":        0.05,
    "United States": 0.09,
    "United Kingdom":0.07,
    "India":         0.06,
    "Germany":       0.03,
    "France":        0.03,
}

CURRENCY_MAP = {
    "Kenya": "KES", "Nigeria": "NGN", "South Africa": "ZAR",
    "Ghana": "GHS", "Egypt": "EGP", "Tanzania": "TZS",
    "Uganda": "UGX", "United States": "USD", "United Kingdom": "GBP",
    "India": "INR", "Germany": "EUR", "France": "EUR",
}

EXCHANGE_RATES = {   # to USD (approximate 2023 averages)
    "KES": 0.0075, "NGN": 0.00130, "ZAR": 0.054,
    "GHS": 0.072,  "EGP": 0.032,  "TZS": 0.00040,
    "UGX": 0.00027,"USD": 1.0,    "GBP": 1.27,
    "INR": 0.012,  "EUR": 1.08,
}

PAYMENT_METHODS_CLEAN = [
    "M-Pesa", "Credit Card", "Debit Card", "Bank Transfer",
    "PayPal", "Airtel Money", "MTN Mobile Money", "Crypto Wallet",
    "Apple Pay", "Google Pay"
]

PRODUCT_CATEGORIES_CLEAN = [
    "Electronics", "Fashion & Apparel", "Groceries", "Travel & Hospitality",
    "Health & Beauty", "Financial Services", "Entertainment", "Education",
    "Home & Furniture", "Automotive"
]

CUSTOMER_SEGMENTS_CLEAN = ["Retail", "SME", "Corporate", "Premium", "Basic"]

TRANSACTION_STATUSES_CLEAN = ["Completed", "Failed", "Pending", "Declined", "Refunded"]

DEVICE_TYPES = ["Mobile", "Desktop", "Tablet"]

PLATFORMS_CLEAN = ["Android", "iOS", "Web", "USSD", "POS Terminal"]

# ──────────────────────────────────────────────
# DIRTY VARIANT MAPS  (simulate real-world inconsistency)
# ──────────────────────────────────────────────
PAYMENT_DIRTY = {
    "M-Pesa":           ["M-Pesa", "Mpesa", "mpesa", "M-PESA", "MPESA"],
    "Credit Card":      ["Credit Card", "credit card", "CreditCard", "CC"],
    "Debit Card":       ["Debit Card", "debit card", "DebitCard", "DC"],
    "Bank Transfer":    ["Bank Transfer", "bank transfer", "BankTransfer", "Wire Transfer"],
    "PayPal":           ["PayPal", "Paypal", "paypal", "PAYPAL"],
    "Airtel Money":     ["Airtel Money", "AirtelMoney", "airtel money"],
    "MTN Mobile Money": ["MTN Mobile Money", "MTN MoMo", "MTN", "mtn mobile money"],
    "Crypto Wallet":    ["Crypto Wallet", "Crypto", "crypto wallet", "Cryptocurrency"],
    "Apple Pay":        ["Apple Pay", "ApplePay", "apple pay"],
    "Google Pay":       ["Google Pay", "GooglePay", "google pay", "GPay"],
}

SEGMENT_DIRTY = {
    "Retail":    ["Retail", "retail", "RETAIL"],
    "SME":       ["SME", "Sme", "sme", "Small Business"],
    "Corporate": ["Corporate", "corporate", "CORPORATE", "Corp"],
    "Premium":   ["Premium", "premium", "PREMIUM", "VIP"],
    "Basic":     ["Basic", "basic", "BASIC", "Standard"],
}

PLATFORM_DIRTY = {
    "Android":      ["Android", "android", "ANDROID"],
    "iOS":          ["iOS", "IOS", "ios", "Apple iOS"],
    "Web":          ["Web", "web", "WEB", "Browser"],
    "USSD":         ["USSD", "ussd"],
    "POS Terminal": ["POS Terminal", "POS", "pos", "Point of Sale"],
}

CATEGORY_DIRTY = {
    "Electronics":          ["Electronics", "electronics", "ELECTRONICS"],
    "Fashion & Apparel":    ["Fashion & Apparel", "Fashion", "fashion & apparel", "Clothing"],
    "Groceries":            ["Groceries", "groceries", "Food & Groceries", "GROCERIES"],
    "Travel & Hospitality": ["Travel & Hospitality", "Travel", "Hospitality", "travel"],
    "Health & Beauty":      ["Health & Beauty", "Health", "health & beauty", "Beauty"],
    "Financial Services":   ["Financial Services", "FinServ", "financial services", "Finance"],
    "Entertainment":        ["Entertainment", "entertainment", "Media & Entertainment"],
    "Education":            ["Education", "education", "EdTech"],
    "Home & Furniture":     ["Home & Furniture", "Home", "home & furniture", "Furniture"],
    "Automotive":           ["Automotive", "automotive", "Auto"],
}

STATUS_DIRTY = {
    "Completed": ["Completed", "completed", "SUCCESS", "success", "Complete"],
    "Failed":    ["Failed", "failed", "FAILED", "Failure"],
    "Pending":   ["Pending", "pending", "In Progress", "PENDING"],
    "Declined":  ["Declined", "declined", "Rejected", "DECLINED"],
    "Refunded":  ["Refunded", "refunded", "REFUNDED"],
}

COUNTRY_DIRTY = {   # sometimes ISO code used instead
    "Kenya": ["Kenya", "KE"], "Nigeria": ["Nigeria", "NG"],
    "South Africa": ["South Africa", "ZA", "SA"], "Ghana": ["Ghana", "GH"],
    "Egypt": ["Egypt", "EG"], "Tanzania": ["Tanzania", "TZ"],
    "Uganda": ["Uganda", "UG"], "United States": ["United States", "USA", "US"],
    "United Kingdom": ["United Kingdom", "UK", "GB"],
    "India": ["India", "IN"], "Germany": ["Germany", "DE"],
    "France": ["France", "FR"],
}

# ──────────────────────────────────────────────
# DATE FORMAT VARIANTS
# ──────────────────────────────────────────────
DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d-%b-%Y", "%Y/%m/%d"]

def random_date_str(dt):
    fmt = np.random.choice(DATE_FORMATS, p=[0.55, 0.20, 0.10, 0.08, 0.07])
    return dt.strftime(fmt)

# ──────────────────────────────────────────────
# HELPER — pick dirty variant
# ──────────────────────────────────────────────
def dirty(val, mapping, dirt_prob=0.35):
    if random.random() < dirt_prob:
        return random.choice(mapping[val])
    return val

# ──────────────────────────────────────────────
# MERCHANT TABLE  (fixed set for referential integrity)
# ──────────────────────────────────────────────
N_MERCHANTS = 300
merchant_ids   = [f"MER{str(i).zfill(5)}" for i in range(1, N_MERCHANTS + 1)]
merchant_names = [fake.company() for _ in range(N_MERCHANTS)]
merchant_df    = dict(zip(merchant_ids, merchant_names))

# ──────────────────────────────────────────────
# CUSTOMER TABLE
# ──────────────────────────────────────────────
N_CUSTOMERS = 15_000
customer_ids = [f"CUST{str(i).zfill(6)}" for i in range(1, N_CUSTOMERS + 1)]
# CLV follows a log-normal distribution; some nulls injected later
customer_clv = np.random.lognormal(mean=6.5, sigma=1.2, size=N_CUSTOMERS)

# ──────────────────────────────────────────────
# CORE GENERATION LOOP
# ──────────────────────────────────────────────
print(f"Generating {N_ROWS:,} transactions...")

records = []
date_range = pd.date_range(START_DATE, END_DATE, freq="h")

countries_list = list(COUNTRIES.keys())
country_probs  = list(COUNTRIES.values())

for i in tqdm(range(N_ROWS)):
    # ── Date (seasonal weighting: Q4 peaks)
    month_weights = np.array([1,1,1.1,1.1,1.1,1.2,1.2,1.3,1.3,1.5,1.6,2.0])
    month = np.random.choice(range(1, 13), p=month_weights / month_weights.sum())
    year  = np.random.choice([2022, 2023, 2024], p=[0.28, 0.36, 0.36])
    try:
        day  = np.random.randint(1, 29)
        dt   = pd.Timestamp(year=year, month=month, day=day,
                            hour=np.random.randint(0, 24),
                            minute=np.random.randint(0, 60))
    except Exception:
        dt = pd.Timestamp(START_DATE)

    # ── Geography
    country_clean    = np.random.choice(countries_list, p=country_probs)
    currency         = CURRENCY_MAP[country_clean]
    exchange_rate    = EXCHANGE_RATES[currency]

    # ── Customer
    cust_idx         = np.random.randint(0, N_CUSTOMERS)
    customer_id      = customer_ids[cust_idx]
    clv              = float(np.round(customer_clv[cust_idx], 2))
    age              = int(np.clip(np.random.normal(35, 12), 18, 75))
    segment_clean    = np.random.choice(CUSTOMER_SEGMENTS_CLEAN,
                                        p=[0.35, 0.25, 0.15, 0.15, 0.10])

    # ── Merchant
    merchant_id   = random.choice(merchant_ids)
    merchant_name = merchant_df[merchant_id]

    # ── Transaction
    transaction_id = str(uuid.uuid4())[:18].upper()
    product_clean  = np.random.choice(PRODUCT_CATEGORIES_CLEAN)
    payment_clean  = np.random.choice(PAYMENT_METHODS_CLEAN,
                                      p=[0.20, 0.18, 0.15, 0.12, 0.10,
                                         0.07, 0.07, 0.04, 0.04, 0.03])
    status_clean   = np.random.choice(TRANSACTION_STATUSES_CLEAN,
                                      p=[0.75, 0.08, 0.07, 0.06, 0.04])
    device_clean   = np.random.choice(DEVICE_TYPES, p=[0.65, 0.25, 0.10])
    platform_clean = np.random.choice(PLATFORMS_CLEAN, p=[0.38, 0.22, 0.20, 0.12, 0.08])

    # Amount: log-normal, varies by segment and category
    base_amount = np.random.lognormal(mean=4.5, sigma=1.3)
    if segment_clean == "Corporate":
        base_amount *= 3.5
    elif segment_clean == "Premium":
        base_amount *= 2.0
    amount_local = float(np.round(base_amount, 2))
    amount_usd   = float(np.round(amount_local * exchange_rate, 2))

    # Discount (0–0.4 range normally)
    discount     = float(np.round(np.random.beta(1.5, 8), 4))
    net_revenue  = float(np.round(amount_usd * (1 - discount), 2))

    # Fraud (2% base; higher for Crypto and cross-border)
    fraud_prob = 0.02
    if payment_clean == "Crypto Wallet":
        fraud_prob = 0.06
    if country_clean in ["Nigeria", "Ghana"]:
        fraud_prob += 0.01
    is_fraud     = int(np.random.random() < fraud_prob)
    chargeback   = int(is_fraud and np.random.random() < 0.35)

    # Session duration (seconds)
    session_dur  = float(np.round(np.random.lognormal(mean=5.5, sigma=1.1), 1))

    # ── Apply dirt
    country_val    = dirty(country_clean, COUNTRY_DIRTY, 0.25)
    payment_val    = dirty(payment_clean, PAYMENT_DIRTY, 0.35)
    segment_val    = dirty(segment_clean, SEGMENT_DIRTY, 0.30)
    platform_val   = dirty(platform_clean, PLATFORM_DIRTY, 0.30)
    category_val   = dirty(product_clean, CATEGORY_DIRTY, 0.30)
    status_val     = dirty(status_clean, STATUS_DIRTY, 0.25)
    date_str       = random_date_str(dt)

    records.append({
        "transaction_id":          transaction_id,
        "transaction_date":        date_str,
        "customer_id":             customer_id,
        "customer_age":            age,
        "customer_segment":        segment_val,
        "country":                 country_val,
        "payment_method":          payment_val,
        "transaction_amount_usd":  amount_usd,
        "currency":                currency,
        "exchange_rate":           exchange_rate,
        "product_category":        category_val,
        "merchant_id":             merchant_id,
        "merchant_name":           merchant_name,
        "transaction_status":      status_val,
        "is_fraud":                is_fraud,
        "device_type":             device_clean,
        "platform":                platform_val,
        "session_duration_sec":    session_dur,
        "chargeback_flag":         chargeback,
        "discount_applied":        discount,
        "net_revenue_usd":         net_revenue,
        "customer_lifetime_value": clv,
    })

df = pd.DataFrame(records)
print(f"Base records generated: {len(df):,}")

# ──────────────────────────────────────────────
# INJECT SPECIFIC DATA QUALITY ISSUES
# ──────────────────────────────────────────────
print("Injecting data quality issues...")

# 1. Duplicate rows (~1.5%)
n_dups = int(N_ROWS * 0.015)
dup_rows = df.sample(n_dups, random_state=7)
df = pd.concat([df, dup_rows], ignore_index=True)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)   # shuffle
print(f"  + {n_dups:,} duplicate rows injected")

# 2. Outlier ages
age_outlier_idx = df.sample(int(N_ROWS * 0.005), random_state=1).index
df.loc[age_outlier_idx, "customer_age"] = np.random.choice([999, 0, -5, 150],
                                                            size=len(age_outlier_idx))
print(f"  + {len(age_outlier_idx):,} outlier ages injected")

# 3. Extreme transaction amounts (fat-tail outliers)
amount_outlier_idx = df.sample(int(N_ROWS * 0.003), random_state=2).index
df.loc[amount_outlier_idx, "transaction_amount_usd"] = np.random.uniform(50_000, 500_000,
                                                                          size=len(amount_outlier_idx))
print(f"  + {len(amount_outlier_idx):,} extreme transaction amounts injected")

# 4. Discount > 1.0 (data entry error)
discount_idx = df.sample(int(N_ROWS * 0.008), random_state=3).index
df.loc[discount_idx, "discount_applied"] = np.random.uniform(1.1, 2.5,
                                                              size=len(discount_idx))
print(f"  + {len(discount_idx):,} invalid discounts (>100%) injected")

# 5. Negative session durations
neg_session_idx = df.sample(int(N_ROWS * 0.006), random_state=4).index
df.loc[neg_session_idx, "session_duration_sec"] = np.random.uniform(-500, -1,
                                                                      size=len(neg_session_idx))
print(f"  + {len(neg_session_idx):,} negative session durations injected")

# 6. Null values — simulate missing data patterns
null_specs = [
    ("transaction_amount_usd", 0.030),
    ("exchange_rate",          0.040),
    ("customer_lifetime_value",0.055),
    ("transaction_status",     0.025),
    ("session_duration_sec",   0.020),
    ("discount_applied",       0.015),
]
for col, rate in null_specs:
    null_idx = df.sample(int(len(df) * rate), random_state=hash(col) % 99).index
    df.loc[null_idx, col] = np.nan
    print(f"  + {len(null_idx):,} nulls in '{col}'")

# 7. Free-text values in transaction_status (simulate dropdown bypass)
freetext_idx = df.sample(int(N_ROWS * 0.01), random_state=5).index
free_texts = ["ok", "done", "N/A", "not sure", "check later", "error", "?", "n/a", "TBD"]
df.loc[freetext_idx, "transaction_status"] = np.random.choice(free_texts,
                                                               size=len(freetext_idx))
print(f"  + {len(freetext_idx):,} free-text entries in 'transaction_status'")

# 8. CLV format inconsistency (some stored as strings with $ sign)
clv_str_idx = df.sample(int(N_ROWS * 0.03), random_state=6).index
df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(object)
df.loc[clv_str_idx, "customer_lifetime_value"] = df.loc[clv_str_idx,
    "customer_lifetime_value"].apply(lambda x: f"${float(x):,.2f}" if pd.notna(x) else np.nan)
print(f"  + {len(clv_str_idx):,} CLV values stored as '$-formatted' strings")

# ──────────────────────────────────────────────
# SAVE
# ──────────────────────────────────────────────
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nDataset saved: {OUTPUT_FILE}")
print(f"Total rows:    {len(df):,}")
print(f"Total columns: {len(df.columns)}")
print("\nColumn summary:")
print(df.dtypes.to_string())
print("\nNull counts:")
print(df.isnull().sum()[df.isnull().sum() > 0].to_string())
print("\nSample (first 3 rows):")
print(df.head(3).to_string())
print("\nAll done. Load 'fintech_payments_raw.csv' into Pandas to begin cleaning.")
