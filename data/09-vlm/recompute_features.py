from pathlib import Path
import json,hashlib,pickle,tarfile,time
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor
from huggingface_hub import HfApi
B=Path(__file__).parent;out=B;out.mkdir(exist_ok=True)
model_id='openai/clip-vit-base-patch32';rev='3d74acf9a28c67741b2f4f2ea7635f0aaf6f0268'
processor=CLIPProcessor.from_pretrained(model_id,revision=rev)
model=CLIPModel.from_pretrained(model_id,revision=rev,use_safetensors=False).eval();torch.set_num_threads(2)
archive=B/'cifar-10-python.tar.gz'
if not archive.exists():
 import urllib.request
 urllib.request.urlretrieve('https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',archive)
assert hashlib.md5(archive.read_bytes()).hexdigest() == 'c58f30108f718f92721af3b95e74349a'

with tarfile.open(archive) as t:
 def read(name):return pickle.load(t.extractfile('cifar-10-batches-py/'+name),encoding='bytes')
 train=[read('data_batch_'+str(i)) for i in range(1,6)];test=read('test_batch');meta=read('batches.meta')
 X=np.concatenate([r[b'data'] for r in train]).reshape(-1,3,32,32).transpose(0,2,3,1);y=np.concatenate([r[b'labels'] for r in train]);Xt=test[b'data'].reshape(-1,3,32,32).transpose(0,2,3,1);yt=np.array(test[b'labels']);classes=[x.decode() for x in meta[b'label_names']]
with torch.inference_mode():
 bare=model.get_text_features(**processor(text=classes,return_tensors='pt',padding=True)).numpy()
 photo=model.get_text_features(**processor(text=['a photo of a '+c for c in classes],return_tensors='pt',padding=True)).numpy()
for kind,offset in [('practice',0),('homework',10)]:
 for split,images,labels in [('validation',X,y),('test',Xt,yt)]:
  ids=np.concatenate([np.flatnonzero(labels==k)[offset:offset+10] for k in range(10)]); selected=images[ids]; features=[]
  for start in range(0,len(ids),8):
   with torch.inference_mode(): f=model.get_image_features(**processor(images=[Image.fromarray(a) for a in selected[start:start+8]],return_tensors='pt')).numpy()
   features.append(f)
  path=out/f'{kind}_{split}.npz';np.savez_compressed(path,features=np.concatenate(features),images=selected,labels=labels[ids],ids=np.array([('train' if split=='validation' else 'test')+':'+str(i) for i in ids]),text_bare=bare,text_photo=photo,classes=np.array(classes))
  print(path.name,'saved',flush=True)
manifest=dict(dataset='CIFAR-10',source='https://www.cs.toronto.edu/~kriz/cifar.html',archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),model=model_id,revision=rev,preprocessing='CLIPProcessor from pinned revision; RGB; default resize and center crop',selection='first 10 per class for practice, next 10 for homework; official train for validation, official test for test',files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('*.npz')})
(out/'manifest.json').write_text(json.dumps(manifest,indent=2));print('complete',rev,flush=True)
