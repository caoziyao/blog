# encoding: utf-8
# gunicorn -w4 -b0.0.0.0:3000 appcorn:application &

from main import configure_app
# from app import configure_manager
# from app import manager

application = configure_app()

# if __name__ == '__main__':
#     configure_manager()
#     application
#     manager.run()      