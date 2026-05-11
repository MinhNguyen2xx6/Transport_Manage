# Transport Manage - Full-Stack Logistics System

Transport Manage is an integrated logistics and fleet management platform designed to digitize the entire lifecycle of transport operations. By bridging the gap between administrative coordination and financial tracking, the system provides a unified interface for dispatchers, accountants, and managers to oversee vehicle movements and fiscal health.

## 🌟 Project Overview

In a traditional logistics environment, data is often fragmented across paper logs and spreadsheets. Transport Manage centralizes this into a real-time system that automates calculations, validates business rules, and provides instant visibility into operational profitability.

## 🏗️ System Architecture

### 1. Backend Engine (FastAPI & PostgreSQL)

The backbone of the project, designed for speed and reliability:

- **RESTful API Architecture:** Provides a structured communication layer for the frontend and potential future mobile integrations.
- **Automated Financial Logic:** A dedicated Service Layer that computes Gross Profit, handles VAT calculations, and monitors vendor-to-revenue ratios.
- **Data Integrity:** Powered by SQLAlchemy and PostgreSQL, ensuring ACID-compliant transactions for sensitive financial records and trip data.
- **Real-time Notifications:** Implementation of WebSockets to provide instant updates to dispatchers when new orders are created or status changes occur.

### 2. Frontend Interface (React & Vite)

A responsive, high-performance web dashboard built for operational efficiency:

- **Component-Driven UI:** Built with React for a modular and maintainable codebase, utilizing a Vite-powered build pipeline for near-instant load times.
- **Real-time Dashboard:** Displays active trips, vehicle availability, and financial summaries at a glance.
- **Interactive Forms:** Dynamic validation for trip entries (e.g., license plate formats, numeric currency checks) to ensure clean data entry from the start.
- **State Management:** Efficiently handles complex logistics data flows across different views (Orders, Fleet, Debts).

## 🛠️ Core Modules

- **Fleet Management:** Tracking vehicle specifications, plate numbers, and ownership (internal vs. vendor).
- **Dispatch Order System:** Managing the full trip lifecycle from "Pending" to "Completed."
- **Financial & Debt Module:** Specialized tracking of advances, freight revenues, and debts owed to external vehicle owners or drivers.
- **Automated Reporting:** Generating summary insights into monthly performance and profit margins.

## 🎯 Project Goals

- **Efficiency:** Reducing the time spent on manual trip entry and profit calculation.
- **Accuracy:** Eliminating human error in financial reporting through automated Pydantic-based validation.
- **Transparency:** Providing a single source of truth for all stakeholders in the transport chain.

---

**Developed by:** Minh Nguyen (Backend Engineer)
**Organization:** Quang Nguyen General Transport Company Limited
**Description** https://docs.google.com/document/d/14pNZvUz7UrMZI5t0bKVUtYpeFibaV1CZtjKdEAAUsb0/edit?usp=sharing
