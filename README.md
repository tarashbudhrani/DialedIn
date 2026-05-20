<div align="center">

# 📱DialedIn: Smartphone Data Pipeline

### End-to-End Data Engineering & Analytics Project

> **Scraped → Cleaned → Analyzed → Visualized** — 10,000 smartphone records, zero manual work.

</div>

---

## 🗺️ Pipeline at a Glance

```
🌐 Web Scraping          🧹 Data Cleaning         📊 EDA                   🖥️ Dashboard
─────────────────        ─────────────────        ─────────────────        ─────────────────
Selenium Chrome    ──►   Strip symbols      ──►   Univariate plots   ──►   Streamlit App
10,000 records           Fix data types           Bivariate analysis        Interactive filters
Dynamic pages            Handle missing           ANOVA / Chi²  tests       Live charts
Auto pagination          Remove duplicates        Brand insights            Visual KPIs
```

---

## 🔢 By the Numbers

| Stage | What Happened |
|---|---|
| 🕷️ **Scraped** | 10,000 records across 30+ smartphone brands |
| 🗑️ **Dropped** | Feature phones, duplicates, incomplete rows |
| 🔧 **Engineered** | 15+ columns parsed from raw messy strings |
| 📈 **Analyzed** | Univariate + Bivariate + Statistical tests |
| 🎛️ **Visualized** | Interactive Streamlit dashboard |

---

## ⚙️ Stage 1 — Web Scraping with Selenium

> Automated Chrome to paginate through 10,000+ listings.

```python
driver.get("https://smartprix.com/mobiles")
# Auto-scroll → extract cards → paginate → save to CSV
```

**Captured fields:** `brand`, `model`, `price`, `rating`, `processor`, `RAM`, `storage`,
`battery`, `display`, `camera`, `OS`, `5G support`, `fast charging`

---

## 🧹 Stage 2 — Data Cleaning

> Raw data is messy. Every column needed surgery.

| Column | Raw Value | Cleaned Value |
|---|---|---|
| `price` | `₹1,29,990` | `129990.0` |
| `processor` | `Snapdragon 8 Gen 3, 4×3.3GHz Octa core` | `brand=Qualcomm, cores=8, speed=3.3` |
| `battery` | `5000mAh, 65W Fast Charging` | `capacity=5000, fast_charge=True, watts=65` |
| `display` | `6.7 inches, 120Hz, 1440×3200` | `size=6.7, refresh=120, resolution=...` |
| `camera` | `50MP + 12MP + 10MP, 12MP front` | `num_cameras=3, rear_res=50` |

**Key cleaning decisions:**
- 🚫 Removed **feature phones** (price < ₹4,000 OR battery < 2,000mAh OR screen < 4")
- 🔄 Converted 7 float columns → int; `fast_charging` → bool
- 🧩 Split compound columns into atomic features using `regex`

---

## 🔍 Stage 3 — Exploratory Data Analysis

### Univariate
- Top 5 brands by volume → **Samsung dominates at ~28%**
- Price distribution is **right-skewed** → log-transformed for analysis
- Most common RAM: **8GB**, Storage: **128GB**, Refresh Rate: **60Hz**

### Bivariate
- `rating` vs `number_of_cores` → 8-core phones rate highest on average
- `price` vs `brand` → **ANOVA confirms** brand significantly impacts price (`p < 0.05`)
- `brand` vs `number_of_cores` → **Chi² confirms** dependency between brand and chipset tier

### Missing Value Strategy

```
MCAR (random) ──► mean / median / mode fill
MAR  (pattern) ──► brand-wise groupby mean  ──► rating column
MNAR (structural) ──► dropped rows
```

| Column | Imputation Method |
|---|---|
| `rating` | Brand-wise mean via `groupby().transform()` |
| `memory`, `storage` | Mode |
| `refresh_rate` | Default → 60Hz |
| `num_of_cameras` | Inferred from `rear_camera` presence |

---

## 🖥️ Stage 4 — Streamlit Dashboard

> Filter by brand, price range, RAM, 5G support — charts update live.

**Dashboard includes:**
- 📊 Value count charts per categorical column
- 🥧 Pie chart — brand market share
- 📦 Box plots — price distribution by brand
- 🌊 KDE curves — rating distributions
- 🔗 Correlation heatmap — numeric features

---

## 🗂️ Project Structure

```
📦 smartphone-intelligence/
├── 🕷️  scraper/
│   └── selenium_scraper.py       # Web scraping pipeline
├── 🧹  notebooks/
│   ├── Data_Cleaning_Case_Study.ipynb
│   ├── EDA_on_smartphones_dataset.ipynb
│   └── EDA_Impute_Missing_Values.ipynb
├── 🖥️  app/
│   ├── main.py                   # Streamlit analytics dashboard
│   ├── app.py                    # UI components demo
│   └── interactive.py            # Widget playground
├── 📁  data/
│   ├── smartphones_raw.csv
│   └── smartphones_cleaned.csv
└── 📄  requirements.txt
```

---


---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Scraping | `Selenium`, `ChromeDriver` |
| Wrangling | `Pandas`, `NumPy`, `Regex` |
| Analysis | `SciPy` (ANOVA, Chi²), `Missingno` |
| Visualization | `Matplotlib`, `Seaborn`, `Plotly` |
| Dashboard | `Streamlit` |

---

<div align="center">

**Built end-to-end — from raw HTML to live dashboard — without a single manually edited cell.**

⭐ Star this repo if it helped you | 🍴 Fork to extend it

</div>
