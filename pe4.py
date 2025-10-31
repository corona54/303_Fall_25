import wikipedia
import time
import os
#####Section A###########################
sea = wikipedia.search('generative artificial intelligence')
#print(x)

start_time = time.perf_counter()
os.makedirs("references_output", exist_ok = True)

for i in sea:
    page = wikipedia.page(i, auto_suggest = False)
    title = page.title
    titl = "".join(char for char in title if char not in r'\/:*?"<>|')
    file_path = os.path.join("references_output", f"{titl}.txt")
    
    ref = page.references
    
    with open(file_path, "w", encoding = "utf-8") as f:
        for refs in ref:
            f.write(refs + "\n")
            
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"\n Total execution time: {elapsed:.2f} seconds")

#####Section B###########################
#sea is grabbed from section A
def wiki_dl_and_save(topic):