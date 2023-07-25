## Deploying a model as web -service 


'''bash
docker build -t ride-pred:v1 .
'''

'''bash 
docker run -it --rm -p 9696:9696 ride-pred:v1
'''