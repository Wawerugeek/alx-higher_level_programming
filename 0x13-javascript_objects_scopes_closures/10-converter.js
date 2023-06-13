#!/usr/bin/node
exports.converter = function (base) {
  return (number) => number.toString(base);
};
