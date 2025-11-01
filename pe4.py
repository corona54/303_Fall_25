import wikipedia
import time
import os
from concurrent.futures import ThreadPoolExecutor

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
# Set the search topic
topic = wikipedia.search('generative artificial intelligence')

def wiki_dl_and_save(topic):
    try:
        # Get the Wikipedia page for the topic
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title

        # Clean the title name to make it a valid filename
        clean_title = "".join(char for char in title if char not in r'\/:*?"<>|')
        file_path = os.path.join("references_output", f"{clean_title}.txt")

        # Get the reference URLs
        references = page.references

        # Write to the file
        with open(file_path, "w", encoding="utf-8") as f:
            for ref in references:
                f.write(ref + "\n")

        # Download confirmation message
        print(f"downloaded reference for:f {title}")

    # Exception handling
    except Exception as e:
            print(f"Failed to download references for: {topic}. Error: {e}")

# Measure start time        
start_time = time.perf_counter()

# Run the download and save function concurrently
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topic)

# Measure end time, and calculate elapsed time, then print it
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"\nTotal run time (concurrent): {elapsed:.2f} seconds")