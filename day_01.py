import sys

NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def search_string(s: str) -> str:
  for num in NUMBERS:
    s = s.replace(num, f'{num}{NUMBERS[num]}{num}')
  
  return s

def extract_digits(s: str) -> list:
  res = []
  for ch in s:
    if ch.isdigit():
      res.append(ch)
  
  return res

def combine_digits(arr: list) -> int:
  return int(f'{arr[0]}{arr[-1]}')

def parse_lines(file):
  for l in file:
    raw_digits = extract_digits(search_string(l))
    number = combine_digits(raw_digits)
    yield number



def main():
  filename = sys.argv[1]
  output_filename = filename.replace("input", "output")
  
  with open(filename) as input_file:
    parsed_lines = list(parse_lines(input_file))
    result = sum(parsed_lines)
  
  with open(output_filename, 'w') as output_file:
    output_file.write(f'{result}\n')

if __name__ == "__main__":
  main()