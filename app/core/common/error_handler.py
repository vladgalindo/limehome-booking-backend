from werkzeug.exceptions import Unauthorized, BadRequest, NotFound


def error_handler(code, message, ui_status):
    if code == 404:
        e = NotFound(message)
        e.data = {'ui': ui_status, 'status': 'error', 'sms': message}
        raise e
    if code == 401:
        e = Unauthorized(message)
        e.data = {'ui': ui_status, 'status': 'error', 'sms': message}
        raise e
    if code == 400:
        e = BadRequest(message)
        e.data = {'ui': ui_status, 'status': 'error', 'sms': message}
        raise e
