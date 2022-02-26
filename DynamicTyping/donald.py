# https://baike.baidu.com/item/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B/10845665?fr=aladdin
class Duck:
    def quack(self):
        print ("这鸭子在呱呱叫")

    def feathers(self):
        print ("这鸭子拥有白色与灰色羽毛" )

    def donald(self):
        print ("我不是donald")
 
class Person:
    def quack(self):
        print ("这人正在模仿鸭子")

    def feathers(self):   
        print ("这人在地上拿起1根羽毛然後给其他人看")

def in_the_forest(duck):
        duck.quack()
        duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()