# from typing import List
#
# from fastapi import Request
#
#
# class UserCreateForm:
#     def __int__(self, request: Request):
#         self.request: Request = request
#         self.errors: List = []
#         self.username: str = None
#         self.email: str = None
#         self.password: str = None
#
#     async def load_data(self):
#         form = await self.request.form()
#         self.username = form.get('username')
#         self.email = form.get('email')
#         self.password = form.get('password')
#
#     async def is_valid(self):
#         if not self.username or not len(self.username) > 3:
#             self.errors.append('Имя пользователя должно включать не менее 3х символов')
#         if not self.email or not (self.email.__contains__('@')):
#             self.errors.append('Введите почту')
#         if not self.password or not len(self.password) > 4:
#             self.errors.append('Пароль должен включать себя не менее 4х символов')
#         if not self.errors:
#             return True
#         return False
