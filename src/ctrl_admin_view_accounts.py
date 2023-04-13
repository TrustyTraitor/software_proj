from Entities.User import User

class ctrl_Admin_View_Accounts:
    def view_all_users(cls, users):
        for user in users:
            user.admin_view_accounts()