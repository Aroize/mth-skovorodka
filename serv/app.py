from tornado.web import Application
from tornado.ioloop import IOLoop
from controllers import *
from db import *

controllers = [
    AuthHandler,
    RegisterHandler
]

def create_application():
    urls = list(map(lambda handler: (handler.get_mapping(), handler), controllers))
    return Application(urls)


if __name__ == "__main__":
    app = create_application()
    app.listen(8888)
    IOLoop.instance().start()
    # user = User(-1, "Ilia", "Ilmenskii", "gipermonk@bk.ru", 21)
    # db_helper.insert_user(user)
    # result = db_helper.get_user_by_id(1)
    # print(result)
    db_helper.close()