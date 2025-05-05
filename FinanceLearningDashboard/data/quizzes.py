"""
Quiz data for the finance education dashboard.
Contains quiz questions, options, correct answers, and explanations for each module.
"""

quiz_data = {
    "Insurance": [
        {
            "question": "What does the premium represent in an insurance policy?",
            "options": [
                "The amount you pay for insurance coverage", 
                "The maximum amount your insurer will pay for a loss", 
                "The amount you pay out-of-pocket before insurance coverage", 
                "A bonus payment from the insurer"
            ],
            "correct_answer": 0,
            "explanation": "Premium is the amount paid by the policyholder to the insurance company to maintain coverage. It's typically paid on a monthly, quarterly, or annual basis."
        },
        {
            "question": "Which type of life insurance provides coverage for a specific period?",
            "options": [
                "Whole Life Insurance", 
                "Term Life Insurance", 
                "Endowment Plan", 
                "Unit Linked Insurance Plan"
            ],
            "correct_answer": 1,
            "explanation": "Term Life Insurance provides coverage for a specific period (term) such as 10, 20, or 30 years. If the insured dies during this term, the beneficiary receives the death benefit."
        },
        {
            "question": "Under which section can you claim tax deduction for health insurance premiums in India?",
            "options": [
                "Section 80C", 
                "Section 80D", 
                "Section 10(10D)", 
                "Section 24"
            ],
            "correct_answer": 1,
            "explanation": "Section 80D allows deduction for health insurance premiums. Up to ₹25,000 for self, spouse, and children, with an additional ₹25,000 (or ₹50,000 for senior citizens) for parents."
        },
        {
            "question": "What is a claim settlement ratio?",
            "options": [
                "Percentage of premium returned if no claim is made", 
                "Ratio of insurance agents to customers", 
                "Percentage of claims settled by an insurer out of total claims received", 
                "Ratio of premium to sum assured"
            ],
            "correct_answer": 2,
            "explanation": "Claim settlement ratio is the percentage of claims settled by an insurance company out of the total claims received during a financial year. A higher ratio indicates better claim settlement practices."
        },
        {
            "question": "Which of the following is NOT a typical exclusion in health insurance policies?",
            "options": [
                "Pre-existing conditions for initial waiting period", 
                "Cosmetic surgery", 
                "Hospitalization due to accident", 
                "Self-inflicted injuries"
            ],
            "correct_answer": 2,
            "explanation": "Hospitalization due to accidents is typically covered by health insurance policies from day one. The other options are common exclusions in most health insurance policies."
        },
        {
            "question": "What is the primary role of IRDAI in the insurance sector?",
            "options": [
                "Selling insurance policies", 
                "Providing insurance coverage", 
                "Regulating the insurance industry", 
                "Offering financial advice"
            ],
            "correct_answer": 2,
            "explanation": "IRDAI (Insurance Regulatory and Development Authority of India) is the primary regulator for the insurance industry. It sets guidelines, protects policyholder interests, and ensures fair business practices."
        },
        {
            "question": "What is the difference between an indemnity health insurance plan and a fixed benefit plan?",
            "options": [
                "Indemnity plans have no waiting period while fixed benefit plans do", 
                "Indemnity plans reimburse actual expenses up to sum insured, while fixed benefit plans pay a predetermined amount", 
                "Fixed benefit plans cover pre-existing diseases from day one", 
                "Indemnity plans are only for senior citizens"
            ],
            "correct_answer": 1,
            "explanation": "Indemnity health insurance plans reimburse the actual medical expenses incurred up to the sum insured. Fixed benefit plans pay a predetermined amount regardless of the actual expenses incurred."
        },
        {
            "question": "What is the free-look period in insurance?",
            "options": [
                "Period where you can evaluate the insurance company's office", 
                "Time period to compare different insurance plans", 
                "Period during which you can review and return the policy if not satisfied", 
                "Time frame when premiums are waived"
            ],
            "correct_answer": 2,
            "explanation": "The free-look period (typically 15-30 days from receiving the policy document) allows the policyholder to review the policy terms and return it for a refund if they're not satisfied with it."
        },
        {
            "question": "Which factor does NOT typically affect your life insurance premium?",
            "options": [
                "Age", 
                "Occupation", 
                "Education level", 
                "Medical history"
            ],
            "correct_answer": 2,
            "explanation": "While age, occupation, and medical history are key factors in determining life insurance premiums, education level typically doesn't directly impact premium calculations."
        },
        {
            "question": "What is the purpose of reinsurance?",
            "options": [
                "To sell multiple insurance policies to the same customer", 
                "To transfer some risk from primary insurers to other insurance companies", 
                "To renew expired insurance policies", 
                "To provide insurance to people previously rejected by other insurers"
            ],
            "correct_answer": 1,
            "explanation": "Reinsurance is the practice where insurance companies transfer portions of their risk portfolios to other insurers to reduce the financial impact of large claims or catastrophic events."
        }
    ],
    "Equity": [
        {
            "question": "What does equity represent in a company?",
            "options": [
                "The company's debt", 
                "Ownership in the company", 
                "The company's annual revenue", 
                "The company's physical assets"
            ],
            "correct_answer": 1,
            "explanation": "Equity represents ownership in a company. When you own equity (shares) in a company, you own a portion of that business and have a claim on its assets and earnings."
        },
        {
            "question": "Which of the following is NOT a characteristic of common stock?",
            "options": [
                "Voting rights at shareholder meetings", 
                "Potential for dividends", 
                "Fixed dividend payments", 
                "Last claim on assets during liquidation"
            ],
            "correct_answer": 2,
            "explanation": "Fixed dividend payments are a characteristic of preferred stocks, not common stocks. Common stocks have variable dividends that are not guaranteed and depend on company performance and board decisions."
        },
        {
            "question": "What is market capitalization?",
            "options": [
                "The total debt of a company", 
                "The total value of a company's outstanding shares", 
                "The amount of capital held in cash reserves", 
                "The company's annual profit"
            ],
            "correct_answer": 1,
            "explanation": "Market capitalization (market cap) is the total value of a company's outstanding shares. It's calculated by multiplying the current share price by the total number of outstanding shares."
        },
        {
            "question": "What is the tax rate for long-term capital gains (LTCG) on equity investments exceeding ₹1 lakh in India?",
            "options": [
                "20% with indexation", 
                "15%", 
                "10% without indexation", 
                "Exempt from tax"
            ],
            "correct_answer": 2,
            "explanation": "Long-term capital gains (held for more than 12 months) on equity investments exceeding ₹1 lakh in a financial year are taxed at 10% without indexation in India."
        },
        {
            "question": "What is the difference between a primary and secondary market?",
            "options": [
                "Primary markets are for large investors, secondary for small investors", 
                "Primary markets are for IPOs, secondary for trading existing securities", 
                "Primary markets are for stocks, secondary for bonds", 
                "Primary markets are in major cities, secondary in smaller towns"
            ],
            "correct_answer": 1,
            "explanation": "The primary market is where new securities are issued and sold for the first time (like IPOs). The secondary market is where existing securities are traded among investors after issuance."
        },
        {
            "question": "What does P/E ratio measure?",
            "options": [
                "Price per share divided by earnings per share", 
                "Profit divided by equity", 
                "Price per share divided by book value per share", 
                "Projected earnings divided by current earnings"
            ],
            "correct_answer": 0,
            "explanation": "The Price-to-Earnings (P/E) ratio is calculated by dividing a company's current share price by its earnings per share (EPS). It indicates how much investors are willing to pay for each rupee of earnings."
        },
        {
            "question": "Which investment strategy focuses on companies with strong growth prospects, often trading at premium valuations?",
            "options": [
                "Value investing", 
                "Income investing", 
                "Growth investing", 
                "Index investing"
            ],
            "correct_answer": 2,
            "explanation": "Growth investing focuses on companies expected to grow their earnings at an above-average rate compared to the market. Growth investors are often willing to pay premium valuations for this future growth potential."
        },
        {
            "question": "What is a Systematic Investment Plan (SIP)?",
            "options": [
                "A one-time large investment in equity", 
                "A plan to systematically sell investments", 
                "Regular investments at fixed intervals", 
                "A government scheme for senior citizens"
            ],
            "correct_answer": 2,
            "explanation": "A Systematic Investment Plan (SIP) involves investing a fixed amount at regular intervals (typically monthly). It's a disciplined approach to equity investing that reduces the impact of market timing and benefits from rupee cost averaging."
        },
        {
            "question": "What is the minimum investment period for equity to be considered long-term for capital gains tax purposes in India?",
            "options": [
                "3 months", 
                "6 months", 
                "12 months", 
                "36 months"
            ],
            "correct_answer": 2,
            "explanation": "In India, equity investments held for more than 12 months are classified as long-term for capital gains tax purposes. Those held for 12 months or less are treated as short-term."
        },
        {
            "question": "Which of the following is NOT a common risk in equity investing?",
            "options": [
                "Market risk", 
                "Company-specific risk", 
                "Liquidity risk", 
                "Credit risk"
            ],
            "correct_answer": 3,
            "explanation": "Credit risk (the risk of default) is primarily associated with debt instruments like bonds, not equities. Equity investments face market risk, company-specific risk, and liquidity risk, among others."
        }
    ],
    "PMS & AIF": [
        {
            "question": "What is the minimum investment amount required for Portfolio Management Services (PMS) in India as per SEBI regulations?",
            "options": [
                "₹10 lakhs", 
                "₹25 lakhs", 
                "₹50 lakhs", 
                "₹1 crore"
            ],
            "correct_answer": 2,
            "explanation": "As per SEBI regulations, the minimum investment amount required for Portfolio Management Services (PMS) in India is ₹50 lakhs."
        },
        {
            "question": "In which type of PMS does the portfolio manager have full discretion over investment decisions?",
            "options": [
                "Advisory PMS", 
                "Non-discretionary PMS", 
                "Discretionary PMS", 
                "Mutual Fund PMS"
            ],
            "correct_answer": 2,
            "explanation": "In Discretionary PMS, the portfolio manager has full discretion over investment decisions. The client authorizes the manager to make all decisions based on the agreed investment strategy."
        },
        {
            "question": "What is the minimum investment amount for Alternative Investment Funds (AIFs) in India?",
            "options": [
                "₹25 lakhs", 
                "₹50 lakhs", 
                "₹75 lakhs", 
                "₹1 crore"
            ],
            "correct_answer": 3,
            "explanation": "The minimum investment amount for Alternative Investment Funds (AIFs) in India is ₹1 crore as per SEBI regulations."
        },
        {
            "question": "Which category of AIF includes venture capital funds and infrastructure funds?",
            "options": [
                "Category I AIF", 
                "Category II AIF", 
                "Category III AIF", 
                "Category IV AIF"
            ],
            "correct_answer": 0,
            "explanation": "Category I AIF includes venture capital funds, social venture funds, infrastructure funds, and SME funds. These are considered beneficial for the economy and receive favorable regulatory considerations."
        },
        {
            "question": "Which of the following is NOT a key difference between PMS and mutual funds?",
            "options": [
                "Ownership structure", 
                "Minimum investment amount", 
                "Customization level", 
                "Regulatory oversight"
            ],
            "correct_answer": 3,
            "explanation": "Both PMS and mutual funds are regulated by SEBI. The key differences are in ownership structure (direct ownership in PMS vs. units in mutual funds), minimum investment (₹50 lakhs for PMS vs. as low as ₹500 for mutual funds), and customization (tailored in PMS vs. standardized in mutual funds)."
        },
        {
            "question": "What is a 'high watermark' provision in PMS and AIF fee structures?",
            "options": [
                "Minimum investment threshold", 
                "Maximum management fee allowed", 
                "Provision ensuring performance fees are charged only after recovering previous losses", 
                "Highest NAV achieved by the fund"
            ],
            "correct_answer": 2,
            "explanation": "A high watermark provision ensures that the investment manager receives performance fees only after recovering any previous losses. This protects investors from paying performance fees multiple times for the same performance."
        },
        {
            "question": "Which of the following AIF categories employs complex trading strategies and may use leverage including through derivatives?",
            "options": [
                "Category I AIF", 
                "Category II AIF", 
                "Category III AIF", 
                "All of the above"
            ],
            "correct_answer": 2,
            "explanation": "Category III AIFs employ diverse or complex trading strategies and may use leverage including through derivatives. This category includes hedge funds, PIPE funds, and various strategy funds."
        },
        {
            "question": "What is 'carried interest' in the context of AIFs?",
            "options": [
                "Interest earned on cash balances", 
                "Performance fee paid to fund managers", 
                "Interest carried forward from previous years", 
                "Additional interest paid by defaulting investors"
            ],
            "correct_answer": 1,
            "explanation": "Carried interest, often called 'carry,' is the performance fee that fund managers receive as compensation. It's typically 20% of the fund's profits above a specified hurdle rate."
        },
        {
            "question": "Which performance measurement eliminates the impact of cash flows when evaluating investment returns?",
            "options": [
                "XIRR (Extended Internal Rate of Return)", 
                "TWRR (Time-Weighted Rate of Return)", 
                "Absolute Return", 
                "Compounded Annual Growth Rate (CAGR)"
            ],
            "correct_answer": 1,
            "explanation": "Time-Weighted Rate of Return (TWRR) eliminates the impact of cash flows when measuring investment performance. It's particularly useful for evaluating a manager's performance independent of the timing of client deposits and withdrawals."
        },
        {
            "question": "What is the tax treatment for income from Category I and II AIFs in India?",
            "options": [
                "Taxed at the fund level", 
                "Pass-through status where income is taxed in the hands of investors", 
                "Completely tax-exempt", 
                "Fixed rate of 10% tax at source"
            ],
            "correct_answer": 1,
            "explanation": "Category I and II AIFs enjoy pass-through status for income (except business income). This means the income is deemed to be directly received by investors and taxed in their hands according to their applicable tax rates."
        }
    ],
    "Stocks": [
        {
            "question": "What do stocks represent in a company?",
            "options": [
                "Loans made to the company", 
                "Company's physical inventory", 
                "Partial ownership in the company", 
                "Company's debt instruments"
            ],
            "correct_answer": 2,
            "explanation": "Stocks represent partial ownership in a company. When you buy a stock, you become a shareholder, owning a piece of that business with claims on its assets and earnings."
        },
        {
            "question": "What is the difference between common stock and preferred stock?",
            "options": [
                "Common stock is less expensive than preferred stock", 
                "Preferred stock typically has voting rights while common stock doesn't", 
                "Common stock has last claim on assets but usually has voting rights; preferred stock has higher claim on assets but usually no voting rights", 
                "There is no difference; they are different terms for the same thing"
            ],
            "correct_answer": 2,
            "explanation": "Common stock typically comes with voting rights but has the last claim on assets during liquidation. Preferred stock usually has no voting rights but has priority over common stock for dividends and asset claims during liquidation."
        },
        {
            "question": "What is market capitalization in the context of stocks?",
            "options": [
                "The maximum capital a company can raise", 
                "The total value of a company's outstanding shares", 
                "The amount of cash a company has on hand", 
                "The company's annual revenue"
            ],
            "correct_answer": 1,
            "explanation": "Market capitalization (market cap) is the total value of a company's outstanding shares, calculated by multiplying the current share price by the total number of shares outstanding."
        },
        {
            "question": "Which accounts are required to start trading stocks in India?",
            "options": [
                "Only a bank account", 
                "Trading account and bank account", 
                "Trading account, demat account, and bank account", 
                "Demat account and credit card"
            ],
            "correct_answer": 2,
            "explanation": "To trade stocks in India, you need three linked accounts: a trading account (to place buy/sell orders), a demat account (to hold shares in electronic form), and a bank account (for fund transfers)."
        },
        {
            "question": "What is a limit order in stock trading?",
            "options": [
                "An order to buy/sell a stock at the current market price", 
                "An order to buy/sell a stock only at a specified price or better", 
                "An order limiting the total number of shares you can buy", 
                "An order that limits your daily trading activity"
            ],
            "correct_answer": 1,
            "explanation": "A limit order is an instruction to buy or sell a stock only at a specified price or better. It ensures you don't pay more than a certain price when buying or sell for less than a certain price when selling."
        },
        {
            "question": "What is the settlement cycle for equity trades in India?",
            "options": [
                "T+1 (Trade date plus one day)", 
                "T+2 (Trade date plus two days)", 
                "T+3 (Trade date plus three days)", 
                "Same day settlement"
            ],
            "correct_answer": 1,
            "explanation": "The settlement cycle for equity trades in India is T+2, meaning trades are settled two business days after execution. For example, a trade executed on Monday would be settled on Wednesday."
        },
        {
            "question": "Which approach to stock analysis focuses on studying company financials, management quality, and competitive position?",
            "options": [
                "Technical analysis", 
                "Fundamental analysis", 
                "Quantitative analysis", 
                "Sentimental analysis"
            ],
            "correct_answer": 1,
            "explanation": "Fundamental analysis involves examining a company's financial statements, evaluating management quality, understanding the competitive landscape, and analyzing broader economic factors to determine a stock's intrinsic value."
        },
        {
            "question": "What is a P/E (Price-to-Earnings) ratio?",
            "options": [
                "The price of a stock divided by its earnings per share", 
                "The profit of a company divided by its equity", 
                "The percentage of earnings paid as dividends", 
                "The price of a stock divided by its book value"
            ],
            "correct_answer": 0,
            "explanation": "The Price-to-Earnings (P/E) ratio is calculated by dividing a company's current share price by its earnings per share (EPS). It indicates how much investors are willing to pay for each rupee of earnings."
        },
        {
            "question": "What is a stock split?",
            "options": [
                "Dividing a company into two separate entities", 
                "Splitting profits between shareholders and the company", 
                "Increasing the number of shares while proportionally decreasing share price", 
                "Separating voting rights from dividend rights"
            ],
            "correct_answer": 2,
            "explanation": "A stock split increases the number of shares while proportionally decreasing the share price, keeping the company's market capitalization unchanged. For example, in a 2:1 split, each share becomes two shares at half the original price."
        },
        {
            "question": "What is a circuit breaker in the context of stock markets?",
            "options": [
                "A device that prevents electronic trading systems from overheating", 
                "A mechanism that temporarily halts trading when market indices move significantly", 
                "A rule that limits the number of trades a single investor can make", 
                "A system that cuts off power to trading floors during emergencies"
            ],
            "correct_answer": 1,
            "explanation": "Circuit breakers are automatic mechanisms that temporarily halt trading when market indices fall by certain percentages. In India, they are triggered at three levels: 10%, 15%, and 20% movements in either direction to prevent panic-driven market crashes."
        }
    ],
    "Bonds": [
        {
            "question": "What is a bond?",
            "options": [
                "A share of ownership in a company", 
                "A debt instrument where investors lend money to an entity for a defined period", 
                "A derivative financial instrument", 
                "A real estate investment vehicle"
            ],
            "correct_answer": 1,
            "explanation": "A bond is a debt instrument where investors lend money to an entity (government or corporation) for a defined period at a specified interest rate. The entity promises to repay the principal at maturity and make periodic interest payments."
        },
        {
            "question": "What is the coupon rate of a bond?",
            "options": [
                "The total return expected if the bond is held until maturity", 
                "The annual interest rate paid on the bond's face value", 
                "The discount rate used to calculate the bond's present value", 
                "The rate at which the bond's value declines over time"
            ],
            "correct_answer": 1,
            "explanation": "The coupon rate is the annual interest rate paid on a bond's face value. It's fixed when the bond is issued and remains the same throughout the bond's life unless it's a floating-rate bond."
        },
        {
            "question": "What happens to bond prices when interest rates rise?",
            "options": [
                "Bond prices rise", 
                "Bond prices fall", 
                "Bond prices remain unchanged", 
                "It depends on the bond issuer"
            ],
            "correct_answer": 1,
            "explanation": "Bond prices move inversely to interest rates. When interest rates rise, existing bond prices fall because newer bonds offer higher yields. This makes existing bonds with lower coupon rates less attractive to investors."
        },
        {
            "question": "Which of the following is considered to have the lowest credit risk?",
            "options": [
                "Corporate bonds", 
                "Municipal bonds", 
                "Government securities (G-Secs)", 
                "High-yield bonds"
            ],
            "correct_answer": 2,
            "explanation": "Government securities (G-Secs) issued by the central government are considered to have the lowest credit risk among bond types because they're backed by the sovereign's ability to tax and print currency."
        },
        {
            "question": "What is yield to maturity (YTM)?",
            "options": [
                "The annual coupon payment divided by the bond's face value", 
                "The annual coupon payment divided by the bond's current market price", 
                "The total return expected if a bond is held until maturity, considering market price and time value of money", 
                "The yield earned if the bond is sold before maturity"
            ],
            "correct_answer": 2,
            "explanation": "Yield to maturity (YTM) is the total return anticipated if a bond is held until maturity. It considers the current market price, face value, coupon rate, and time to maturity, accounting for the time value of money."
        },
        {
            "question": "What is a zero-coupon bond?",
            "options": [
                "A bond that pays no interest during its term and is sold at a deep discount to face value", 
                "A bond with a very low coupon rate close to zero", 
                "A bond that has defaulted on its interest payments", 
                "A bond with interest payments that decrease to zero over time"
            ],
            "correct_answer": 0,
            "explanation": "A zero-coupon bond pays no periodic interest (coupon) during its term. It's issued at a discount to its face value, and the investor receives the full face value at maturity, with the difference representing the implicit interest."
        },
        {
            "question": "What is the primary difference between corporate bonds and government bonds?",
            "options": [
                "Corporate bonds are always secured while government bonds are unsecured", 
                "Government bonds have higher yields than corporate bonds of similar maturity", 
                "Corporate bonds carry higher credit risk and typically offer higher yields than government bonds", 
                "Government bonds can be traded while corporate bonds cannot"
            ],
            "correct_answer": 2,
            "explanation": "Corporate bonds generally carry higher credit risk (risk of default) than government bonds, and to compensate investors for this additional risk, they typically offer higher yields than government bonds of similar maturity."
        },
        {
            "question": "What is duration in the context of bond investing?",
            "options": [
                "The time until a bond matures", 
                "A measure of a bond's price sensitivity to interest rate changes", 
                "The average time it takes to sell a bond in the secondary market", 
                "The period between interest payments"
            ],
            "correct_answer": 1,
            "explanation": "Duration is a measure of a bond's price sensitivity to interest rate changes. It indicates how much a bond's price will change when interest rates move. Bonds with longer duration are more sensitive to interest rate changes."
        },
        {
            "question": "What is a callable bond?",
            "options": [
                "A bond that can be converted into equity shares", 
                "A bond where the issuer can redeem it before maturity at a specified price", 
                "A bond where the investor can demand early repayment", 
                "A bond that offers variable interest rates"
            ],
            "correct_answer": 1,
            "explanation": "A callable bond gives the issuer the right to redeem (call back) the bond before its maturity date at a predetermined price. Issuers typically exercise this right when interest rates fall, allowing them to refinance at lower rates."
        },
        {
            "question": "How are long-term capital gains on listed bonds taxed in India?",
            "options": [
                "10% without indexation", 
                "20% without indexation", 
                "10% with indexation or 20% without indexation, whichever is lower", 
                "10% without indexation or 20% with indexation, whichever is lower"
            ],
            "correct_answer": 3,
            "explanation": "Long-term capital gains (held > 12 months) on listed bonds in India are taxed at 10% without indexation or 20% with indexation, whichever results in lower tax liability for the investor."
        }
    ]
}

# Video resources for each module
video_resources = {
    "Insurance": [
        {"title": "Understanding Insurance - Comprehensive Guide", "url": "https://youtu.be/z6XAZve99xY?si=WIV_03Yp1WqQNxg6"}
    ],
    "Equity": [
        {"title": "Equity Investment Fundamentals", "url": "https://youtu.be/WEDIj9JBTC8?si=i5SJlaCMuiuLAgLn"}
    ],
    "PMS & AIF": [
        {"title": "Portfolio Management Services Explained", "url": "https://youtu.be/0zu0a8MCmk4?si=DqVdTJCw0jNIr40V"},
        {"title": "Alternative Investment Funds Guide", "url": "https://youtu.be/hEnp1dvzjag?si=HdeMwQ3AMGFBjzwV"}
    ],
    "Stocks": [
        {"title": "Stock Market Investing Guide", "url": "https://youtu.be/p7HKvqRI_Bo?si=UhKnneMKO6RpOELi"}
    ],
    "Bonds": [
        {"title": "Bond Investment Fundamentals", "url": "https://youtu.be/nMLVn_n1hb8?si=plAqOJmjaW2a1_js"}
    ]
}

# PDF resources for each module
pdf_resources = {
    "Insurance": [
        {"title": "Complete Guide to Insurance Planning", "url": "https://www.irdai.gov.in/ADMINCMS/cms/whatsNew_Layout.aspx?page=PageNo4446&flag=1"},
        {"title": "Insurance Policy Comparison Toolkit", "url": "https://policyholder.gov.in/knowyourpolicy.aspx"},
        {"title": "Health Insurance Claim Checklist", "url": "https://www.irdai.gov.in/ADMINCMS/cms/frmGeneral_Layout.aspx?page=PageNo4167&flag=1"},
        {"title": "Tax Benefits of Insurance Investments", "url": "https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1"}
    ],
    "Equity": [
        {"title": "Equity Investment Fundamentals", "url": "https://www.sebi.gov.in/sebi_data/faqfiles/jun-2018/1528282643226.pdf"},
        {"title": "Stock Market Analysis Techniques", "url": "https://www.bseindia.com/static/investors/investor_education.aspx"},
        {"title": "Beginner's Guide to Share Trading", "url": "https://www.nseindia.com/learn/education-monitor-investments"}
    ],
    "PMS & AIF": [
        {"title": "High Net Worth Investment Guide", "url": "https://www.sebi.gov.in/sebi_data/attachdocs/1487576082993.pdf"},
        {"title": "AIF Categories Comparison", "url": "https://www.sebi.gov.in/sebi_data/commondocs/aifreg_p.pdf"}
    ],
    "Stocks": [
        {"title": "Stock Market Investor Manual", "url": "https://www.nseindia.com/learn/education-monitor-investments"},
        {"title": "Technical Analysis Basics", "url": "https://www.bseindia.com/downloads1/BSE_Brokers_Forum_Training_on_Technical_Analysis.pdf"}
    ],
    "Bonds": [
        {"title": "Fixed Income Investment Guide", "url": "https://www.rbi.org.in/Scripts/FAQView.aspx?Id=79"},
        {"title": "Government Securities Guide", "url": "https://www.rbi.org.in/Scripts/FAQView.aspx?Id=172"}
    ]
}
