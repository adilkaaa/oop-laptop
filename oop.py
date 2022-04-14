class Laptop:
    name = None
    cpu = None
    ram = None
    video_card = None
    hard_disk = None
    motherboard = None
    size_of_screen = None
    d = dict()

    # def __init__(self,cpu,ram,video_card,hard_disk,motherboard,size_of_screen):
        # self.cpu = cpu
        # self.ram = ram
        # self.video_card = video_card
        # self.hard_disk = hard_disk
        # self.motherboard = motherboard
        # self.size_of_screen = size_of_screen


    def add_to_dict(self,k,v):
        self.d[k] = v
        

    def show_dict(self):
        print(self.d)
        
acer = Laptop()
acer.cpu = 'AMD Athlon 3050U'
acer.ram = 8
acer.video_card = 'Radeon Graphics'
acer.hard_disk = 256
acer.motherboard = 'cer motherboard'
acer.size_of_screen = 15.6

acer.add_to_dict('model','Acer')
acer.add_to_dict('cpu', acer.cpu)
acer.add_to_dict('ram', acer.ram)
acer.add_to_dict('video_card', acer.video_card)
acer.add_to_dict('hard_disk', acer.hard_disk)
acer.add_to_dict('motherboard', acer.motherboard)
acer.add_to_dict('size_of_screen', acer.size_of_screen)

acer.show_dict()




