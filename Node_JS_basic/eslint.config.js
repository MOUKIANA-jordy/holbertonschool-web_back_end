// eslint.config.js
const js = require('@eslint/js');

module.exports = [
  js.configs.recommended,
  {
    files: ['**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx'],
    rules: {
      // Ajoutez vos règles personnalisées ici
      'no-unused-vars': 'warn',
      'no-console': 'off',
    },
  },
];

