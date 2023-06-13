#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((listElement, i) => list[list.length - i - 1]);
};
