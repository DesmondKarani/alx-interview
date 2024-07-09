#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the movie details based on the Movie ID
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch and print character names
const printCharacters = (characters) => {
  characters.forEach(character => {
    request(character, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
};

// Make a request to get the movie details
request(movieUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    printCharacters(characters);
  }
});
