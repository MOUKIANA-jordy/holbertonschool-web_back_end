// 5-payment.test.js
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with hooks', function () {
  let consoleSpy;

  // Création du spy avant chaque test
  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
  });

  // Nettoyage après chaque test
  afterEach(function () {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" when called with 100, 20', function () {
    sendPaymentRequestToApi(100, 20);

    // Vérifie que console.log a été appelé une seule fois
    sinon.assert.calledOnce(consoleSpy);
    // Vérifie que le message affiché est correct
    sinon.assert.calledWithExactly(consoleSpy, 'The total is: 120');
  });

  it('should log "The total is: 20" when called with 10, 10', function () {
    sendPaymentRequestToApi(10, 10);

    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWithExactly(consoleSpy, 'The total is: 20');
  });
});
