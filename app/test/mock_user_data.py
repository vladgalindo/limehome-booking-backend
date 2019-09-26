VALID_USER = dict(
            email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "123456")

INVALID_USER = dict(
            email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "not the same")

ACTIVATED_USER = dict(
            email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "123456",
            is_active=True)