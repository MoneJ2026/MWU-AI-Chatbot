# 🤖 MWU AI Chatbot

An intelligent AI-powered chatbot developed for **Madda Walabu University (MWU)**. The chatbot helps students quickly find information about university services using **Machine Learning**, **Natural Language Processing (NLP)**, and a **JSON knowledge base**.

---

## 📌 Features

* 🎓 Admission information
* 📚 Library information
* 💻 ICT support
* 🏥 Campus clinic information
* 🛏 Dormitory information
* ⚽ Sports information
* 🧪 Laboratory information
* 💼 Career services
* 🏫 University information
* 🌐 Official website information
* 🔒 Campus security
* 🧠 User memory (remember user name)
* 🌍 Multilingual support (English, Afaan Oromo, Amharic)
* 🤖 Machine Learning intent classification

---

## 🛠 Technologies Used

* Python 3
* Streamlit
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* RapidFuzz
* Joblib
* JSON

---

## 🧠 Machine Learning

This project uses **Supervised Machine Learning** for **Intent Classification**.

### Training Pipeline

```text
intents.csv
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Logistic Regression
      │
      ▼
Trained Model
      │
      ▼
model.pkl
```

The trained model predicts the user's intent, and the chatbot retrieves the correct answer from the appropriate JSON knowledge file.

---

## 📂 Project Structure

```text
MWU-Chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── config.py
├── memory.py
├── responses.py
├── utils.py
├── faq.py
│
├── ML/
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── encoder.pkl
│
├── data/
│   ├── intents.csv
│   ├── library.json
│   ├── admission.json
│   ├── ict.json
│   ├── clinic.json
│   ├── dormitory.json
│   ├── sports.json
│   ├── laboratory.json
│   ├── career.json
│   ├── academic.json
│   ├── university.json
│   ├── website.json
│   └── security.json
│
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/MoneJ2026/MWU-AI-Chatbot.git
```

Move into the project directory:

```bash
cd MWU-AI-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Machine Learning Model

```bash
cd ML
python train_model.py
```

This generates:

* model.pkl
* vectorizer.pkl
* encoder.pkl

inside the **models/** folder.

---

## ▶️ Run the Chatbot

Return to the project root and run:

```bash
python -m streamlit run app.py
```

---

## 💬 Example Questions

* Where is the library?
* How can I register?
* Where is the ICT office?
* Where is the clinic?
* Dormitory rules?
* Sports activities?
* Career services?
* Academic calendar?
* University history?
* Official website?

---

## 📈 Future Improvements

* Increase training dataset
* Confidence score prediction
* Semantic search
* Voice assistant
* Admin dashboard
* Mobile application
* RAG (Retrieval-Augmented Generation)
* LLM integration

---

## 👨‍💻 Developer

**Monet Girma**

Computer Science Student

Madda Walabu University

## 📄 License

This project is developed for educational and research purposes.
