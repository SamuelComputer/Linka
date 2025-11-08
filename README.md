# Linka


# Linka 🔗
A real-time chat web application built with **Django Channels**, **WebSockets**, and **Daphne**.  
It allows users to send and receive messages instantly — similar to WhatsApp Web.

---

## 🚀 Features
- Real-time chat with WebSockets  
- User authentication  
- Modern responsive UI  
- Message persistence in the database  
- ASGI support with Daphne  

---

## 🛠️ Technologies
- Django 5+
- Channels
- Daphne
- HTML, CSS, JavaScript
- SQLite (for local testing)

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/SamuelComputer/Linka.git

# Navigate into the project
cd Linka

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
