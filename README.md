# Traffic Violation System

## Overview
A comprehensive web-based traffic violation management system built with Django. This system enables efficient handling of traffic violations, including reporting, tracking, and managing violations with features like QR code generation and face recognition for enhanced security.

## Features
- **User Authentication & Authorization**
  - Role-based access control (Admin, Staff, Regular Users)
  - Secure login and registration system
  - Password reset functionality

- **Violation Management**
  - Record and track traffic violations
  - Generate violation tickets
  - QR code integration for quick access to violation details
  - Face recognition for identity verification
  - NCAP violation handling
  - Adjudication process management

- **User Portal**
  - Personal dashboard for users
  - View and track violation history
  - Online payment integration
  - Document upload capability

- **Administrative Features**
  - User management
  - Violation type configuration
  - System-wide announcements
  - Activity logging and monitoring
  - Report generation

## Technology Stack
- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: SQLite (Development) / MySQL (Production)
- **Authentication**: Django Authentication System
- **Additional Libraries**:
  - Face Recognition
  - QR Code Generation
  - PDF Generation
  - Image Processing

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- MySQL (for production)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/xf00889/traffic-violation-system.git
   cd traffic-violation-system
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   - Copy `.env.example` to `.env`
   - Update the environment variables in `.env` with your configurations
   ```bash
   cp .env.example .env
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the System
- **Main Application**: http://localhost:8000
- **Admin Interface**: http://localhost:8000/admin

### User Types and Capabilities
1. **Admin Users**
   - Full system access
   - User management
   - System configuration
   - Report generation

2. **Staff Users**
   - Violation recording
   - Ticket generation
   - User assistance

3. **Regular Users**
   - View personal violations
   - Make payments
   - Submit appeals

## Development

### Project Structure
```
traffic_violation_system/
├── CAPSTONE_PROJECT/      # Project settings
├── traffic_violation_system/  # Main application
├── templates/             # HTML templates
├── static/               # Static files
├── media/                # User-uploaded files
└── requirements.txt      # Project dependencies
```

### Key Components
- `settings.py`: Project configuration
- `urls.py`: URL routing
- `views.py`: View logic
- `models.py`: Database models
- `forms.py`: Form definitions

## Security Features
- SSL/TLS encryption support
- CSRF protection
- Password hashing
- Session management
- Face recognition verification
- QR code authentication

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Production Deployment
- Configure production settings
- Set up a production database
- Configure static file serving
- Set up SSL certificates
- Use a production-grade web server (e.g., Nginx)
- Configure environment variables

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, please open an issue in the GitHub repository or contact the development team.

## Acknowledgments
- Django Framework
- Bootstrap
- Face Recognition Libraries
- QR Code Generation Tools
- All contributors and testers
