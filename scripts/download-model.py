#!/usr/bin/env python3
import os
import urllib.request
from torchvision.models import ResNet152_Weights

weights = ResNet152_Weights.DEFAULT
url = weights.url
filename = url.split('/')[-1]

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
dedup_data = os.getenv('DEDUP_DATA', os.path.join(project_root, 'data'))
model_dir = os.path.join(dedup_data, 'models', 'checkpoints')
os.makedirs(model_dir, exist_ok=True)

target_path = os.path.join(model_dir, filename)

if os.path.exists(target_path):
    print(f"Model already exists: {target_path}")
    exit(0)

print(f"Downloading ResNet152 weights...")
print(f"  URL: {url}")
print(f"  Target: {target_path}")

try:
    urllib.request.urlretrieve(url, target_path)
    size_mb = os.path.getsize(target_path) / (1024 * 1024)
    print(f"Download complete! ({size_mb:.1f} MB)")
except Exception as e:
    print(f"Download failed: {e}")
    exit(1)
