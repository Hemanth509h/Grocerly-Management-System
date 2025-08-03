from flask import Flask
from sub_main_py.index import index_bp
from sub_main_py.distributor import distributor_bp
from sub_main_py.admin import admin_bp
from sub_main_py.add_edit_product import add_edit_product_bp
from sub_main_py.forgotpasswordpage import forgotpassword_bp


app = Flask(__name__)
app.secret_key = "123456789789456123"

# Register Blueprints
app.register_blueprint(index_bp, url_prefix="/index")
app.register_blueprint(distributor_bp, url_prefix="/distributor")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(add_edit_product_bp, url_prefix="/add_edit_product")
app.register_blueprint(forgotpassword_bp, url_prefix="/forgotpassword")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=50959)
