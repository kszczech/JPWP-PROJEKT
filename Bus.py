class Bus:

  def __init__(self, name, seats, empty_seat):
    self.name = name
    self.seats = seats
    self.empty_seat = empty_seat
    self.list = []


  def __repr__(self):
    return self.name + ':\n' + '\n'.join(str([t[0] + ' ' + t[1] + ' - Kierunek: ' + t[2] + '; Zabawometr: ' + str(t[3]) for t in self.list]).split(','))



