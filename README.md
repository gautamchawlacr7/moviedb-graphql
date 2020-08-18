# moviedb-graphql

It is a GraphQL API which will help the user to track the movies that they have watched previously and will recommend new movies based on the movies they have watched.

To populate the database I have used [The MovieDB API](https://developers.themoviedb.org/3/getting-started/introduction).



### Requirements
- Python3.8
- Django
- pip
- To install other requirements go to the project path in command line and run:
```shell script
pip install -r requirements.txt
```
- Copy the .env.example
```shell script
cp .env.example .env
```
- Edit the .env file to set the environment variables for the project as per your system.

###Steps for starting the server
- To populate the database with the latest, popular and upcoming movies, run the following command:
```
python manage.py seedmovies
```
- To start the server, run the following command:
```
python manage.py runserver
```

###Features
- Show list of all movies present in the database.
- Show detailed data of a particular movie given id as the argument.
- User can create new list with a unique codename to identify the list. (this will act as a watched list)
- User can push a movie to a previously created list with its respective codename. (this will show that the movie is watched by the user).
- Finally, a general query will be written which will list all the recommended movies based on the items in a created list. (codename of the list will be provided to generate the recommendations).

### Queries and Mutations to access the features
### Getting Started
To access any feature the user needs to be authorized, so send the following requests to get started.
- Create a User
```
mutation{
  createUser(username:"", email:"", password:""){
    user{
      id
      username
      email
    }
  }
}
```

- Get Token Authentication
```
mutation{
  tokenAuth(username:"", password:""){
    token
  }
}
```

- Verify the Token that is provided after running the above request
```
mutation {
  verifyToken(token: ""){
    payload
  }
}
```

####Features
- Show list of all movies present in the database.
```
query {
  movies {
    id
    name
    avgRating
  }
}
```
- Show detailed data of a particular movie given id as the argument.
```
query {
  movies (movieId: ){ #provide movie id
    id
    name
    avgRating
  }
}
```
- User can create new list with a unique codename to identify the list. (This will act as a watched list.)
```
mutation{
  createList(codename:""){ #provide codename
    codename
  }
}
```
- User can push a movie to a previously created list with its respective codename. (This will show that the movie is watched by the user.)
```
mutation{
  addMovie(codename:"", movieId:){ #provide movie id and codename of the list
    userList{
      codename
      movieList{
        id
        avgRating
        name
      }
    }
 }
    
}

```
- Finally, a general query will be written which will list all the recommended movies based on the items in a created list. (Codename of the list will be provided to generate the recommendations.)
```
query{
    recommendations(codename:"<codename>"){
        id
        avgRating
        name
  }
}
```

###
The API is also deployed on [Heroku](https://moviedbgraphql.herokuapp.com/graphql)