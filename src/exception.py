import sys
import logging
def error_message_detail(error, error_detail: sys):
    _, _, error_tb = error_detail.exc_info()
    filename = error_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script[{0}] in line no : [{1}] error message : [{2}]".format(
        filename, error_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=sys)

    def __str__(self):
        return self.error_message

