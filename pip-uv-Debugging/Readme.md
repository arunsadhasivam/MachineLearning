

pip install:
============
  
  pip install --no-cache-dir -r requirements.txt
  
  usually it remember failure which happen previous and keep failing. to avoid clear and run requirement to get exact output
  i change the requirement  for e.g transformers==4.6.1 to transformers since latest has .whl older does not have precompiled bundles.
  it continues to fail because it remember old failures.
