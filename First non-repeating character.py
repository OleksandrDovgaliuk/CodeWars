def first_non_repeating_letter(string):
  stringCopy = "".join([x.lower() for x in string])
  for s in stringCopy:
    if stringCopy.count(s) == 1:
      if s.isalpha():
        if s in string: return s
        if s.upper() in string: return s.upper()
      else:
        return s
  return ""


from TestFunction import Test
test = Test(None)   
