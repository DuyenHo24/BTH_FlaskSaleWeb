from saleapp.models import Category, Product, User
import hashlib
from saleapp import db
def load_categories():
    return Category.query.all()

def load_products(cate_id=None, kw=None):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.all()

#lấy chi tiết sản phẩm
def get_product_by_id(product_id):
    return Product.query.get(product_id)

#hàm chứng thực người dùng
def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()) #strip()là cắt khoảng trắng 2 đầu

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first() #.first() xc thực lấy thằng đầu tiên
def get_user_by_id(user_id):
    return User.query.get(user_id)

def register(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username.strip(), password=password, image=avatar) #a=b thì a là tên trường trong lớp models
    db.session.add(u)
    db.session.commit()