# Import necessary libraries and modules
from datetime import datetime
from tqdm import tqdm
from datasets import load_dataset
from concurrent.futures import ProcessPoolExecutor
from items import Item

# Constant variable declarations
CHUNK_SIZE = 1000
MIN_PRICE = 0.5
MAX_PRICE = 999.49

# ItemLoader.py loads and cleans product data from Hugging Face, creates Item objects for valid products, and uses parallel processing for speed. 
# It will download the dataset if needed.
# This file defines an ItemLoader class that loads, processes, and cleans product data from the Amazon Reviews 2023 dataset (using Hugging Face’s datasets library). 
# It creates Item objects (from your items.py file) for each valid product, filtering by price and cleaning the data in parallel for efficiency.

class ItemLoader:

    def __init__(self, name):
        """Initialize the ItemLoader with a dataset name."""
        self.name = name
        self.dataset = None

    def from_datapoint(self, datapoint):
        """
        Try to create an Item from this datapoint
        Return the Item if successful, or None if it shouldn't be included
        
        Tries to create an Item from a single datapoint:
        - Converts the price to float and checks if its within the allowed range.
        - Returns the Item if it should be included (based on its own logic), otherwise returns None        
        """
        try:
            price_str = datapoint['price']
            if price_str:
                price = float(price_str)
                if MIN_PRICE <= price <= MAX_PRICE:
                    item = Item(datapoint, price)
                    return item if item.include else None
        except ValueError:
            return None

    def from_chunk(self, chunk):
        """
        Create a list of Items from this chunk of elements from the Dataset.
        
        Processes a chunk (list) of datapoints, returning a list of valid Item objects.
        """
        batch = []
        for datapoint in chunk:
            result = self.from_datapoint(datapoint)
            if result:
                batch.append(result)
        return batch

    def chunk_generator(self):
        """
        Iterate over the Dataset, yielding chunks of datapoints at a time
        
        Yields chunks of the dataset for batch processing.
        """
        size = len(self.dataset)
        for i in range(0, size, CHUNK_SIZE):
            yield self.dataset.select(range(i, min(i + CHUNK_SIZE, size)))

    def load_in_parallel(self, workers):
        """
        Use concurrent.futures to farm out the work to process chunks of datapoints -
        This speeds up processing significantly, but will tie up your computer while it's doing so!
        
        Uses multiple processes to process chunks in parallel, speeding up data cleaning and item creation.
        - Uses tqdm to show progress.
        - Sets the category for each item.
        - Returns the list of all valid items.
        """
        results = []
        chunk_count = (len(self.dataset) // CHUNK_SIZE) + 1
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for batch in tqdm(pool.map(self.from_chunk, self.chunk_generator()), total=chunk_count):
                results.extend(batch)
        for result in results:
            result.category = self.name
        return results
            
    def load(self, workers=8):
        """
        Load in this dataset; the workers parameter specifies how many processes
        should work on loading and scrubbing the data
        
        Main method to load and process the dataset:

        - Downloads the dataset from Hugging Face (this will download data if not present locally).
        - Processes the data in parallel.
        - Prints timing and summary info.
        - Returns the cleaned list of items.
        """
        start = datetime.now()
        print(f"Loading dataset {self.name}", flush=True)
        self.dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", f"raw_meta_{self.name}", split="full", trust_remote_code=True)
        results = self.load_in_parallel(workers)
        finish = datetime.now()
        print(f"Completed {self.name} with {len(results):,} datapoints in {(finish-start).total_seconds()/60:.1f} mins", flush=True)
        return results