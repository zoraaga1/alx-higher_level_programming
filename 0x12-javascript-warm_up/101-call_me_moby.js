#!/usr/bin/node

exports.executeXTimes = function (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};
