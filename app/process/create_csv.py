import pandas as pd
from dataclasses import dataclass


@dataclass
class BookData:
    name: str
    auther: str


class CreateBook(BookData):
    def __init__(self,
                 start: int = None,
                 length: int = 10,
                 ):
        self.start = start
        self.length = length

    def create_csv(self):
        name_list = []
        auther_list = []
        for i in range(self.start, self.length):
            name = f'book_{str(i)}'
            auther = f'auther_{str(i)}'
            name_list.append(name)
            auther_list.append(auther)

        dic = {
            "name": name_list,
            "auther": auther_list,
        }
        df = pd.DataFrame(dic)
        df.to_csv("books.csv", index=False)
        print("ここ")
