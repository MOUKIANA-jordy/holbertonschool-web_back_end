const express = require('express');

// Create an Express application
const app = express();

// Define a route for the endpoint /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the Express application
module.exports = app;
