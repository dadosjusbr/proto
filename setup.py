import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='protoDadosjusbr',  
     version='0.82',
     author="Dadosjusbr",
     author_email="dadosjusbr@gmail.com",
     description="Contém esquema de dados e funções para os coletores do DadosjusBr",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/dadosjusbr/proto/",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )