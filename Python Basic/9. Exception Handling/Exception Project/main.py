from datetime import datetime

class WidgitException(Exception):
    message = 'Generice Widget Exception.'

    def __init__(self, *args, custom_message=None):
        super().__init__(args)
        if args:
            self.message = args[0]
        self.custom_message = custom_message if custom_message is not None else self.message

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:]
        }
        print(f'EXCEPTION:{datetime.utcnow().isoformat()}: {exception}')


class SupplierException(WidgitException):
    message = "Supplier Exception"

