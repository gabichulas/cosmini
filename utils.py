class Utils():
    @staticmethod
    def read_data():
        with open("data/data.txt", "r", encoding="utf-8") as f:
            text = f.read()
        return text
    
    @staticmethod
    def read_data_limited(char_limit):
        with open("data/data.txt", "r", encoding="utf-8") as f:
            text = f.read(char_limit)
        return text