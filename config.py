
class Config():
    def __init__(self):
        self.map = {}
        self.map['padding'] = 5
        self.map['win_height'] = 480
        self.map['win_width'] = 640
        self.map['win_background'] = 'gray'
        self.map['maze_rows'] = 15
        self.map['maze_cols'] = 25
        self.map['cell_size_x'] = 25
        self.map['cell_size_y'] = 25

    def load(self, filename):
        try:
            with open(filename, 'r') as f:
                line = f.readline()
                while line != '':
                    key_value = line.split('=')
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        if value.isdigit():
                            value=int(value)
                        print(f'{key}={value}')
                        self.map[key]=value
                    line = f.readline()


        except FileNotFoundError:
            print(f'file {filename} not found')
        except Exception as e:
            print(f'An error occurred: {e}')

    def getMap(self):
        return self.map
