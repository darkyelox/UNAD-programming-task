from exceptions_logger import ExceptionsLoggerHandler

def raise_error(msg: str):
    raise ValueError(msg)

def test_should_write_logger_on_error():
    ex_handler = ExceptionsLoggerHandler('test-logger')

    ex_handler.handle(
        execute=lambda:
            1/0,
        onError=lambda:
            print('There was an error'),
        onSuccess=lambda:
            print('Ok')
    )

    ex_handler.handle(
        execute=lambda:
            raise_error('This should not pass'),
        onError=lambda:
            print('There was an error'),
        onSuccess=lambda:
            print('Ok')
    )

    
test_should_write_logger_on_error()