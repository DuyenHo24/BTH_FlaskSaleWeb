from saleapp.models import Category, Product
from saleapp import db, app
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')

class ProductView(ModelView):
    column_searchable_list = ['name','description'] #tìm kiếm
    column_filters = ['name','price'] #lọc
    can_view_details = True #xem chi tiết
    can_export = True #xuất excel
    column_exclude_list = ['image'] #ẩn cột
    column_labels = {
        'price': 'Giá',
        'description': 'Mô tả'
    } #đổi tên cột

    def is_accessible(self):
        return current_user.is_authenticated

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category, db.session, name='Danh mục'))
admin.add_view(ProductView(Product, db.session, name='Sản phẩm'))
admin.add_view(StatsView(name='Thống kê'))