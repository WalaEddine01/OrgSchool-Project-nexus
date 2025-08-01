# OrgSchool - Django Version

A modern school management system built with Django and Django REST Framework. This is a complete refactored version of the original Flask-based OrgSchool application.

## 🚀 Features

- **User Authentication**: Custom user model for school administrators
- **School Management**: Create and manage schools
- **Class Management**: Organize students into different classes (Class 01-04)
- **Student Management**: Track student information including name, age, and class assignments
- **Teacher Management**: Assign teachers to classes and maintain records
- **REST API**: Full REST API with Django REST Framework
- **Admin Interface**: Django admin panel for advanced management
- **Responsive UI**: Modern Bootstrap 5-based interface
- **Automatic Setup**: Classes are automatically created upon registration

  <p>
    <a href="">🌐 Live Demo (not ready)</a> •
    <a href="#-getting-started">🚀 Quick Start</a> •
    <a href="API_DOC.md">📖 API Docs</a> •
  </p>

  <p>
    <a href="https://github.com/WalaEddine01">👨‍💻 GitHub</a> •
    <a href="https://twitter.com/w1laaeddine">🐦 Twitter</a> •
    <a href="https://www.linkedin.com/in/wala-eddine-boulebbina">💼 LinkedIn</a> •
    <a href="https://walaeddine.tech">📄 portfolio</a>
  </p>
</div>

---

## 📋 Overview

OrgSchool is a comprehensive **Student Management System (SMS)** designed to streamline the organization and administration of educational institutions. Built with modern web technologies, it provides a robust platform for managing students, teachers, classes, and administrative tasks efficiently.


## 📑 Table of Contents

- [📋 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [⚡ Quick Setup](#-quick-setup)
  - [🐳 Docker Setup (Optional)](#-docker-setup-optional)
- [💻 Usage](#-usage)
- [📖 API Documentation](#-api-documentation)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [👥 Contributors](#-contributors)
- [🆘 Support](#-support)
- [📄 License](#-license)

---

## ✨ Features

### 🔐 **Security & Authentication**
- **Secure User Authentication** with session management
- **Password Hashing** using industry-standard algorithms
- **Role-based Access Control** for different user types
- **Data Validation** to prevent malicious inputs

### 📊 **Management Capabilities**
- **Student Management**: Add, edit, remove, and track student information
- **Teacher Management**: Manage teacher profiles and assignments
- **Class Management**: Organize students into classes and subjects
- **School Administration**: Complete school data management

### 🎨 **User Experience**
- **Responsive Design** that works on all devices
- **Intuitive User Interface** with modern styling
- **Real-time Updates** for seamless user experience
- **Interactive Dashboard** with key metrics and insights

### 🔌 **API & Integration**
- **RESTful API** for third-party integrations
- **Swagger Documentation** for easy API exploration
- **JSON Data Exchange** for modern web standards
- **CORS Support** for cross-origin requests

---

## 🏗️ Architecture

OrgSchool follows a **Layered Architecture** pattern ensuring scalability and maintainability:

```
┌─────────────────────────────────┐
│     Presentation Layer          │
│   (HTML, CSS, JavaScript)       │
├─────────────────────────────────┤
│     Application Layer           │
│    (Flask Routes & Logic)       │
├─────────────────────────────────┤
│     Business Logic Layer        │
│      (Models & Services)        │
├─────────────────────────────────┤
│     Data Access Layer           │
│    (SQLAlchemy & MySQL)         │
└─────────────────────────────────┘
```


---

## 🛠️ Tech Stack

### **Backend**
- **Python 3.8+** - Core programming language
- **Flask 2.0+** - Web framework
- **SQLAlchemy** - ORM for database operations
- **MySQL 8.0+** - Primary database
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and validation

### **Frontend**
- **HTML5** - Markup language
- **CSS3** - Styling with modern features
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **jQuery** - DOM manipulation and AJAX

### **Development & Deployment**
- **Git** - Version control
- **Virtual Environment** - Dependency isolation
- **Swagger/Flasgger** - API documentation
- **CORS** - Cross-origin resource sharing

---

## 🚀 Getting Started

### 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download Python](https://python.org/downloads/))
- **MySQL 8.0 or higher** ([Download MySQL](https://mysql.com/downloads/))
- **Git** ([Download Git](https://git-scm.com/downloads))
- **pip** (usually comes with Python)

### ⚡ Quick Setup

#### 1. **Clone the Repository**
```bash
git clone https://github.com/WalaEddine01/OrgSchool-project-nexus-.git
cd OrgSchool-project-nexus 
```

#### 2. **Set Up Virtual Environment**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

#### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 4. **Configure Database**
```bash
# Start MySQL service
sudo systemctl start mysql  # On Linux
# brew services start mysql  # On Mac
# net start mysql            # On Windows

# Set up database
sudo mysql < setup/setup_mysql_dev.sql
```

#### 5. **Set Environment Variables** (Optional)
```bash
export ORG_TYPE_STORAGE=db
export ORG_API_HOST=0.0.0.0
export ORG_API_PORT=5001
```

#### 6. **Initialize Database Tables**
```bash
python3 -c "
from models import storage
storage.reload()
"
```

#### 7. **Start the Application**

**Frontend (Web Interface):**
```bash
python3 app.py
```
*Access at: [http://localhost:5002](http://localhost:5002)*

**API Server:**
```bash
python3 -m api.v1.app
```
*Access at: [http://localhost:5001](http://localhost:5001)*

**API Documentation:**
*Access Swagger docs at: [http://localhost:5001/apidocs](http://localhost:5001/apidocs)*

### 🐳 Docker Setup (Optional)

For a containerized setup, you can use Docker:

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run individual services
docker build -t orgschool .
docker run -p 5002:5002 orgschool
```

---

## 💻 Usage

### 🔐 **Admin Registration & Login**
1. Navigate to the registration page
2. Create an admin account with school details
3. Login with your credentials
4. Access the admin dashboard

### 🏫 **School Management**
- **Create Schools**: Set up your educational institution
- **Manage Classes**: Organize students by grade and section
- **Track Students**: Add, edit, and monitor student information
- **Teacher Assignment**: Assign teachers to classes and subjects

### 📊 **Dashboard Features**
- **Real-time Statistics**: View student and teacher counts
- **Quick Actions**: Rapidly add new students or teachers
- **Data Overview**: Get insights into school operations

---

## 📖 API Documentation

OrgSchool provides a comprehensive RESTful API for integration with external systems:

- **📚 Full API Documentation**: [API_DOC.md](API_DOC.md)
- **🔍 Interactive Swagger Docs**: [http://localhost:5001/apidocs](http://localhost:5001/apidocs)

### Quick API Examples:

**Get API Status:**
```bash
curl http://localhost:5001/api/v1/status
```

**Create New Admin:**
```bash
curl -X POST http://localhost:5001/api/v1/admins \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@school.com",
    "password": "securepassword",
    "school_name": "Example School"
  }'
```

**Get All Students:**
```bash
curl http://localhost:5001/api/v1/sclasses/{class_id}/students
```

---

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python3 -m pytest tests/

# Run specific test file
python3 -m pytest tests/test_models/

# Run with coverage
python3 -m pytest --cov=models tests/
```

### Test Coverage:
- **Unit Tests**: Model validation and business logic
- **Integration Tests**: Database operations
- **API Tests**: Endpoint functionality
- **UI Tests**: Form validation and user interactions

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help make OrgSchool better:

### 🐛 **Bug Reports**
When filing an issue, please include:
- **Clear Description**: What happened vs. what you expected
- **Steps to Reproduce**: Detailed steps to recreate the issue
- **Environment**: OS, Python version, browser (if applicable)
- **Screenshots**: If relevant, include visual evidence

### ✨ **Feature Requests**
- Check existing issues to avoid duplicates
- Clearly describe the feature and its benefits
- Provide examples of how it would be used

### 🔧 **Pull Requests**
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### 📝 **Development Guidelines**
- Follow **PEP 8** style guidelines for Python code
- Add **tests** for new features
- Update **documentation** as needed
- Ensure **backwards compatibility** when possible

---

## 👥 Contributors

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/WalaEddine01">
          <img src="https://avatars.githubusercontent.com/u/135642375?s=150&v=4" width="150px;" alt="Wala Eddine B"/>
          <br />
          <sub><b>Wala Eddine Boulebbina</b></sub>
        </a>
        <br />
        <sub>🏗️ Project Creator & Lead Developer</sub>
        <br />
        <a href="https://github.com/WalaEddine01" title="GitHub">🐙</a>
        <a href="https://linkedin.com/in/wala-eddine-boulebbina" title="LinkedIn">💼</a>
        <a href="https://twitter.com/w1laaeddine" title="Twitter">🐦</a>
      </td>
    </tr>
  </table>
</div>

### 🙏 **Special Thanks**
- **Inspiration**: [ostad.education.gov.dz](https://ostad.education.gov.dz/) - Algerian Ministry of Education platform
- **Community**: All contributors and users who provide feedback and suggestions

---

## 🆘 Support

Need help? We're here for you!

### 📧 **Contact Options**
- **📨 Email**: [walaaeddine33@gmail.com](mailto:walaaeddine33@gmail.com)
- **💬 GitHub Discussions**: [Project Discussions](https://github.com/WalaEddine01/OrgSchool-project-nexus /discussions)
- **🐛 Issues**: [Report a Bug](https://github.com/WalaEddine01/OrgSchool-project-nexus /issues)

### 📚 **Resources**
- **📖 API Documentation**: [API_DOC.md](API_DOC.md)
- **🌐 Live Demo**: [walaeddine.tech](http://walaeddine.tech)

### 💝 **Support the Project**
If you find OrgSchool helpful, consider:
- ⭐ **Starring** the repository
- 🐛 **Reporting** bugs or issues
- 💡 **Suggesting** new features
- 📢 **Sharing** with others
- 🤝 **Contributing** code or documentation

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Wala Eddine Boulebbina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">
  <h3>🌟 Star this repository if you found it helpful!</h3>
  <p>
    <a href="https://github.com/WalaEddine01/OrgSchool-project-nexus /stargazers">
      <img src="https://img.shields.io/github/stars/WalaEddine01/OrgSchool-project-nexus ?style=social" alt="GitHub stars">
    </a>
    <a href="https://github.com/WalaEddine01/OrgSchool-project-nexus /network/members">
      <img src="https://img.shields.io/github/forks/WalaEddine01/OrgSchool-project-nexus ?style=social" alt="GitHub forks">
    </a>
  </p>
  
  <p><em>Made with ❤️ by <a href="https://github.com/WalaEddine01">Wala Eddine Boulebbina</a></em></p>
  
  <sub>🚀 Building the future of education management, one commit at a time.</sub>
</div>

