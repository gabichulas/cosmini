from utils import Utils
import unicodedata


class TextProcessing:
    def __init__(self):
        self.utils = Utils()
        self.text = None
        self.metadata = {}
    
    def load(self, normalize_unicode: bool = True, strip_whitespace: bool = True) -> str:

        raw_text = self.utils.read_data()
        
        if not raw_text or len(raw_text.strip()) == 0:
            raise ValueError(f"The file is empty or just contains spaces.")
        
        text = raw_text.replace('\r\n', '\n').replace('\r', '\n')
        
        if normalize_unicode:
            text = unicodedata.normalize('NFC', text)
        
        if strip_whitespace:
            text = text.strip()
        
        self.text = text
        
        self.metadata = {
            'raw_length': len(raw_text),
            'processed_length': len(text),
            'num_lines': text.count('\n') + 1,
            'num_chars': len(text),
            'num_chars_no_spaces': len(text.replace(' ', '').replace('\n', '').replace('\t', '')),
        }
        
        print(f"✓ Text loaded succesfully")
        
        return self.text
    
    def get_metadata(self) -> dict:
        if not self.text:
            raise RuntimeError("There is not text loaded. You must call load() first.")
        return self.metadata.copy()
    
    def sample(self, bound: int = 100):
        if not self.text:
            raise RuntimeError("There is not text loaded. You must call load() first.")
        print(self.text[:bound])
