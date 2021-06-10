class User():
    def __init__(self, first_name, last_name, email, login):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.login_atempts = 0
    def describe_user(self):
        print(f'Имя : {self.first_name} \nФамилия : {self.last_name} \nemail : {self.login} \nlogin : {self.login}'
              f'\nПопыток входа: {self.login_atempts}'
              )
    def greet_user(self):
        print(f'\nПриветствую, {self.first_name} {self.last_name}')
    def increment_login_attempts(self):
        self.login_atempts+=1
    def reset_login_attempts(self):
        self.login_atempts=0
class Privilegies():
    def __init__(self, privilegies='Создание сообщений'):
        self.privilegies = privilegies
    def show_privilegies(self):
        print(f'Rights: {self.privilegies}')
class Admin(User):
    def __init__(self, first_name, last_name, email, login):
        super().__init__(first_name, last_name, email, login)
        self.privilegies = Privilegies()



admin = Admin('serg','lebedev','huyna@mail.ru','zalupakonya')
admin.describe_user()
admin.increment_login_attempts()
admin.describe_user()
admin.reset_login_attempts()
admin.describe_user()
admin.greet_user()
admin.privilegies.privilegies="Хуйсосня"
admin.privilegies.show_privilegies()