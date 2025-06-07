# Regulatory-Change-Detector


# 🧠 AI-Powered Regulatory Change Detector

A functional prototype for identifying and analyzing changes between versions of regulatory documents — built as part of the Zipp.ai Intern Assessment Project (Case Study #1: *The Challenge of Regulatory Change*).

> Automates change detection and provides LLM-powered impact analysis using a local model (Mistral via Ollama). Built with Python + Streamlit.

---

## 🔍 Problem Statement

Regulated industries like pharmaceuticals and medical devices must comply with evolving standards from agencies like the US FDA, EMA, or CDSCO. These standards are published in long and dense documents that are frequently updated.

Currently, teams manually compare document versions to identify:

- 📌 What has changed?
- 📌 What is the type of change (new rule, clarification, etc.)?
- 📌 How might it impact internal SOPs?

This manual process is slow, error-prone, and risky.

---

## 🎯 Project Objective

To build an AI-powered tool that automates the initial stages of this workflow:

- ✅ Detect added, removed, and modified sections.
- ✅ Analyze each change using a local large language model (LLM).
- ✅ Provide clear insights about the nature and potential impact of each change.

---

## 🧰 Tech Stack

| Layer      | Tech/Tool |
|------------|-----------|
| Language   | Python 3.8+ |
| Frontend   | Streamlit |
| Backend    | Difflib for text comparison |
| AI Engine  | [Ollama](https://ollama.com/) with `mistral` model |
| File Types | `.txt` regulatory documents |

---
🖼️ App UI Preview

![Screenshot (51)](https://github.com/user-attachments/assets/6a51b84a-2535-429c-a9c4-8c82b7ddcee6)


1️⃣ File Upload Interface

![Screenshot (52)](https://github.com/user-attachments/assets/1b4d84a7-f307-486e-aed5-7625b7a47e08)

2️⃣ AI-Powered Change Summary


![Screenshot (53)](https://github.com/user-attachments/assets/4fa257aa-1e1c-4e0a-9a74-d9705a53dfbb)









