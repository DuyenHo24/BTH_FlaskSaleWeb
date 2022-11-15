from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from saleapp import db, app
from flask_login import UserMixin
from enum import Enum as UserEnum

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default = 0)
    image = Column(String(100))
    active = Column(Boolean, default = True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    image = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        import hashlib
        password = str(hashlib.md5('12345678'.encode('utf-8')).hexdigest())
        u = User(name='Duyen', username='Duyenadmin', password=password,
                 image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                 user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()
        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # p1 = Product(name='Iphone 13', description='Apple, 128GB', price=20000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p2 = Product(name='Iphone 14', description='Apple, 256GB', price=25000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p3 = Product(name='Samsung galaxynote 10', description='Samsung, 256GB', price=28000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p4 = Product(name='iPad Pro 2022', price=22000000, description='Apple, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=2)
        # p5 = Product(name='Galaxy Tab S8', price=24000000, description='Samsung, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=2)
        # db.session.add_all([p1,p2,p3,p4,p5])
        # db.session.commit()

        # p6 = Product(name='Iphone 13', description='Apple, 128GB', price=20000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p7 = Product(name='Iphone 14', description='Apple, 256GB', price=25000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p8 = Product(name='Samsung galaxynote 10', description='Samsung, 256GB', price=28000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # db.session.add_all([p6, p7, p8])
        # db.session.commit()
        # db.create_all()