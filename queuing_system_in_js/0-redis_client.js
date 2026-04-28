import redis from 'redis';

// Crée le client Redis
const client = redis.createClient();

// Gestion des erreurs
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connexion réussie
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
