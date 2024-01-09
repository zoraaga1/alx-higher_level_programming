#!/usr/bin/node

exports.converter = function (base) {
  Number.prototype.toString = function (base) {
    return this.constructor(this.valueOf()).toString(base);
  };
  return function (number) {
    return number.toString(base);
  };
};
