# 📦 Smart Inventory & AI Pricing System

A full-stack, cross-platform application that integrates a **Spring Boot** backend with a **Python Machine Learning** service to automate inventory management and pricing strategy.

## 🚀 Overview

This project demonstrates **System Interoperability** by bridging Java and Python. It manages a product database via MySQL and uses an AI model to suggest optimal selling prices based on stock levels and categories.

## ✨ Key Features

- **Full-Stack Dashboard**: Responsive UI built with **Bootstrap 5** featuring real-time stock alerts and printable retail invoices.
- **AI-Powered Pricing**: A Python-based **Linear Regression** model that predicts recommended prices.
- **Cross-Platform Communication**: Java backend acts as a bridge, communicating with the Python AI via RESTful API calls.
- **Automated Data Persistence**: Integrated with **MySQL** using Spring Data JPA for seamless data management.

## 🛠️ Technology Stack

- **Backend**: Java (Spring Boot), Maven
- **AI/Service Layer**: Python 3.14, Flask, Scikit-learn, Pandas
- **Database**: MySQL
- **Frontend**: HTML5, JavaScript (Fetch API), Bootstrap 5

## ⚙️ Setup & Installation

### 1. Database Setup

- Create a database named `invoice_inventory_db` in MySQL.

### 2. Python AI Service

```bash
cd ai-price-predict
python -m venv venv
.\venv\Scripts\activate
pip install flask scikit-learn pandas mysql-connector-python
python train_model.py  # To train the model on MySQL data
python app.py          # To start the AI server on port 5000
```
