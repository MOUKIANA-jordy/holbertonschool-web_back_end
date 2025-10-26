// 3-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // Vérifie que la fonction a bien été appelée une fois
    sinon.assert.calledOnce(spy);
    // Vérifie qu’elle a bien été appelée avec les bons arguments
    sinon.assert.calledWithExactly(spy, 'SUM', 100, 20);

    spy.restore(); // Important pour éviter des effets de bord
  });
});
