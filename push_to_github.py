import os

os.environ["GX_GITHUB"] = "1"
os.system('mkdocs gh-deploy')
