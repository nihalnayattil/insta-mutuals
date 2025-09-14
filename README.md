# 👥 Instagram Mutuals Finder

A **Streamlit app** to find **mutual followers or mutual followings** between two Instagram accounts.  
Upload exported following/follower lists from Instagram and instantly see which accounts are followed by both profiles.

---

## 🚀 Features
- Compare **following lists** or **followers lists** of two Instagram accounts.  
- Find **mutual accounts** easily.  
- Display results in an interactive Streamlit table.  
- Shows the total number of mutual accounts.  
- Can also be used to find mutuals within a single account (between your followers and following).  

---

## 🔗 Exporting Instagram Data
You can export followers and following lists for free using tools like:  
👉 [EasyComment Instagram Export Tool](https://easycomment.ai/en/ig-follower-export-tool)  

Make sure your exported files are in `.xlsx` format.

> **Privacy note:** Rename files with neutral names (e.g., `account1_following.xlsx`, `account2_following.xlsx`) before sharing or committing them.

---

## 📂 Project Structure (example)
```

instagram-mutuals/
│── app.py                  # Main Streamlit app
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── account1\_following.xlsx # Placeholder for account 1 following list
│── account2\_following.xlsx # Placeholder for account 2 following list

````

---

## 🛠 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/nihalnayattil/insta-mutuals.git
cd insta-mutuals
pip install -r requirements.txt
````

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the link shown in your terminal (usually `http://localhost:8501`) in your browser.

Upload the following `.xlsx` files:

1. Account 1 following/followers list
2. Account 2 following/followers list

The app will display all **mutual accounts**.

---

## 📊 Example Output

* Total mutual accounts: **50**
* Interactive table with:

  * ID
  * User Name
  * Full Name
  * Profile URL
  * Avatar
  * Verified status

---

## ✅ Requirements

* Python 3.9+
* Dependencies listed in `requirements.txt` (tested versions):

```txt
pandas==2.3.2
streamlit==1.49.1
openpyxl==3.1.5
```

---

## 📌 Notes

* Input files must contain a column named **`User Name`**.
* Can be used for any two accounts where you have exported following/follower lists.
* Do not commit real personal data to public repositories.

---

## 📄 License

This project is for personal/educational use.
Feel free to modify and improve it!
