def loginPage(**kwargs):
    users = {'dilip':'dilip123', 'sam':'sam123', 'john':'john123'}
    userName=kwargs.get('userName')
    password=kwargs.get('password')
    try:#
        if userName is None or password is None:
            raise ValueError('userName and password are required')
        if userName not in users:
            raise ValueError('userName does not exist')
        if users[userName] != password:
            raise ValueError('password is incorrect')
        print("login successful")
    except Exception as e:
        print(e)
    finally:
        print("login attempt completed")
#loginPage(userName='dilip2', password='dilip123')
my_dict = { 'userName': 'dilip', 'password': 'dilip123' }
loginPage(**my_dict) 


