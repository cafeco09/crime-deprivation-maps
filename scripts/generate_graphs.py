from pathlib import Path
import shutil
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"
GRAPHS_DIR = ROOT / "graphs"

GRAPHS_DIR.mkdir(parents=True, exist_ok=True)

print(f"Repo root: {ROOT}")
print(f"Graphs folder: {GRAPHS_DIR}")

# Copy existing PNG infographics from assets/ to graphs/
if ASSETS_DIR.exists():
    for file in sorted(ASSETS_DIR.glob("*.png")):
        target = GRAPHS_DIR / file.name
        shutil.copy2(file, target)
        print(f"Copied: {target}")
else:
    print("No assets/ folder found. Skipping asset copy.")

# 1. Asylum support by selected local authority
area_file = DATA_DIR / "selected_area_metrics.csv"

if area_file.exists():
    df = pd.read_csv(area_file)

    if "supported_asylum_seekers_end_dec_2025" in df.columns:
        plot_df = df.sort_values("supported_asylum_seekers_end_dec_2025")

        plt.figure(figsize=(9, 5))
        plt.barh(plot_df["area"], plot_df["supported_asylum_seekers_end_dec_2025"])
        plt.title("Supported asylum seekers by selected local authority")
        plt.xlabel("Supported asylum seekers, end Dec 2025")

        for i, v in enumerate(plot_df["supported_asylum_seekers_end_dec_2025"]):
            plt.text(v + 40, i, f"{int(v):,}", va="center")

        plt.tight_layout()
        out = GRAPHS_DIR / "asylum_support_by_area.png"
        plt.savefig(out, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved: {out}")

    if "latest_recorded_crime_rate_per_1000" in df.columns:
        plot_df = df.sort_values("latest_recorded_crime_rate_per_1000")

        plt.figure(figsize=(9, 5))
        plt.barh(plot_df["area"], plot_df["latest_recorded_crime_rate_per_1000"])
        plt.title("Latest recorded crime-rate context")
        plt.xlabel("Recorded crimes per 1,000 residents")

        for i, v in enumerate(plot_df["latest_recorded_crime_rate_per_1000"]):
            plt.text(v + 2, i, f"{v:.2f}", va="center")

        plt.tight_layout()
        out = GRAPHS_DIR / "crime_rate_by_area.png"
        plt.savefig(out, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved: {out}")

    if "deprivation_context_scale_1_to_5" in df.columns:
        plot_df = df.sort_values("deprivation_context_scale_1_to_5")

        plt.figure(figsize=(9, 5))
        plt.barh(plot_df["area"], plot_df["deprivation_context_scale_1_to_5"])
        plt.title("Deprivation context scale")
        plt.xlabel("Context scale: lower to higher deprivation")
        plt.xlim(0, 5.5)

        for i, v in enumerate(plot_df["deprivation_context_scale_1_to_5"]):
            plt.text(v + 0.1, i, f"{v}", va="center")

        plt.tight_layout()
        out = GRAPHS_DIR / "deprivation_context_scale.png"
        plt.savefig(out, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved: {out}")
else:
    print(f"Missing: {area_file}")

# 2. National asylum claimant nationality profile
nationality_file = DATA_DIR / "national_asylum_claimant_nationality_profile_2025.csv"

if nationality_file.exists():
    df = pd.read_csv(nationality_file)
    value_col = "share_of_uk_asylum_claimants_2025_percent"

    if value_col in df.columns:
        plot_df = df.sort_values(value_col)

        plt.figure(figsize=(9, 5))
        plt.barh(plot_df["nationality"], plot_df[value_col])
        plt.title("Top nationalities of UK asylum claimants, 2025")
        plt.xlabel("Share of UK asylum claimants (%)")

        for i, v in enumerate(plot_df[value_col]):
            plt.text(v + 0.2, i, f"{v:.0f}%", va="center")

        plt.figtext(
            0.5,
            -0.03,
            "Nationality is not ethnicity. This is national claimant data, not local-authority composition.",
            ha="center",
            fontsize=9,
            wrap=True,
        )

        plt.tight_layout()
        out = GRAPHS_DIR / "nationality_profile_asylum_claimants_2025.png"
        plt.savefig(out, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved: {out}")
else:
    print(f"Missing: {nationality_file}")

# 3. Annual aggregated crime-rate trend
trend_file = DATA_DIR / "annual_aggregated_crime_rates_2022_2025.csv"

if trend_file.exists():
    df = pd.read_csv(trend_file)

    plt.figure(figsize=(9, 5))

    if "birmingham_avg_quarterly_crimes_per_1000" in df.columns:
        plt.plot(df["year"], df["birmingham_avg_quarterly_crimes_per_1000"], marker="o", label="Birmingham")

    if "liverpool_avg_quarterly_crimes_per_1000" in df.columns:
        plt.plot(df["year"], df["liverpool_avg_quarterly_crimes_per_1000"], marker="o", label="Liverpool")

    if "manchester_avg_quarterly_crimes_per_1000" in df.columns:
        plt.plot(df["year"], df["manchester_avg_quarterly_crimes_per_1000"], marker="o", label="Manchester")

    plt.title("Annual aggregated recorded-crime rates, 2022–2025")
    plt.xlabel("Year")
    plt.ylabel("Average quarterly crimes per 1,000 residents")
    plt.xticks(df["year"])
    plt.grid(True, alpha=0.25)
    plt.legend()

    plt.tight_layout()
    out = GRAPHS_DIR / "annual_crime_rate_trend_2022_2025.png"
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")
else:
    print(f"Missing: {trend_file}")

# 4. Reoffending risk indicators
risk_file = DATA_DIR / "reoffending_risk_indicators.csv"

if risk_file.exists():
    df = pd.read_csv(risk_file)
    value_col = "adult_proven_reoffending_rate_percent"

    if value_col in df.columns:
        plot_df = df.sort_values(value_col)

        plt.figure(figsize=(10, 6))
        plt.barh(plot_df["risk_indicator"], plot_df[value_col])
        plt.title("Measured reoffending-risk indicators")
        plt.xlabel("Adult proven reoffending rate (%)")

        for i, v in enumerate(plot_df[value_col]):
            plt.text(v + 1, i, f"{v:.1f}%", va="center")

        plt.tight_layout()
        out = GRAPHS_DIR / "reoffending_risk_indicators.png"
        plt.savefig(out, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved: {out}")
else:
    print(f"Missing: {risk_file}")

print("Done. Graphs saved in graphs/")
