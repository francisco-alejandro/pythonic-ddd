# Pythonic Application Architecture


This repo its a demo that describes an architecture known as the onion architecture. It uses the dependency injection principle extensively, and it is profoundly influenced by the Domain Driven Design (DDD) principles and some functional programming principles.

This layers implmentation means that we have a reference from one of the outer layers (infrastructure) to one of the inside layers (domain). In the onion architecture we are only allowed to reference from the outer layers to the inner layers and not the other way around.

So, in each subdomain whe can found three layers:

 - Domain: Where entites (main domain objects) are defined. In a nutshell,  we try to create a useful model of some problem, defining rules and events
 -  Application: It describe ways that our software can be used. So it defines the solution to a business logic problem
 -  Infraestructure: Here we can found controllers and repositories. Repositories are used in order to retrieve domain objects from persistence technologies using software design principles like the Liskov Subsitution Principle. Controllers can be the single place to capture all the defined use cases and manage all HTTP stuffs, like jsonify or get query params.
 

!["The Clean Architecture". From the golden Uncle Bob archives.](https://khalilstemmler.com/img/blog/ddd-intro/clean.jpg)

A http request follows the next path through the onion architecture.

![RESTful HTTP ](https://khalilstemmler.com/img/blog/clean-architecture/execution-cycle.svg)

## Demo code
It implements three endpoints.

- An endpoint to get detail for a given user (balance). **GET** /users/:user_id
	Example Id: "826d26eb-a820-4a2f-a453-69731484799b"
	 
- An endpoint to make a transfer of money between two users. 
	**POST** /wallets/wallets/transfer. Example request body:
	```
    {
		"originUserId": "826d26eb-a820-4a2f-a453-69731484799b",
		"targetUserId": "9d2c74aa-490b-4c41-9b93-99f5ca55cf71",
		"amount": 10
	}
	```
- A health check endpoint. **GET** /

 This demo is dockerized, so to run it, simply execute:

> bash run-docker.sh

 inside root project folder. By default app listens in 5280 port, but it can be changed using environment variables, see **services.envar** file. run-docker.sh script also creates demo data to test the app
 

 