#  Global FinTech Digital Payments — Business Problem Statement


##  Project Context

In the digital payments industry, companies process millions of transactions daily across
multiple countries, currencies, payment channels, and customer segments. While the volume
of data generated is enormous, most businesses struggle to convert that data into decisions
that protect revenue, reduce risk, and improve customer experience.

This project simulates the work of a data analyst embedded in a fintech company's analytics
team. Using a realistic, messy dataset of **~100,000 payment transactions** spanning three
years across 12 countries, we will clean, analyse, and visualise the data to answer the
questions that actually matter to business stakeholders.

---

##  The Core Problem

> **Businesses are losing revenue, customers, and competitive advantage because transaction data sits in raw, uncleaned systems that no one has turned into insights.**

Specifically, this dataset addresses seven interconnected business problems that a
real fintech analytics team would be tasked with solving.

---

##  Business Problems We Are Solving

---

###  Problem 1 — Fraud & Financial Risk Exposure

**The Problem:**
The business has no clear picture of where fraud is concentrating. Fraud is not
distributed evenly — it clusters around specific payment methods, geographies,
devices, and time windows. Without identifying this fingerprint, the risk team
is applying blanket policies that create friction for legitimate customers while
missing targeted fraud patterns entirely.

**What We Will Do:**
Analyse fraud rates across payment method, country, device type, and time of day.
Quantify the total revenue lost to fraudulent transactions and chargebacks.
Identify the specific combinations of conditions that predict fraud likelihood.

**Business Impact:**
Enables the Risk and Compliance team to build targeted fraud detection rules,
reduce chargeback costs, and protect revenue without degrading the experience
for low-risk customers.

---

### Problem 2 — Revenue Leakage Nobody Is Tracking

**The Problem:**
The business is losing money through channels it has not identified.Failed
transactions that were never retried, discounts applied beyond approved thresholds,
chargeback losses concentrated in a small number of merchants, and FX losses on
cross-border transactions that have never been quantified. This is called revenue
leakage, and in payments businesses it is often significant and entirely preventable.

**What We Will Do:**
Calculate the total revenue lost through declined and failed transactions by payment
method. Identify merchants with disproportionately high chargeback rates. Measure the
impact of above-threshold discounts on net revenue. Quantify FX erosion across
currency corridors.

**Business Impact:**
Gives the CFO and Finance team a concrete dollar figure for preventable revenue loss,
and prioritises which leakage channels to close first.

---

###  Problem 3 — No Clear View of Revenue Trends & Seasonality

**The Problem:**
Leadership knows revenue is growing, but cannot clearly articulate which markets,
product categories, and customer segments are driving that growth — or whether
Q4 peaks represent sustainable acquisition or one-time spikes that collapse in Q1.
Without this clarity, budget allocation for the next year is based on intuition
rather than evidence.

**What We Will Do:**
Build a month-over-month and year-over-year revenue trend analysis. Decompose
revenue by country, product category, and customer segment. Investigate whether
seasonal spikes are driven by new customers or increased activity from existing ones.

**Business Impact:**
Equips the CFO and commercial leadership with a clear revenue narrative they can
use to allocate budgets, set targets, and communicate performance to investors.

---

###  Problem 4 — Customer Segments Are Not Being Served Correctly

**The Problem:**
The business classifies customers into segments (Retail, SME, Corporate, Premium,
Basic) but has no evidence that these segments predict actual spending behaviour
or lifetime value. High-value customers may be misclassified and receiving
low-priority service, while resources are being spent retaining customers who
generate minimal long-term revenue.

**What We Will Do:**
Analyse customer lifetime value (CLV) distribution across segments. Identify
mismatches where CLV does not align with segment classification. Examine whether
heavy discount users produce lower net revenue despite higher transaction volume —
a pattern known as margin cannibalism.

**Business Impact:**
Enables the Product and Marketing teams to fix segmentation models, redirect
retention spend toward genuinely high-value customers, and redesign discount
strategies that protect margins.

---

###  Problem 5 — Payment Channel Performance Is Unknown

**The Problem:**
The business accepts ten different payment methods but has no analytical view of
which channels drive the highest transaction values, which have the highest failure
rates, and which correlate with fraud. Engineering and product investment is being
made into payment integrations without knowing which ones actually generate value.

**What We Will Do:**
Compare average transaction value, completion rate, fraud rate, and net revenue
across all payment methods. Break this down further by customer segment and
geography to reveal which payment method works best for which market.

**Business Impact:**
Gives the Product and Engineering teams data-backed prioritisation for which payment
integrations to invest in, improve, or deprecate — turning intuition into a roadmap.

---

###  Problem 6 — Geographic Market Performance Is Opaque

**The Problem:**
The business operates across 12 countries but leadership cannot clearly answer which
markets are growing, which are underperforming relative to their potential, and where
the next expansion investment should be directed. Country-level revenue is known in
aggregate but has never been broken down by payment behaviour, product mix, or
customer quality.

**What We Will Do:**
Build a geographic revenue breakdown showing total revenue, average transaction value,
fraud rate, and dominant payment method by country. Identify high-volume but
low-value markets versus low-volume but high-value markets. Surface the markets
with the fastest growth trajectory over the three-year period.

**Business Impact:**
Provides the executive team with a market prioritisation framework grounded in data,
directly informing geographic expansion strategy and regional resource allocation.

---

###  Problem 7 — Operational Failures Are Costing Revenue Silently

**The Problem:**
Every declined or failed transaction is a moment where a willing customer could not
complete a purchase. These failures are logged in the system but have never been
analysed for patterns. Nobody knows whether failures spike at certain times of day,
on certain devices, or through certain payment methods — which means the operations
team cannot target the root cause.

**What We Will Do:**
Calculate overall and segmented transaction failure rates by payment method, device
type, platform, and hour of day. Estimate the total revenue lost to avoidable
failures. Identify the conditions that most strongly predict a transaction failing.

**Business Impact:**
Translates directly into sprint priorities for the Engineering team and operational
scheduling changes for the Ops team, with a clear revenue recovery figure attached
to each recommendation.

---

##  How These Problems Connect

These seven problems are not independent, they form a connected picture of
business health:

```
Revenue Trends (Problem 3)
        │
        ├──► Who is driving revenue? ──► Customer Segments (Problem 4)
        │
        ├──► Where is revenue leaking? ──► Revenue Leakage (Problem 2)
        │                                         │
        │                                         └──► Fraud (Problem 1)
        │
        ├──► Which channels work? ──► Payment Channels (Problem 5)
        │
        ├──► Which markets matter? ──► Geography (Problem 6)
        │
        └──► What is breaking? ──► Operations (Problem 7)
```

A complete analysis answers all seven. A stakeholder presentation tells the story
of how they connect  from the headline revenue number down to the specific
operational and product decisions that will move it.

---

## Analytical Approach

| Phase | Activity | Tool |
|-------|----------|------|
| 1 | Data Cleaning — fix nulls, duplicates, outliers, inconsistent categories | Python / Pandas |
| 2 | SQL Analysis — aggregations for business queries | SQL (SQLite3 ) |
| 3 | Exploratory Data Analysis — distributions, correlations, time series, fraud patterns | Seaborn / Matplotlib |
| 4 | Dashboard — executive KPIs, fraud monitor, segmentation, geographic view | Power BI |
| 5 | Storytelling — findings, root causes, and three actionable recommendations | Report / Presentation |

---

##  Key Questions We Will Answer

By the end of this project, we will have clear, data-backed answers to the following:

1. What is the month-over-month and year-over-year revenue trend, and which quarters peak?
2. Which product categories generate the highest net revenue versus highest volume?
3. What is the fraud rate by payment method, device type, and country?
4. Which merchants have the highest chargeback rates and what is the revenue impact?
5. Do discount-heavy customers produce lower net revenue despite higher transaction volume?
6. Which countries contribute the most revenue and which are underperforming?
7. What is the failed transaction rate by payment method, and what is the total revenue loss?
8. Which device and platform combination drives the highest completion rate and revenue?
9. What is the distribution of customer lifetime value across segments?
10. How do exchange rate fluctuations affect cross-border transaction revenue over time?

---

*Dataset: Global FinTech Digital Payments | 100,000 transactions | 22 fields | 12 countries | 3 years*