def list_to_dict(meta_list):
    meta_dict = {}
    for item in meta_list:
        key, value = item.split(":", 1)
        
        key = key.strip()
        value = value.strip().lstrip('<').rstrip('>')
        
        # Add to dictionary
        meta_dict[key] = value
        
    return meta_dict

def dict_to_list(input_dict):
    transformed_list = []
    for k, inner_dict in input_dict.items():
        # Create a new dictionary with 'name': k and update with inner_dict
        new_dict = {'text': k}
        new_dict.update(inner_dict)
        transformed_list.append(new_dict)
    return transformed_list

def translate_to_string(data_dict):
    return '\n'.join(f"{key}: {value}" for key, value in data_dict.items())

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def bold(string):
    return color.BOLD + str(string) + color.END
