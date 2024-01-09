#!/usr/bin/node

exports.executeXTimes = function (x, theFunction) {
    while (x-- > 0) {
        theFunction();
    }
};
