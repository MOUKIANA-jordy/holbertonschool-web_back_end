// eslint.config.js
import js from '@eslint/js';

export default [
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

