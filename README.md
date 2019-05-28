Python program to query OMDB API

- Build docker container

1) Generate OMDB API key
https://www.omdbapi.com/apikey.aspx

2) Clone git code
# git clone https://github.com/nbayapu7/omdbapi-python.git

3) Place the API KEY in Dockerfile
ENV OMDB_API_KEY xxxxxxxxx

4) Build Dockerfile
# cd omdbapi-python
# docker build -t omdb-api:python .

5) Run container
# docker run -it <image id>

6) Instructions to use python script, example:
*) Help message 
root@bf94f5d524c8:~# python omdbapi.py -h

omdbapi.py [options]
Options:
-t | --title  "Movie Title"
-h | --help   "Print help message"


*) Query a title
root@bf94f5d524c8:~# python omdbapi.py -t "speed"





 
 
