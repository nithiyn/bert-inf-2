import logging 
import torch
import torch_neuronx
from benchmark import benchmark
from bert_encode import BERTEncoder

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

encoder= BERTEncoder()

logging.info("encoding sequences")
example = encoder.encode(encoder.sequence_0, encoder.sequence_2, batch_size=4)
filename = 'model_4_batch.pt'
        
# Run benchmark
metrics = benchmark(filename, example)

# Log key metrics
logging.info(f"✅ Batch {batch_size}: {metrics['throughput']:.2f} inferences/sec")
print()