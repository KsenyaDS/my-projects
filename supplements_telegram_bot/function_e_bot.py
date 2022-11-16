import re
from supplements_data import supplements_info, danger_levels_info,danger_levels_order

def prepare_text(composition):
  return re.sub(r"\s+", " ", composition.lower())


def get_supplement_info(composition):
  return_data = {}


  for supplement in supplements_info:
    danger_level = supplement['danger_level']
    code = supplement['code']
    variants = supplement['variants']

    human_code = ''

    if danger_level not in return_data: return_data[danger_level] = []

    if re.search(r"\b(e|е)-?%s\b" % code, composition, re.IGNORECASE):
      human_code += f'Е{code}'

    for variant in variants:
      if variant in composition:
        human_code += f' ({variant})' if human_code else variant
    
    if human_code: return_data[danger_level].append(human_code)

  return_string = ''
  for danger_level in danger_levels_order:

    if len(return_data[danger_level]) > 0:

      return_string+= f'{danger_levels_info[danger_level]}\r\n{", ".join(return_data[danger_level])}\r\n\r\n'

  return return_string

# print (get_supplement_info('E100'))




