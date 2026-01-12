# 1. 설계도(Class) 만들기
class Dog:
    # [준비 단계] 강아지가 태어날 때 정해지는 것들 (이름, 품종)
    def __init__(self, name, breed):
        self.name = name   # 이 강아지(self)의 이름 설정
        self.breed = breed # 이 강아지(self)의 품종 설정

    # [행동 단계] 강아지가 할 수 있는 기능 (짖기)
    def bark(self):
        print(f"{self.name}: 멍멍! 나는 {self.breed}이야.")

# 2. 설계도를 보고 실제 강아지(Object) 찍어내기
my_dog = Dog("초코", "푸들")
your_dog = Dog("백구", "진돗개")

# 3. 각 객체의 기능 사용하기
my_dog.bark()   # 출력: 초코: 멍멍! 나는 푸들이야.
your_dog.bark() # 출력: 백구: 멍멍! 나는 진돗개야.