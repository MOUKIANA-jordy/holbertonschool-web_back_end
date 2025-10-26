// 6-payment_token.js

function getPaymentTokenFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ data: 'Successful response from the API' });
    } else {
      // Rejette la promesse immédiatement si success est false
      reject(new Error('Failed response from the API'));
    }
  });
}

module.exports = getPaymentTokenFromAPI;
