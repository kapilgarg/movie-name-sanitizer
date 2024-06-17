import spacy
from spacy.training.example import Example
import random
from tqdm import tqdm
from config import resolution,qualitie,d_types
from utils import generate_test_train_data



patterns_resol = [{"label": "resolution", "pattern": resolution} for resolution in resolution]
patterns_quality = [{"label": "quality", "pattern": quality} for quality in qualitie]
patterns_type = [{"label": "dim", "pattern": d_type} for d_type in d_types]

model = 'en_core_web_sm'
iterations = 10

def get_ner_pipe(nlp):
    if 'ner' not in nlp.pipe_names:
        nlp.add_pipe('ner', last=True)
        
    ner = nlp.get_pipe('ner')
    return ner

def add_entity_rules(nlp):
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns_resol)
    ruler.add_patterns(patterns_quality)
    ruler.add_patterns(patterns_type)

def add_ner_labels(ner, data):
    for _, annotations in data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])
        
def train_ner(nlp, exclude_pipes,train_data):
    with nlp.disable_pipes(*exclude_pipes):
        for _ in range(iterations):
            random.shuffle(train_data)
            losses = {}
            
            for text, annotations in tqdm(train_data):
                text = text.replace("~"," ").replace("."," ").lower()
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example],losses=losses,drop=0.5)
            print(losses)



def main():
    test_data, train_data = generate_test_train_data()
    nlp = spacy.load(model)
    
    ner = get_ner_pipe(nlp)
    
    add_entity_rules(nlp)
    
    add_ner_labels(ner, train_data)
    
    exclude_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    
    train_ner(nlp, exclude_pipes,train_data)
    
    nlp.to_disk('movie-name-sanitizer')
    

if __name__ == '__main__':
    main()
    
    
    
    
    





    