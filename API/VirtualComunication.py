class VirtualComunication:

    """docstring for VirtualComunication"""

    def __init__(self):

        self.in_waiting = 0

    def write(self, mensaje):
        mensaje = mensaje.decode('utf-8')

        if mensaje[0] == 'M':

            if len(mensaje) == 4 and mensaje[1] == '0' and self.verify_led(mensaje[2]) and mensaje[3] == 'N':

                self.in_waiting = 1

        if mensaje[0] == 'T':

            if len(mensaje) == 11 and mensaje[-1] == 'U':

                try:
                    _ = int(mensaje[1:-1])
                    self.in_waiting = 1
                except:
                    pass

        if mensaje == 'W':

            self.in_waiting = 1

        if mensaje[0] == 'J':

            if len(mensaje) == 6 and self.verify_led(mensaje[1]) and mensaje[-1] == 'K':
                
                self.in_waiting = 1

    def read(self):

        self.in_waiting = 0

        return b'O'

    def close(self):

        pass

    def verify_led(self, val):

        if (val == '1' or val == '2' or val == '3' or val == '4'
            or val == '5' or val == '6' or val == '7' or val == '8'
            or val == '9' or val == 'A' or val == 'B' or val == 'C'
            or val == 'D' or val == 'E' or val == 'F'):

            return True

        else:

            return False
