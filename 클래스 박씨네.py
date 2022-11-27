class HousePark:
    lastname = '박'
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print('%s, %s 여행을 가다.'%(self.fullname, where))

class HouseKim(HousePark) :
    lastname = '김'
    def travel(self, where, day):
        print('%s, %s 여행을 %d일 가다.'%(self.fullname, where, day))

pey = HousePark('을타')
pey.travel('베트남')

kimu = HouseKim('꼬무')
kimu.travel('독도', 7)