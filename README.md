# Smart Bulk Email Sender 📧

A Python-based bulk email automation tool designed to send personalized HTML emails to multiple recipients — while avoiding spam filters. It supports authenticated SMTP (like SendGrid, Gmail, or Mailgun), HTML templating, throttling, and proper email headers to ensure high deliverability.

---

## ✅ Features

- 📬 Send personalized emails to many recipients from a CSV file
- 🛡️ Avoid spam filters using proper MIME structure and best practices
- 🔐 Works with secure SMTP services (SendGrid, Gmail, Mailgun, etc.)
- 🧠 Includes HTML + plain-text fallback to maximize inbox delivery
- ⏱️ Throttled email sending to avoid bulk spam flagging
- 🗂️ Modular project structure for easy customization and scaling
- 📄 Logs email delivery status to `email_log.txt`

---

Project Structure
bulk_email_sender/
│
├── email_config.json       # SMTP settings
├── recipients.csv          # Recipient email list
├── templates/
│   └── email_template.html # HTML email body
├── sender.py               # Main script to send emails
├── utils.py                # Helpers (CSV loading, logging)
└── email_log.txt           # Sent/failed log
 
## 🚀 How to Use

### 1. Setup SMTP Configuration

Create a file called `email_config.json`:

```json
{
  "smtp_server": "smtp.sendgrid.net",
  "port": 465,
  "sender_email": "your_email@domain.com",
  "username": "apikey",
  "password": "your_sendgrid_api_key"
}



