const express = require('express');

const app = express();

// Middleware pour parser le JSON du corps des requêtes POST
app.use(express.json());

// Route GET /
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Route GET /cart/:id
app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

// Route GET /available_payments
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// Route POST /login
app.post('/login', (req, res) => {
  const username = req.body.userName;
  res.send(`Welcome ${username}`);
});

// Port du serveur
const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
