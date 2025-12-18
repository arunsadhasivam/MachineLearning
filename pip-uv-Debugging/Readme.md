

pip install:
============
  
        pip install --no-cache-dir -r requirements.txt

  Important:
  ===========
  
        really worked , this helps to install changed version.        
  
  usually it remember failure which happen previous and keep failing. to avoid clear and run requirement to get exact output
  i change the requirement  for e.g transformers==4.6.1 to transformers since latest has .whl older does not have precompiled bundles.
  it continues to fail because it remember old failures.

print architecture:
=====================
    
    python -c "import platform; print(platform.architecture())"
    
  output:
  =======
  
    ('64bit', 'WindowsPE')


comment:
=========

in requirement.txt comment like this a space **before** and **after** the comment is required

    urllib3 # ==1.26.5  correct
    urllib3# ==1.26.5   not correct 
    urllib3 #==1.26.5   not correct
