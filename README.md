### Steps

1. Change directory to docker-elk
> cd docker-elk

2. Run the command for setup all services elasticsearch
>docker-compose up -d

3. Change directory to root
> cd ..

4. Run python script in docker. In this script occur parse csv to dict, sort and regular expressions. 
> docker-compose up -d

5. Change directory to elasticspa
> cd elasticspa

6. Run server  
> docker-compose up -d

7. [Open in browser](http://localhost:8080/). On start page you can click on head table and do sort by every column(normal and reverse). In input you can search by customers_firstname
