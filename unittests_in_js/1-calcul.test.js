const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when adding 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 5 when adding 1.2 and 3.7', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('should return 7 when adding 2.5 and 4.6', function () {
      assert.strictEqual(calculateNumber('SUM', 2.5, 4.6), 8);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when subtracting 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when subtracting 2.5 and 2.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 2.5), 0);
    });

    it('should return 1 when subtracting 5.5 and 4.6', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.5, 4.6), 1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when dividing 1.4 by 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return Error when dividing by 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return 2.5 when dividing 5.2 by 2.4', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.2, 2.4), 2.5);
    });

    it('should return -2.5 when dividing -5.2 by 2.4', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -5.2, 2.4), -2.5);
    });
  });
});
