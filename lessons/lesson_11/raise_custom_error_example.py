
print(type(123))


class AgeError(Exception):

    def __init__(self, age):
        message = (f"You are not authorized to perform "
                   f"this action because your age is {age}")

        super().__init__(message)


raise AgeError(42)


