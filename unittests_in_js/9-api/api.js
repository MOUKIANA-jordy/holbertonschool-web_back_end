const express = require('express');

const app = express();

// Route GET /
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Route GET /cart/:id avec validation que :id est un nombre
app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

// Port du serveur
const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

// Export pour tests
module.exports = app;
