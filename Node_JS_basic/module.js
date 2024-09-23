module.exports = {
    env: {
        browser: true,
        es2021: true,
        node: true, // Ajoutez ceci pour définir l'environnement Node.js
    },
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'airbnb-base', // Assurez-vous d'utiliser la bonne configuration
    ],
    parser: '@typescript-eslint/parser',
    plugins: ['react', '@typescript-eslint'],
    rules: {
        // Ajoutez vos règles personnalisées ici
    },
};

