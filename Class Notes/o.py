def func(count):
  if count < 0:
    return
  print(f"{count} Lovely!")
  func(count - 1)
func(5)