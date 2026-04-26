# 📌 Flask + MongoDB Assignment Project

## 🚀 Overview

This project is a simple full-stack web application built using **Flask** and **MongoDB Atlas**. It demonstrates backend API development, frontend form handling, database integration, and proper error handling.

---

## 🎯 Features

* 🔹 **API Endpoint (`/api`)**

  * Reads data from a backend JSON file (`data.json`)
  * Returns data as a JSON response

* 🔹 **Frontend Form**

  * Accepts user input (Name, Email)
  * Sends data to backend via POST request

* 🔹 **MongoDB Integration**

  * Stores submitted data in MongoDB Atlas

* 🔹 **Success & Error Handling**

  * Redirects to success page on successful submission
  * Displays error on same page if submission fails

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** MongoDB Atlas
* **Frontend:** HTML (Jinja2 Templates)
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
flask-assignment/
│── app.py
│── data.json
│── requirements.txt
│── README.md
│── .env
│── .gitignore
│
├── templates/
│   ├── form.html
│   ├── success.html
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-link>
cd flask-assignment
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
MONGO_URI=your_mongodb_connection_string
```

---

### 4. Run the Application

```
python app.py
```

---

## 🌐 Application URLs

| Feature      | URL                           |
| ------------ | ----------------------------- |
| Form Page    | http://127.0.0.1:5000/        |
| API Endpoint | http://127.0.0.1:5000/api     |
| Success Page | http://127.0.0.1:5000/success |

---

## 📸 Screenshots

> *(Add your screenshots here before submission)*

* ✅ Flask server running
* ✅ API JSON response (`/api`)
* ✅ Form UI
* ✅ Success page
* ✅ MongoDB Atlas data

---

## 🔍 API Details

### GET `/api`

**Description:**
Returns data from `data.json`

**Response Example:**

```json
[
  {
    "name": "John",
    "email": "john@example.com"
  }
]
```

---

## 🧠 Error Handling

* If MongoDB insertion fails:

  * The error is displayed on the form page
  * No redirection occurs

---

## ⚠️ Notes

* MongoDB connection string is stored securely using `.env`
* `.env` file is excluded from version control via `.gitignore`

---

## 📌 Submission Details

* ✔ GitHub repository link included
* ✔ Screenshots attached
* ✔ Working API and form submission

---

## 📚 Conclusion

This project demonstrates:

* Building REST API using Flask
* Handling frontend form submissions
* Integrating with MongoDB Atlas
* Implementing success/error workflows

---

## 🔗 Repository Link

> *(Add your GitHub repo link here)*

---
