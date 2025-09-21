import re 

class Block: 
    def __init__(self,text : str) : 
        self.text = text 
        self.start ,self.stop = [self.parse_block(block) for block in self.parse_line(self.text)]
        self.start_total_ms = self.start["HH"] * 3600000 + self.start["MM"] * 60000 + self.start["SS"] * 1000 + self.start["mmm"] 
        self.stop_total_ms = self.stop["HH"] * 3600000 + self.stop["MM"] * 60000 + self.stop["SS"] * 1000 + self.stop["mmm"] 

    @staticmethod
    def parse_line(text : str)->list[str]: 
        match = re.match(r"(?P<start>\d{2}:\d{2}:\d{2},\d{3}) --> (?P<stop>\d{2}:\d{2}:\d{2},\d{3})",text) 
        if match: 
            return [match.group("start"),match.group("stop")]
        return []
    
    @staticmethod
    def parse_block(block : str): 
        match = re.match(r"(?P<HH>\d{2}):(?P<MM>\d{2}):(?P<SS>\d{2}),(?P<mmm>\d{3})",block)
        block_dict = dict()
        if match: 
            block_dict["HH"] = int(match.group("HH"))
            block_dict["MM"] = int(match.group("MM"))
            block_dict["SS"] = int(match.group("SS"))
            block_dict["mmm"] = int(match.group("mmm"))
        return block_dict
    

    def shift(self,shift : int): 
        self.start_total_ms += shift
        self.stop_total_ms += shift
        self.start = self.Convert_total_ms(self.start_total_ms) 
        self.stop = self.Convert_total_ms(self.stop_total_ms) 

    @staticmethod
    def Convert_total_ms(total_ms : int): 
        block_dict = {
            "HH": total_ms // 3600000, 
            "MM": (total_ms % 3600000) // 60000, 
            "SS": (total_ms % 60000) // 1000 , 
            "mmm": total_ms % 1000
        }
        return block_dict

    def print_block(self): 
        print(self.timestamp())

    def timestamp(self)-> str : 
        return f"{self.start['HH']:02}:{self.start['MM']:02}:{self.start['SS']:02},{self.start['mmm']:03} --> {self.stop['HH']:02}:{self.stop['MM']:02}:{self.stop['SS']:02},{self.stop['mmm']:03}"


def sub_to_blocks(text : str) -> tuple[list[Block],list[str]]: 
    '''Parses the Subtitle contents and return a list of  Block objects or timespamps : str'''
    timestamps = re.findall(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}",text) 
    blocks = [Block(text) for text in timestamps] 
    return (blocks,timestamps)


def update_sub(contents : str,blocks : list[Block], timestamps : list[str]): 
    '''Takes in subtitle contents and Modifies it with the latest changes'''
    content = contents
    for block,stamp in zip(blocks,timestamps): 
        content = re.sub(stamp,block.timestamp(),contents)
    return content





