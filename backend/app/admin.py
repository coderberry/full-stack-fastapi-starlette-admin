from starlette_admin import Admin, AdminApp
from app.models import User, Item
from app.core.config import settings

admin_app = AdminApp(
    title=settings.PROJECT_NAME,
    admin_path="/admin",
)

admin_app.add_model(User)
admin_app.add_model(Item)

def init_admin(app):
    admin_app.mount_to(app)
