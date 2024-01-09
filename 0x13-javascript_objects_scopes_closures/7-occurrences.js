#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentElement) => {
    if (currentElement === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
