# Elite Grocers - E-Commerce Web Application

A comprehensive e-commerce platform built with Flask and MongoDB, featuring role-based access control for customers, distributors, and administrators.

## Features

### User Management
- **Multi-role Authentication**: Support for customers, distributors, and administrators
- **Secure Login/Registration**: Password hashing with bcrypt
- **Password Reset**: Forgot password functionality
- **Session Management**: Secure user sessions with role-based access

### Product Management
- **Product Catalog**: Browse products by categories
- **Add/Edit Products**: Administrator and authorized users can manage inventory
- **Image Upload**: Product images with base64 encoding
- **Search & Filter**: Find products quickly
- **Real-time Updates**: Dynamic product loading

### Order Management
- **Shopping Cart**: Add, remove, and modify cart items
- **Order Placement**: Complete checkout process
- **Order Tracking**: View order history and status
- **Role-based Views**: Different order views for customers, distributors, and admins

### Administrative Features
- **Dashboard**: Admin panel with statistics and insights
- **User Management**: Manage customer and distributor accounts
- **Order Oversight**: View and manage all orders
- **Today's Orders**: Quick access to daily orders
- **Admin Authentication**: PIN-based admin verification

### Distributor Features
- **Regional Orders**: View orders specific to distributor's pincode
- **Order Management**: Process and track regional deliveries
- **Pincode-based Access**: Secure regional distribution control

## Technology Stack

- **Backend**: Python Flask with modular blueprint architecture
- **Database**: MongoDB with PyMongo
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Security**: bcrypt for password hashing, session management
- **Styling**: Custom CSS with responsive design
- **Architecture**: RESTful API design

## Project Structure

```
├── main.py                 # Flask application entry point
├── requirements.txt        # Python dependencies
├── sub_main_py/           # Flask blueprints
│   ├── index.py           # Main user routes
│   ├── admin.py           # Administrator functionality
│   ├── distributor.py     # Distributor-specific routes
│   ├── add_edit_product.py # Product management
│   ├── forgotpasswordpage.py # Password reset
│   └── db.py              # Database configuration
├── templates/             # HTML templates
│   ├── index.html         # Main user interface
│   ├── admin.html         # Admin dashboard
│   ├── distributor.html   # Distributor interface
│   ├── add_edit_product.html # Product management UI
│   ├── forgotpasswordpage.html # Password reset UI
│   └── error.html         # Error page
├── static/                # Static assets
│   ├── images/            # Product and logo images
│   └── stylesanjavascript/
│       ├── css/           # Stylesheets
│       └── js/            # JavaScript files
```

## Installation & Setup

### Prerequisites
- Python 3.11+
- MongoDB instance (local or cloud)
- Modern web browser

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd elite-grocers
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB**
   - Update database connection in `sub_main_py/db.py`
   - Ensure MongoDB is running and accessible

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:5000`
   - The application will be running in debug mode

## Usage

### For Customers
1. Register a new account or login with existing credentials
2. Browse the product catalog
3. Add items to your cart
4. Proceed to checkout and place orders
5. View your order history

### For Distributors
1. Login with distributor credentials
2. Enter your assigned pincode
3. View orders specific to your region
4. Manage and track deliveries

### For Administrators
1. Login with admin credentials
2. Access the admin dashboard
3. Manage users, products, and orders
4. View analytics and daily reports
5. Add, edit, or remove products

## API Endpoints

### Authentication
- `POST /index/login` - User login
- `POST /index/register` - User registration
- `GET /index/logout` - User logout
- `GET /index/loginornot` - Check login status

### Products
- `GET /index/products` - Fetch products
- `POST /AddProduct` - Add new product (Admin)
- `POST /EditProduct` - Edit existing product (Admin)
- `POST /DeleteProduct` - Delete product (Admin)

### Orders
- `POST /index/add_to_cart` - Add item to cart
- `POST /index/place_order` - Place order
- `POST /admin/get_orders` - Get all orders (Admin)
- `POST /admin/TodayOrders` - Get today's orders (Admin)

### User Management
- `POST /admin/get_users` - Get all users (Admin)
- `POST /admin/manage_user` - Manage user accounts (Admin)

## Database Schema

### Collections
- **users**: User accounts with roles (customer, distributor, admin)
- **Orders**: Order data with items, pricing, and delivery info
- **Complaints**: Customer complaint submissions
- **admins**: Administrator PIN verification
- **Product Categories**: Various product collections (groceries, etc.)

## Security Features

- Password hashing with bcrypt
- Session-based authentication
- Role-based access control
- Input validation and sanitization
- CSRF protection
- Admin PIN verification for sensitive operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please create an issue in the repository or contact the development team.

## Acknowledgments

- Flask community for the excellent web framework
- MongoDB for the flexible database solution
- All contributors who helped build this platform