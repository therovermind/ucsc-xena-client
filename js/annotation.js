// deprecated. Was used to draw ga4gh annotations.
/*global require: false, module: false */
'use strict';
var multi = require('multi');

function getType([type]) {
	return type;
}

module.exports = {
	draw: multi(getType)
};
