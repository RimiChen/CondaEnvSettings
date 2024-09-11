from transformers import cached_path
from shutil import rmtree

# Clear the Hugging Face cache
cache_dir = cached_path("")
rmtree(cache_dir)