#!/usr/bin/node

const request = require('request');

// Function to fetch character names asynchronously
const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Unexpected status code: ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

// Function to fetch movie details and print character names
const printCharacters = async (movieId) => {
  try {
    // Fetch movie details
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const response = await new Promise((resolve, reject) => {
      request(movieUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(new Error(`Unexpected status code: ${response.statusCode}`));
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    // Fetch and print character names in order
    for (const characterUrl of response.characters) {
      const characterName = await fetchCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
};

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Ensure Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as an argument.');
  process.exit(1);
}

// Print characters for the specified Movie ID
printCharacters(movieId);
