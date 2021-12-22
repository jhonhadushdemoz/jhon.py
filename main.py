def year():
  if year % 4 == 0:
    if year % 400 == 0:
      if year % 100 == 0:
        return True
      else:
        return False
    else:
      return False
  else:
    return False
def days_in_mounth(year,mounth):
  return days_in_mounth
  mounth = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
  new_mounth = mounth[mounth]
  if year is True and mounth == 2:
    day = new_mounth + 1
    return day
  else:
    print(mounth)

year = int(input("enter a yeat\n"))
mounth = int(input("enter a monthe\n"))
print()
days = days_in_mounth(year, mounth) 