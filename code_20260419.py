import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 页面基础设置
st.set_page_config(
    page_title="Premier League Economic Impact Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 页面标题与开发者信息
st.title("Premier League Economic Impact Analysis")
st.markdown("**Developer:** Yongjin.Chen | **Student ID:** 2468705")
st.divider()

# ---------------- 1. 读取数据 ----------------
df = pd.read_csv("pl_economic_data.csv")
df.columns = df.columns.str.strip()

# ---------------- 2. 数据概览模块 ----------------
st.subheader("📊 Dataset Overview")
st.dataframe(df, use_container_width=True)
st.divider()

# ---------------- 3. 侧边栏筛选模块 ----------------
st.sidebar.header("Filter Options")
selected_year = st.sidebar.selectbox("Select Season Year", sorted(df["year"].unique()))
selected_league = st.sidebar.selectbox("Select League", df["league"].unique())

# 筛选后的数据
filtered_df = df[(df["year"] == selected_year) & (df["league"] == selected_league)]
st.subheader(f"📈 {selected_year} Season - {selected_league} Detailed Data")
st.dataframe(filtered_df, use_container_width=True)
st.divider()

# ---------------- 4. 图表1：收入vs支出对比 ----------------
st.subheader("💰 Club Revenue vs Spending")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(filtered_df["team"], filtered_df["revenue_million"], label="Revenue (Million £)", color="#1f77b4")
ax1.bar(filtered_df["team"], filtered_df["spending_million"], label="Spending (Million £)", color="#ff7f0e", alpha=0.7)
ax1.set_ylabel("Million £")
ax1.set_title(f"Revenue vs Spending - {selected_year} Season")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
st.pyplot(fig1)
st.divider()

# ---------------- 5. 图表2：积分趋势 ----------------
st.subheader("🏆 Club Points Performance")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(filtered_df["team"], filtered_df["points"], marker='o', linewidth=2, color="#2ca02c")
ax2.set_ylabel("Points")
ax2.set_title(f"Team Points - {selected_year} Season")
plt.xticks(rotation=45, ha="right")
plt.grid(alpha=0.3)
plt.tight_layout()
st.pyplot(fig2)
st.divider()

# ---------------- 6. 结论与分析模块 ----------------
st.subheader("📌 Key Findings & Conclusions")
st.markdown("""
1.  **Financial Performance vs On-Field Results**
    Higher revenue clubs generally spend more on transfers and wages, which correlates with better league performance.
2.  **Efficiency Differences Between Clubs**
    Manchester City and Liverpool show strong performance with efficient spending, while some high-spending clubs underperform.
3.  **Trend Over Seasons**
    Spending power has grown steadily across the Premier League, with top clubs widening the financial gap.
""")
