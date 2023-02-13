### Steps

1. Change directory to docker-elk
> cd docker-elk

2. Run the coommand for setup all services elasticsearch
>docker-compose up

3. Change directory to root
> cd ..

4. Run python script in docker. In this script occur parse csv to dict, sort and regular expressions. 
> docker-compose up

5. Change directory to elasticspa
> cd elasticspa

6. Run server and go to the [Link](http://localhost:8080/). On start page you can click on head table and do sort by every column(normal and reverse). In input you can search by customers_firstname
> docker-compose up

