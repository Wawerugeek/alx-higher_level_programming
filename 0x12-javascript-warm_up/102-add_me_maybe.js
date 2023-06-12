#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  return (theFunction(++number));
};
