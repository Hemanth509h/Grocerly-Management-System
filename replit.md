# Elite Grocers - Project Documentation

## Overview
Elite Grocers is a comprehensive e-commerce web application built with Flask and MongoDB. The project features a multi-role system supporting customers, distributors, and administrators with role-based access control.

## Current State
- **Status**: Fully functional Flask application running on port 5000
- **Last Updated**: September 10, 2025
- **Flask Server**: Running successfully with all blueprints registered

## Recent Changes
- **September 10, 2025**: 
  - Fixed Flask server port configuration (changed from 50959 to 5000)
  - Created comprehensive README.md with detailed project documentation
  - Added .gitignore file with Python/Flask-specific exclusions
  - Created MIT LICENSE file for open source distribution
  - Updated project documentation in replit.md

## Project Architecture

### Technology Stack
- **Backend**: Python 3.11 with Flask framework
- **Database**: MongoDB with PyMongo driver
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Security**: bcrypt for password hashing
- **Architecture**: Modular blueprint design

### Key Components
1. **main.py**: Flask application entry point
2. **sub_main_py/**: Flask blueprints for different functionalities
   - index.py: Main user interface and authentication
   - admin.py: Administrator dashboard and controls
   - distributor.py: Distributor-specific features
   - add_edit_product.py: Product management system
   - forgotpasswordpage.py: Password reset functionality
   - db.py: MongoDB connection and configuration
3. **templates/**: HTML templates for all pages
4. **static/**: CSS stylesheets, JavaScript files, and product images

### Features Implemented
- Multi-role authentication (customer, distributor, admin)
- Product catalog with image support
- Shopping cart and order management
- Admin dashboard with user and order management
- Distributor regional order tracking
- Password reset functionality
- Responsive design with dark theme

## User Preferences
- **Coding Style**: Modular Flask blueprint architecture
- **Database**: MongoDB for flexible document storage
- **Security**: bcrypt password hashing, session management
- **UI/UX**: Dark theme with green accent colors, responsive design

## Deployment Configuration
- **Port**: 5000 (corrected from 50959)
- **Host**: 0.0.0.0 (allows external connections)
- **Debug Mode**: Enabled for development
- **Session Secret**: Configured (should be environment variable in production)

## Dependencies
- flask: Web framework
- pymongo: MongoDB driver
- bcrypt: Password hashing

## GitHub Repository Setup
✅ README.md - Comprehensive project documentation
✅ .gitignore - Python/Flask specific exclusions
✅ LICENSE - MIT license
✅ requirements.txt - Python dependencies
✅ Proper project structure with clear separation of concerns

## Next Steps for Production
1. Move database connection strings to environment variables
2. Use production WSGI server (gunicorn)
3. Set up proper secret key management
4. Configure production database
5. Add comprehensive testing suite
6. Set up CI/CD pipeline

## Security Considerations
- Passwords are properly hashed with bcrypt
- Session management implemented
- Role-based access control in place
- Input validation for all forms
- Admin PIN verification for sensitive operations

## Performance Notes
- MongoDB collections properly organized
- Image upload with base64 encoding
- Static file serving configured
- JavaScript modules separated by functionality
- CSS organized by component/page