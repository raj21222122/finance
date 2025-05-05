"""
Module for data visualization components for the finance education dashboard.
Contains visualization functions for each financial module.
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Insurance data visualizations
insurance_data = {
    "Insurance Type": ["Life", "Health", "Motor", "Home", "Travel"],
    "Coverage (%)": [85, 65, 90, 45, 30],
    "Premium Growth (%)": [12, 18, 8, 5, 15],
    "Claims Ratio (%)": [65, 80, 75, 45, 30]
}

insurance_df = pd.DataFrame(insurance_data)

# Equity data visualizations
equity_data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Returns (%)": [12, -3, 28, -8, 14, 18, 22, -12, 15, 10],
    "Market Cap (Trillion ₹)": [1.2, 1.3, 1.8, 1.5, 1.7, 2.0, 2.5, 2.2, 2.7, 3.0]
}

equity_df = pd.DataFrame(equity_data)

# PMS & AIF data visualizations
pms_aif_data = {
    "Category": ["Category I AIF", "Category II AIF", "Category III AIF", "PMS"],
    "Assets Under Management (Billion ₹)": [250, 650, 450, 350],
    "Average Returns (%)": [12, 15, 18, 14],
    "Minimum Investment (Lakhs ₹)": [50, 50, 50, 25]
}

pms_aif_df = pd.DataFrame(pms_aif_data)

# Stocks data visualizations
stocks_data = {
    "Sector": ["IT", "Banking", "Pharma", "FMCG", "Auto", "Energy"],
    "Market Share (%)": [22, 28, 15, 12, 10, 13],
    "YoY Growth (%)": [15, 12, 18, 8, 5, 10],
    "P/E Ratio": [25, 18, 22, 35, 20, 12]
}

stocks_df = pd.DataFrame(stocks_data)

# Bonds data visualizations
bonds_data = {
    "Bond Type": ["Government", "Corporate AAA", "Corporate AA", "Corporate A", "Municipal"],
    "Yield (%)": [7.2, 8.1, 9.5, 10.8, 7.8],
    "Duration (Years)": [10, 5, 7, 3, 8],
    "Risk Score (1-10)": [2, 4, 6, 8, 3]
}

bonds_df = pd.DataFrame(bonds_data)

# Visualization functions for each module
def insurance_visualizations():
    """Display insurance visualizations"""
    st.subheader("Insurance Market Data")
    
    # Coverage by insurance type
    fig1 = px.bar(
        insurance_df, 
        x="Insurance Type", 
        y="Coverage (%)",
        title="Insurance Coverage by Type",
        color="Insurance Type",
        labels={"Coverage (%)": "Market Coverage (%)"}
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Premium growth vs claims ratio
    fig2 = px.scatter(
        insurance_df,
        x="Premium Growth (%)",
        y="Claims Ratio (%)",
        size="Coverage (%)",
        color="Insurance Type",
        title="Premium Growth vs Claims Ratio",
        labels={"Premium Growth (%)": "Annual Premium Growth (%)", "Claims Ratio (%)": "Claims Ratio (%)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("Insurance Market Data")
    st.dataframe(insurance_df, hide_index=True)
    
    # Download option
    csv = insurance_df.to_csv(index=False)
    st.download_button(
        label="Download Insurance Data as CSV",
        data=csv,
        file_name="insurance_market_data.csv",
        mime="text/csv"
    )

def equity_visualizations():
    """Display equity visualizations"""
    st.subheader("Equity Market Performance")
    
    # Equity returns over years
    fig1 = px.line(
        equity_df, 
        x="Year", 
        y="Returns (%)",
        title="Equity Market Returns Over Time",
        markers=True,
        labels={"Returns (%)": "Annual Returns (%)"}
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Market cap growth
    fig2 = px.area(
        equity_df,
        x="Year",
        y="Market Cap (Trillion ₹)",
        title="Market Capitalization Growth",
        labels={"Market Cap (Trillion ₹)": "Market Capitalization (Trillion ₹)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("Equity Market Data")
    st.dataframe(equity_df, hide_index=True)
    
    # Download option
    csv = equity_df.to_csv(index=False)
    st.download_button(
        label="Download Equity Data as CSV",
        data=csv,
        file_name="equity_market_data.csv",
        mime="text/csv"
    )

def pms_aif_visualizations():
    """Display PMS & AIF visualizations"""
    st.subheader("PMS & AIF Market Data")
    
    # AUM Comparison
    fig1 = px.bar(
        pms_aif_df, 
        x="Category", 
        y="Assets Under Management (Billion ₹)",
        title="Assets Under Management by Category",
        color="Category",
        labels={"Assets Under Management (Billion ₹)": "AUM (Billion ₹)"}
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Returns vs Minimum Investment
    fig2 = px.scatter(
        pms_aif_df,
        x="Minimum Investment (Lakhs ₹)",
        y="Average Returns (%)",
        size="Assets Under Management (Billion ₹)",
        color="Category",
        title="Returns vs Minimum Investment",
        labels={"Average Returns (%)": "Average Annual Returns (%)", "Minimum Investment (Lakhs ₹)": "Minimum Investment (Lakhs ₹)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("PMS & AIF Data")
    st.dataframe(pms_aif_df, hide_index=True)
    
    # Download option
    csv = pms_aif_df.to_csv(index=False)
    st.download_button(
        label="Download PMS & AIF Data as CSV",
        data=csv,
        file_name="pms_aif_data.csv",
        mime="text/csv"
    )

def stocks_visualizations():
    """Display stocks visualizations"""
    st.subheader("Stock Market Sector Analysis")
    
    # Market share by sector
    fig1 = px.pie(
        stocks_df, 
        values="Market Share (%)", 
        names="Sector",
        title="Market Share by Sector",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Growth vs P/E Ratio
    fig2 = px.scatter(
        stocks_df,
        x="P/E Ratio",
        y="YoY Growth (%)",
        size="Market Share (%)",
        color="Sector",
        title="Growth vs P/E Ratio by Sector",
        labels={"YoY Growth (%)": "Year-on-Year Growth (%)", "P/E Ratio": "Price-to-Earnings Ratio"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("Stock Market Sector Data")
    st.dataframe(stocks_df, hide_index=True)
    
    # Download option
    csv = stocks_df.to_csv(index=False)
    st.download_button(
        label="Download Stock Market Data as CSV",
        data=csv,
        file_name="stock_market_data.csv",
        mime="text/csv"
    )

def bonds_visualizations():
    """Display bonds visualizations"""
    st.subheader("Bond Market Analysis")
    
    # Yield comparison
    fig1 = px.bar(
        bonds_df, 
        x="Bond Type", 
        y="Yield (%)",
        title="Bond Yields by Type",
        color="Bond Type",
        labels={"Yield (%)": "Current Yield (%)"}
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Risk vs Duration vs Yield
    fig2 = px.scatter(
        bonds_df,
        x="Duration (Years)",
        y="Risk Score (1-10)",
        size="Yield (%)",
        color="Bond Type",
        title="Risk vs Duration vs Yield",
        labels={"Risk Score (1-10)": "Risk Score (1-10)", "Duration (Years)": "Duration (Years)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("Bond Market Data")
    st.dataframe(bonds_df, hide_index=True)
    
    # Download option
    csv = bonds_df.to_csv(index=False)
    st.download_button(
        label="Download Bond Market Data as CSV",
        data=csv,
        file_name="bond_market_data.csv",
        mime="text/csv"
    )

# Function to generate real-world examples for each module
def get_real_world_examples(module):
    """Return real-world examples for the specified module"""
    examples = {
        "Insurance": [
            {
                "title": "Health Insurance Success Story",
                "content": """
                Rahul, a 45-year-old software engineer, purchased a comprehensive health insurance policy for ₹10 lakhs 
                coverage with a premium of ₹15,000 per year. Six months later, he was diagnosed with a critical illness 
                requiring surgery. The total hospital bill came to ₹8 lakhs, which was fully covered by his insurance 
                policy. Without insurance, this medical emergency would have depleted his savings.
                
                Key takeaway: A relatively small annual premium protected him from a significant financial burden.
                """
            },
            {
                "title": "Term Life Insurance Case Study",
                "content": """
                Priya, a 35-year-old mother of two, purchased a 30-year term life insurance policy with ₹1 crore coverage 
                for a premium of ₹12,000 per year. After 5 years, she unfortunately passed away in an accident. Her family 
                received the full sum assured of ₹1 crore, which helped provide financial security for her children's education 
                and daily expenses.
                
                Key takeaway: For a total investment of ₹60,000 (5 years of premium), her family received financial protection 
                of ₹1 crore, demonstrating the high protection value of term insurance.
                """
            }
        ],
        "Equity": [
            {
                "title": "Long-term SIP Investment",
                "content": """
                Vikram started a SIP (Systematic Investment Plan) in an equity mutual fund with just ₹5,000 per month at age 25. 
                He consistently invested for 25 years without withdrawing. By age 50, his monthly investment of ₹5,000 (total 
                investment of ₹15 lakhs) had grown to approximately ₹1.2 crores, thanks to the power of compounding and an 
                average annual return of 12% from the equity market.
                
                Key takeaway: Starting early and staying invested through market cycles can lead to substantial wealth creation.
                """
            },
            {
                "title": "Value Investing Success",
                "content": """
                Neha researched and invested ₹2 lakhs in a fundamentally strong but undervalued company during the market 
                crash of 2020. She identified the company based on strong fundamentals, low debt, and consistent dividend 
                history. By 2023, as the company's true value was recognized by the market, her investment had grown to 
                ₹8 lakhs, a 300% return in just three years.
                
                Key takeaway: Thorough research and investing during market corrections can yield exceptional returns when 
                investing in quality companies.
                """
            }
        ],
        "PMS & AIF": [
            {
                "title": "High Net Worth Portfolio Transformation",
                "content": """
                Rajiv, with investable assets of ₹2 crores, moved from traditional mutual funds to a professionally managed 
                PMS. The portfolio manager created a customized strategy focusing on emerging sectors and special situations. 
                Despite the higher fee structure (2% management fee plus 20% performance fee), Rajiv's portfolio generated 
                returns of 22% annually over 5 years compared to the 14% from his previous mutual fund investments.
                
                Key takeaway: Customized portfolio management can justify higher fees through superior performance for larger portfolios.
                """
            },
            {
                "title": "Alternative Investment Fund Performance",
                "content": """
                A group of investors participated in a Category II AIF focused on pre-IPO and late-stage private companies. 
                With a minimum investment of ₹1 crore each, the fund invested in 12 companies over its 5-year tenure. When 
                the fund exited, investors received a total return of 25% CAGR, significantly outperforming public markets 
                during the same period which delivered 12% CAGR.
                
                Key takeaway: Access to private market opportunities through AIFs can provide portfolio diversification and 
                potentially higher returns, albeit with higher minimum investment requirements and lower liquidity.
                """
            }
        ],
        "Stocks": [
            {
                "title": "Blue-chip Long-term Holding",
                "content": """
                Suresh invested ₹5 lakhs in shares of a leading Indian IT company in 2010, buying at ₹150 per share. 
                He held onto these shares through multiple market cycles, including temporary downturns. By 2025, the 
                share price had reached ₹3,800, and he had received substantial dividends throughout this period. His 
                initial investment had grown to approximately ₹1.25 crores, representing a 25x return over 15 years.
                
                Key takeaway: Investing in quality businesses and having the patience to hold through market cycles can 
                create significant wealth.
                """
            },
            {
                "title": "Sector Rotation Strategy",
                "content": """
                Meera implemented a sector rotation strategy by monitoring economic indicators and moving her ₹10 lakh 
                portfolio between different sectors based on the business cycle. She moved from defensive sectors (FMCG, 
                Pharma) during economic uncertainty to cyclical sectors (Banking, IT) during economic expansion. This 
                active strategy helped her generate 18% annualized returns over 10 years, compared to the market average 
                of 12%.
                
                Key takeaway: Understanding macroeconomic trends and adjusting sector allocation accordingly can enhance 
                investment returns.
                """
            }
        ],
        "Bonds": [
            {
                "title": "Laddered Bond Portfolio",
                "content": """
                Anand, a retiree, created a bond ladder with his ₹50 lakh corpus by investing ₹10 lakhs each in government 
                bonds maturing in 1, 2, 3, 4, and 5 years. This provided him with predictable income while managing interest 
                rate risk. When each bond matured, he reinvested in a new 5-year bond. This strategy provided him with an 
                average yield of 7.5% with minimal risk, ensuring a steady income stream during retirement.
                
                Key takeaway: Bond laddering can help create predictable income while managing interest rate fluctuations.
                """
            },
            {
                "title": "Corporate Bond Opportunity",
                "content": """
                During a period of market volatility, Kiran identified AA-rated corporate bonds of a fundamentally strong 
                company trading at a significant discount due to temporary market fears. She invested ₹15 lakhs in these 
                bonds yielding 9.5% when similar-rated bonds were yielding only 7.8%. As market fears subsided, the bond 
                prices appreciated, and she received both the high coupon payments and capital appreciation when she sold 
                a portion of her holdings after two years.
                
                Key takeaway: Market inefficiencies in bond pricing can create opportunities for higher returns without 
                taking excessive credit risk.
                """
            }
        ]
    }
    
    return examples.get(module, [])