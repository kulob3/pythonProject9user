"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__status = False
        self.is_logged_in = True
        self.__is_admin = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_new(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password_new(self, value):
        self.__password = value

    @property
    def is_admin(self):
        return self.__status

    @is_admin.setter
    def _is_admin(self, value):
        self.__status = value

    def login(self, password):
        if password == self.__password:
            return True
        return False

    def logout(self):
        self.is_logged_in = False



# код для проверки
user1 = User("Alice", "qwerty")
# print(user1.name)  # Alice
# print(user1.password)  # qwerty
# print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword
#
# user1._is_admin = True
# print(user1.is_admin)  # True
#
# user1.login("newpassword")  # True
# user1.logout()