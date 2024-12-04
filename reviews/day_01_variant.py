import sys



def extract_digits(s: str) -> list:
  res = list(filter(str.isdigit, s))

  return res

def combine_digits(arr: list) -> int:
  return int(f'{arr[0]}{arr[-1]}')


def parse_lines(file):
  for l in file:
    raw_digits = extract_digits(l)
    number = combine_digits(raw_digits)
    yield number

def main():
  filename = sys.argv[1]
  output_filename = filename.replace("input", "output")
  
  with open(filename) as input_file:
    result = sum(parse_lines(input_file))

  with open(output_filename, 'w') as output_file:
    output_file.write(f'{result}')

if __name__ == "__main__":
  main()

class MyRange:
  def __init__(self, upper_bound):
    self._upper_bound = upper_bound
    self._i = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    ret = self._i
    if ret >= self._upper_bound:
      raise StopIteration()
    self._i += 1
    return ret