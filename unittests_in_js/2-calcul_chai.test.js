const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber using Chai', function () {
  describe('SUM', function () {
    it('should return 6 when adding 1.4 and 4.5', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 5 when adding 1.2 and 3.7', function () {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });

    it('should return 8 when adding 2.5 and 4.6', function () {
      expect(calculateNumber('SUM', 2.5, 4.6)).to.equal(8);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when subtracting 1.4 and 4.5', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0 when subtracting 2.5 and 2.5', function () {
      expect(calculateNumber('SUBTRACT', 2.5, 2.5)).to.equal(0);
    });

    it('should return 1 when subtracting 5.5 and 4.6', function () {
      expect(calculateNumber('SUBTRACT', 5.5, 4.6)).to.equal(1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when dividing 1.4 by 4.5', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return Error when dividing by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return 2.5 when dividing 5.2 by 2.4', function () {
      expect(calculateNumber('DIVIDE', 5.2, 2.4)).to.equal(2.5);
    });

    it('should return -2.5 when dividing -5.2 by 2.4', function () {
      expect(calculateNumber('DIVIDE', -5.2, 2.4)).to.equal(-2.5);
    });
  });
});
