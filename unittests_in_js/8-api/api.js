// 8-api/api.js
const express = require('express');

const app = express();

// Route GET /
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Démarrage du serveur
const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

// Export pour les tests si besoin
module.exports = app;
