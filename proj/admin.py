from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    # 重写登录页面
    login_template = 'admin/login.html'
