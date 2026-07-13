# 📧 Spam Mail Prediction using Machine Learning

A Machine Learning project that classifies emails as Spam or Ham (Not Spam) using Logistic Regression and TF-IDF Vectorization.

The model is trained on a labeled spam email dataset and allows users to enter custom email messages for real-time spam detection through an interactive command-line interface.

Live Demo Link: https://spam-mail-prediction-zqqftax5wzhus4tvuqsiwz.streamlit.app/
---

# 🚀 Features

- Spam Mail Classification
- Text Preprocessing
- TF-IDF Vectorization
- Logistic Regression Classifier
- Train/Test Split
- Model Evaluation
- Interactive User Input
- Real-Time Spam Detection

---

# 📂 Dataset

The project uses a labeled spam email dataset containing two classes:

- Ham → Legitimate Email
- Spam → Unwanted or Promotional Email

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Jupyter Notebook

---

# 📈 Project Workflow

Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Label Encoding
      │
      ▼
Train/Test Split
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Train Logistic Regression Model
      │
      ▼
Evaluate Accuracy
      │
      ▼
Interactive Spam Prediction
---

# 💻 Interactive Prediction

The program allows users to enter any email message.

Example:

Enter Email:

Congratulations!
You've won a FREE iPhone.
Click the link below to claim your prize.
Output:

Prediction:
Spam Mail
or

```text
Prediction:
Ham Mail

The model can classify completely unseen email messages entered by the user.

---

# 📁 Project Structure

text
Spam-Mail-Prediction/
│
├── Spam Mail Prediction.ipynb
├── README.md
└── requirements.txt

---

# ⚙️ Installation

Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/Spam-Mail-Prediction.git

Navigate into the project

bash
cd Spam-Mail-Prediction

Install the required libraries

bash
pip install -r requirements.txt

Launch Jupyter Notebook

bash
jupyter notebook
`

---

# 📊 Model Evaluation

The model is evaluated using:

- Accuracy Score

The classifier was also tested on real email messages outside the dataset to verify its ability to generalize.

---

# 🧠 What I Learned

- Natural Language Processing (NLP) Basics
- TF-IDF Vectorization
- Logistic Regression
- Text Classification
- Data Preprocessing
- Interactive Machine Learning Applications
- Building an End-to-End ML Project

---

# 🚀 Future Improvements

- Flask Web Application
- Streamlit Dashboard
- Probability Scores
- Email File (.eml) Support
- Model Deployment
- Deep Learning-based Spam Detection

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome!

---

# 📜 License

This project is licensed under the MIT License.
