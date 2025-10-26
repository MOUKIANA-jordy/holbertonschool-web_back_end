// 4-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  it('should stub Utils.calculateNumber and verify console.log output', function () {
    // Création du stub : on remplace la vraie fonction par une version contrôlée
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Création d’un spy sur console.log
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Vérifie que la fonction Utils.calculateNumber a été appelée avec les bons arguments
    sinon.assert.calledOnce(stub);
    sinon.assert.calledWithExactly(stub, 'SUM', 100, 20);

    // Vérifie que console.log a bien affiché le message attendu
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWithExactly(consoleSpy, 'The total is: 10');

    // Nettoyage
    stub.restore();
    consoleSpy.restore();
  });
});
