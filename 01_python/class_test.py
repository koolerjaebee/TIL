# 생성자 역시 메서드(함수)기 때문에 추가인자를 받을 수 있습니다.
class Person:
    def __init__(self, name):
        self.name = name
        print(f'아 응애에요 by {self.name}')
    
    def __del__(self):
        print(f'Rust in pieces - {self.name}')


p = Person('ssafy')
