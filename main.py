import random
import time
import hashlib
import matrix

class USBAuthKey:
    def __init__(self):
        self.secret_key = str(random.getrandbits(256))
        self.current_state = None

    def generate_matrix(self):
        matrix_size = random.randint(3,5)
        matrix = []
        for i in range(matrix_size):
            row = []
            for j in range(matrix_size):
                row.append(random.randint(0, 255))
        matrix.append(row)
        return matrix

    def connect (self):
        self.current_state = self.generate_matrix()
        timestamp = str(time.time())
        data_to_hast = str (self.current_state) + timestamp + self.secret_key
        auth_token = hashlib.sha256(data_to_hast.encode()).hexdigest()
        return auth_token

    def disconnect (self):
        self.current_state = None

usb_key = USBAuthKey()
token = usb_key.connect()
print (f"Doğrulama token: {token}")
usb_key.disconnect()

